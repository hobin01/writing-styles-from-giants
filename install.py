"""Install WSG directly from an extracted GitHub source archive."""

import shutil
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT / "src"))
from wsg import main


def source_install():
    # Assemble the same layout the wheel exposes, without a build backend.
    with tempfile.TemporaryDirectory() as scratch:
        payload = Path(scratch)
        for name in ("VERSION", "LICENSE", "THIRD_PARTY_NOTICES.md"):
            shutil.copyfile(ROOT / name, payload / name)
        shutil.copyfile(ROOT / "src/wsg/payload/SKILL.md", payload / "SKILL.md")
        shutil.copytree(ROOT / ".agents/skills/wsg/agents", payload / "agents")
        for name in ("commands", "skills"):
            shutil.copytree(ROOT / name, payload / ".catalog" / name)
        main(payload)


if __name__ == "__main__":
    source_install()
