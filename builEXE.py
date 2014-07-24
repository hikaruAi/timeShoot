import os
script="""import sys

from cx_Freeze import setup, Executable
includes = ["re","atexit"]
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
        name = "timeShoot",
        version = "1.04",
        description = "Minimalist time lapse Recorder by Hikaru Ai",
        options = {"build_exe" : {"includes" : includes }},
        executables = [Executable("timeShoot.pyw", base = base,icon="ico.ico")])"""

file=open("temp.py","wt")
file.write(script)
file.close()
os.system("python temp.py build")
os.remove("temp.py")
input("\nHECHO")