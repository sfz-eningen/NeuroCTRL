### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben, Maximilian Menzel
# Last edit:  01.12.2019
# Purpose:    This script is used to define the chronological order of the called classes and functions.
###
## COMMENT
"""
Start Main Script:
>>> import main
To get classes only:
>>> from __init__ import *
"""
## IMPORTS
from basic_libs.general import fwatcher as fw   # IMPORT Watchdog
f = fw(__file__)                                # CREATE Watchdog
from settings import Settings                   # IMPORT Settings
s = Settings()                                  # READ Settings
from __init__ import flaskAPI, AutoStream, sys  # IMPORT Classes
import time                                     # IMPORT Time module
from threading import Thread                    # IMPORT threading module 
## SCRIPT
w = flaskAPI()  # Create WEB-API Thread object
Streams = []    # Create empty list to store AutoStream objects
for Stream in s.Streams:
    # Create "communication.receive.AutoStream" object
    Streams.append(AutoStream(Stream["type"])) # Create and start data stream
    # Create "api.classes.flaskAPI" object with "c" as receive handle
    if Stream["api"] == True:                       # Only start API if stated so
        w.addR(Streams[-1], page=Stream["page"])    # Add Resource 

w.start() # Start API Thread

try:
    while 1: 
        time.sleep(0.2)
except:
    for c in Streams:
        c.stop()
    w.raiseexception()
    del Streams, w
    # EOF
    time.sleep(2)
    f.eof()
