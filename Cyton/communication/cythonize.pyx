from distutils.core import setup
from Cython.Build import cythonize
from shutil import copyfile
from os import listdir
from os.path import isfile, join

files = [f for f in listdir(".\\") if isfile(join(".\\", f))]
print(files)
for f in files:
  if f[-3:] == ".py":
    copyfile(f, f"{f}x")
    setup(
        ext_modules = cythonize(f"{f}x")
    )