### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as this header is left intact or you credit the author.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben
# Last edit:  13.11.2019
# Purpose:    This library is used to read out OpenBCI-GUI Streams
###
"""
Auto import file for subpackage "Cyton.communication"
"""
# import importlib.util
# ibd = ""
# for x in __file__.split("\\")[:-2]:
#   ibd = f"{ibd}{x}\\"
# spec = importlib.util.spec_from_file_location("pwatcher", f"{ibd}\\basic_libs\\general.py"); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen); pwatcher = gen.pwatcher
from basic_libs import pwatcher
communication = pwatcher("Cyton.communication")
from . import *
from .receive import *
from .gData import *
communication.eof()