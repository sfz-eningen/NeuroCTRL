# from . import *
# WATCHDOG
import importlib.util
ibd = ""
for x in __file__.split("\\")[:-1]:
  ibd = f"{ibd}{x}\\"
spec = importlib.util.spec_from_file_location("pwatcher", f"{ibd}basic_libs\\general.py"); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen); pwatcher = gen.pwatcher
Cyton = pwatcher("Cyton", typ="package")
# IMPORTS
try:
  from .basic_libs import *
  from .basic_libs.general import *
  from .config import *
  from .communication import AutoStream, bprepr
  from .aiprep import AIStream
  from .samples import *
  from .cli import *
  # from .api import *
except:
  from basic_libs import *
  from basic_libs.general import *
  from config import *
  from communication import AutoStream, bprepr
  from aiprep import AIStream
  from samples import *
  from cli import *
  # from api import *
import sys
conf = Config()
Cyton.eof()