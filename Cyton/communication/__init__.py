"""
Auto import file for subpackage "Cyton.communication"
"""
import importlib.util
ibd = ""
for x in __file__.split("\\")[:-2]:
  ibd = f"{ibd}{x}\\"
spec = importlib.util.spec_from_file_location("pwatcher", f"{ibd}\\basic_libs\\general.py"); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen); pwatcher = gen.pwatcher

communication = pwatcher("Cyton.communication")
import pyximport; pyximport.install()
from . import *
from .receive import *
from .gData import *
communication.eof()