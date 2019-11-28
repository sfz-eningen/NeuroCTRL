### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben
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
    sys.stdout.write(f"[\n\x1B[34;1m{Stream['type']}, {Stream['api']}\x1B[0m]\n")
    # Create "communication.receive.AutoStream" object
    c = AutoStream(Stream["type"]) # Create and start data stream
    # Create "api.classes.flaskAPI" object with "c" as receive handle
    if Stream["api"] == True:
        w.addR(c, page=Stream["page"]) # Add Resource 
    Streams.append(c)

w.start() # Start API Thread

try:
    while 1: 
        time.sleep(0.2)
except:
    print(Streams)
    for c in Streams:
        c.stop()
        print(c)
    w.raiseexception()
    del Streams, w
    # EOF
    time.sleep(2)
    f.eof()
