# import importlib.util
# ibd = ""
# # for x in __file__.split("\\")[:-2]:
# #   ibd = f"{ibd}{x}\\"
# # spec = importlib.util.spec_from_file_location("pwatcher", f"{ibd}\\basic_libs\\general.py"); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen); pwatcher = gen.pwatcher
from basic_libs import pwatcher
samples = pwatcher("Cyton.samples")

# IMPORTS
from .save import *
from .load import *

samples.eof()