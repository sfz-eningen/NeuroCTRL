### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben, Maximilian Menzel
# Last edit:  01.12.2019
# Purpose:    This script is used to define the chronological order of the called classes and functions.
###
## COMMENT
from os import system, path, chdir
chdir(path.dirname(path.realpath(__file__)))

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
    brainAI, dimc, TestStreamer, AII, cleanup, \
    AIIk                                        # IMPORT Classes
from numpy import round as nround
import time                                     # IMPORT Time module
from threading import Thread                    # IMPORT threading module 
## SCRIPT
AIIk("<CREATE AI>")
states = ["Idle", "Focused", "Up", "Down", "Left", "Right"]
AI = brainAI()
AIIk("<CREATED AI>")
AIIk("<TRAIN AI>")
try:
    AI.train()
except KeyboardInterrupt:
    cleanup([], f)
    sys.exit("\n\n\x1B[31;1m" + "INTERRUPTED BY USER!\x1B[0m\n")
AIIk("<TRAINED AI>")
time.sleep(1)
AIIk("<CREATE STREAMS>")
Streams = []    # Create empty list to store AutoStream objects
for Stream in s.Streams:
    # Create "communication.receive.AutoStream" object
    Streams.append(AutoStream(Stream["type"])) # Create and start data stream
AIIk("<CREATED STREAMS>")

time.sleep(1)

AIIk("<READER LOOP>")
try:                    # Wait until broke by CTRL+C
    while 1:            # Do nothing for ever
        m = []
        for e in Streams[0].read():
            m.append(dimc(e))
        ana = AI.analyze(m)
        for x in ana:
            sys.stdout.write("\n" + str(x) + "  " + str(states[int(x+0.5)]))
except KeyboardInterrupt:
    AII("\x1B[31m" + "INTERRUPTED BY USER!")
except ValueError:
    AII("\x1B[31m" + "VALUE ERROR!")
finally:
    cleanup(Streams, f)