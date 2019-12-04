from os import walk, getcwd, path, system, remove
from sys import argv
import sys
system("pip install -r requirements.txt")

f = []
d = []
for (dirpath, dirnames, filenames) in walk("./"):
  f.extend(filenames)
  d.extend(dirnames)
  break
fst = ""
for file in f:
  fst += f' --add-data "{path.abspath(file)}";"." '
dst = ""
for dirn in d:
  if not dirn in ["OpenBCI_GUI", "__pycache__", "build", "dist", "output", ".git"]:
    dst += f' --add-data "{path.abspath(dirn)}";"{dirn}/" '
command = f'{path.split(sys.executable)[0]}\Scripts\pyinstaller --add-data "{sys.path[-1]}\scipy\sparse\linalg\isolve\_iterative.cp37-win32.pyd";"site-packages\scipy\sparse\linalg\isolve" -i {path.abspath("build-files/icon.ico")} -y -F {fst} {dst} {argv[1]}'
print(f"{getcwd()}>", command)
system(command)
from shutil import copyfile
try:
  remove(f'{argv[1].replace(".py", "")}.exe')
except:
  pass
copyfile(f'./dist/{argv[1].replace(".py", ".exe")}', f'{getcwd()}\\{argv[1].replace(".py", ".exe")}')