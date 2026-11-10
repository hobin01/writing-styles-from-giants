import argparse
import shutil
import sys
import tempfile
from pathlib import Path


PAYLOAD = Path(__file__).parent / "payload"
HOSTS = {
    "codex": (".agents/skills", ".agents/skills"),
    "claude": (".claude/skills", ".claude/skills"),
    "opencode": (".opencode/skills", ".config/opencode/skills"),
    "pi": (".pi/skills", ".pi/agent/skills"),
}


def same_copy(source, target):
    if target.is_symlink():
        return False
    if source.is_dir():
        if not target.is_dir():
            return False
        names = {child.name for child in source.iterdir()}
        if names != {child.name for child in target.iterdir()}:
            return False
        return all(same_copy(source / name, target / name) for name in names)
    return (target.is_file() and target.stat().st_size == source.stat().st_size
            and target.read_bytes() == source.read_bytes())


def install(source, base, host, user_scope, dry_run):
    project_path, user_path = HOSTS[host]
    skills_root = base
    for part in Path(user_path if user_scope else project_path).parts:
        skills_root /= part
        if skills_root.is_symlink():
            raise ValueError(f"Skill path contains a symlink: {skills_root}")
        if skills_root.exists() and not skills_root.is_dir():
            raise ValueError(f"Skill path is not a directory: {skills_root}")

    target = skills_root / "wsg"
    if target.is_symlink() or target.exists():
        if same_copy(source, target):
            return f"Already installed at {target}"
        raise ValueError(f"Existing path at {target}. Move it outside the skills directory before installing.")
    if dry_run:
        return f"Would install at {target}"

    skills_root.mkdir(parents=True, exist_ok=True)
    # Publish the complete skill in one rename so hosts cannot load a partial copy.
    with tempfile.TemporaryDirectory(prefix=".wsg-", dir=skills_root) as temporary:
        staged = Path(temporary) / "wsg"
        shutil.copytree(source, staged)
        try:
            staged.rename(target)
        except OSError:
            if same_copy(source, target):
                return f"Already installed at {target}"
            raise
    return f"Installed at {target}"


def main(payload=PAYLOAD):
    parser = argparse.ArgumentParser(prog="wsg", description="Install WSG writing methods for an agent.")
    parser.add_argument("--version", action="version", version=(payload / "VERSION").read_text().strip())
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("install")
    command.add_argument("--host", choices=HOSTS, required=True)
    command.add_argument("--global", dest="user_scope", action="store_true", help="install for your user")
    command.add_argument("--dry-run", action="store_true", help="show the destination without writing")
    args = parser.parse_args()
    try:
        base = Path.home() if args.user_scope else Path.cwd()
        print(install(payload, base, args.host, args.user_scope, args.dry_run))
    except (OSError, ValueError) as error:
        sys.exit(f"wsg: {error}")
