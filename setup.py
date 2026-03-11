import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages":["pygame"],
    "include_files":["asset/"]
}

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Space Shooter - Demo",
    version = "1.0",
    description = "Demo jogavel",
    options = {"build_exe": build_exe_options},
    executables = [Executable("main.py", base=base, target_name="SpaceShooter.exe")]
)