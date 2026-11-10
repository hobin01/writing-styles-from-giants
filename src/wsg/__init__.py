import argparse
import shutil
import sys
import tempfile
from contextlib import nullcontext
from pathlib import Path


PAYLOAD = Path(__file__).parent / "payload"
HOSTS = {
    "codex": (".agents/skills", ".agents/skills"),
    "claude": (".claude/skills", ".claude/skills"),
    "opencode": (".opencode/skills", ".config/opencode/skills"),
    "pi": (".pi/skills", ".pi/agent/skills"),
}


def select_hosts(explicit):
    if explicit:
        return list(dict.fromkeys(explicit))
    if not (sys.stdin.isatty() and sys.stdout.isatty()):
        raise ValueError("Specify --host HOST in noninteractive mode.")
    detected = [host for host in HOSTS if shutil.which(host)]
    if not detected:
        raise ValueError("No supported CLI found on PATH. Specify --host HOST to install explicitly.")
    print("Detected on PATH:", ", ".join(detected))
    try:
        names = input("Enter host names separated by spaces (Enter to cancel): ").split()
    except EOFError:
        names = []
    if not names:
        print("Cancelled.")
    for name in names:
        if name not in detected:
            raise ValueError(f"{name!r} is not a detected host. Choose from: {', '.join(detected)}.")
    return list(dict.fromkeys(names))


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


def install(source, base, host, user_scope, dry_run, *, link=False):
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
        if link and target.exists() and target.samefile(source):
            return f"Already available at {target}"
        if not link and same_copy(source, target):
            return f"Already installed at {target}"
        raise ValueError(f"Existing path at {target}. Move it outside the skills directory before installing.")
    if dry_run:
        if link:
            return f"Would link {target} to {source}"
        return f"Would install at {target}"

    skills_root.mkdir(parents=True, exist_ok=True)
    if link:
        try:
            target.symlink_to(source, target_is_directory=True)
        except FileExistsError:
            if target.is_symlink() and target.exists() and target.samefile(source):
                return f"Already linked to {source} at {target}"
            raise
        return f"Linked {target} to {source}"

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


def main(payload=PAYLOAD, *, prepare_copy=None, link_source=None):
    parser = argparse.ArgumentParser(prog="wsg", description="Install WSG writing methods for an agent.")
    parser.add_argument("--version", action="version", version=(payload / "VERSION").read_text().strip())
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("install")
    command.add_argument("--host", choices=HOSTS, action="append",
                         help="install for this host (repeatable); omit to select detected CLIs in a terminal")
    command.add_argument("--global", dest="user_scope", action="store_true", help="install for your user")
    command.add_argument("--dry-run", action="store_true", help="show the destination without writing")
    command.add_argument("--link", action="store_true", help="link to the adapter in a persistent Git checkout")
    args = parser.parse_args()
    if args.link and (link_source is None or not (link_source / "SKILL.md").is_file()):
        parser.error("--link requires install.py in a Git checkout. Omit --link to install a copy.")
    try:
        hosts = select_hosts(args.host)
        if not hosts:
            return
        base = Path.home() if args.user_scope else Path.cwd()
        source_context = nullcontext(link_source if args.link else payload)
        if prepare_copy and not args.link:
            source_context = prepare_copy()
        with source_context as source:
            if len(hosts) > 1 and not args.dry_run:
                # Check every destination for conflicts before changing the first.
                for host in hosts:
                    install(source, base, host, args.user_scope, True, link=args.link)
            for host in hosts:
                print(install(source, base, host, args.user_scope, args.dry_run, link=args.link))
    except (OSError, ValueError) as error:
        sys.exit(f"wsg: {error}")
