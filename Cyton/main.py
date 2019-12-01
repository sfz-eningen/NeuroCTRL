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
from __init__ import flaskAPI, AutoStream, sys,\
    brainAI, dimc                               # IMPORT Classes
import time                                     # IMPORT Time module
from threading import Thread                    # IMPORT threading module 
## SCRIPT
AI = brainAI()
AI.train()

Streams = []    # Create empty list to store AutoStream objects
for Stream in s.Streams:
    # Create "communication.receive.AutoStream" object
    Streams.append(AutoStream(Stream["type"])) # Create and start data stream

try:                    # Wait until broke by CTRL+C
    while 1:            # Do nothing for ever
        m = []
        for e in Streams[0].read():
            m.append(dimc(e))
        print(AI.analyze(m))
except:
    for c in Streams:   # Stop Streams on exit
        c.stop()
    # EOF
    time.sleep(2)
    f.eof()             # Stop Watchdog
