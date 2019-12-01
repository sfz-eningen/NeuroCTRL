### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2019
git # Author:     Frederik Beimgraben, Maximilian Menzel
# Last edit:  13.11.2019
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
from basic_libs.general import fwatcher as fw
f = fw(__file__)
from settings import Settings
s = Settings()
from __init__ import flaskAPI, AutoStream, sys
import time
from threading import Thread
## SCRIPT
w = flaskAPI() # Create WEB-API Thread object
Streams = []
for Stream in s.Streams:
    # Create "communication.receive.AutoStream" object
    Streams.append(AutoStream(Stream["type"])) # Create and start data stream
    # Create "api.classes.flaskAPI" object with "c" as receive handle
    if Stream["api"] == True:
        w.addR(Streams[-1], page=Stream["page"]) # Add Resource 

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
