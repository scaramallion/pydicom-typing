
import os
from pathlib import Path
import shutil
import subprocess
import sys


BASE_DIRECTORY = Path(__file__).parent.parent
SRC_DIRECTORY = BASE_DIRECTORY / "custom"
DST_DIRECTORY = BASE_DIRECTORY / "pydicom"
PYDICOM_DIRECTORY = BASE_DIRECTORY.parent / "pydicom" / "src" / "pydicom"

if __name__ == "__main__":
    # Clear out the stub files
    if DST_DIRECTORY.exists():
        shutil.rmtree(DST_DIRECTORY)

    # Generate basic stub files using mypy's `stubgen`
    print("Generating basic stub files with stubgen")
    subprocess.run(["which", "stubgen"], shell=True)
    returncode = subprocess.run(
        [
            f". {os.fspath(BASE_DIRECTORY / 'env' / 'env310' / 'bin' / 'activate')};"
            f"stubgen {os.fspath(PYDICOM_DIRECTORY)} -o .",
        ],
        shell=True,
    )

    if not list(DST_DIRECTORY.glob("*.pyi")):
        print("  Failed to generate the basic stub files")
        sys.exit()

    # Generate the custom stub files
    print("Generating custom stub files")
    if not SRC_DIRECTORY.exists():
        SRC_DIRECTORY.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [
            f". {os.fspath(BASE_DIRECTORY / 'env' / 'env310' / 'bin' / 'activate')};"
            "python scripts/generate_stubs.py",
        ],
        shell=True,
    )

    # Replace basic stub files with custom ones
    print("Replacing basic stub files with custom ones")
    for path in SRC_DIRECTORY.glob("*.pyi"):
        shutil.copyfile(path, DST_DIRECTORY / path.name)