### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben, Maximilian Menzel
# Last edit:  03.12.2019
# Purpose:    This script is used to test the accuracy of the Random Forest Regressor
###
## CHANGE DIRECTORY TO PROJECT ROOT
from os import path, chdir
chdir(path.dirname(path.realpath(__file__)))
## IMPORTS
from basic_libs.general import fwatcher as fw   # IMPORT Watchdog
f = fw(__file__)                                # CREATE Watchdog
from settings import Settings                   # IMPORT Settings
s = Settings()                                  # READ Settings
from __init__ import flaskAPI, AutoStream, sys,\
    brainAI, dimc, AII, cleanup, \
    AIIk                                        # IMPORT Classes
import time                                     # IMPORT Time module
# CONFIGURATION AND STREAMS
# (AI)

AIIk("<CREATE AI>")
AIf = brainAI()
AIt = brainAI()
AIIk("<CREATED AI>")


AIIk("<TRAIN AI>")
try:
    AIf.train()
    AIt.train(file="./samples/samples00.csv")
except KeyboardInterrupt:
    cleanup([], f)
    sys.exit("\n\n\x1B[31;1m" + "INTERRUPTED BY USER!\x1B[0m\n")
AIIk("<TRAINED AI>")


# (STREAMS)
AIIk("<CREATE STREAMS>")
# Create empty list to store AutoStream objects
Streams = []
# Loop to start all Streams
for Stream in s.Streams:
    # Create and start data stream
    Streams.append(AutoStream(Stream["type"])) 
AIIk("<CREATED STREAMS>")
# MAIN THREAD LOOP
webAPI = flaskAPI()
webAPI.addR(Streams[0], [AIf, AIt], page="/read")
webAPI.run()
try:                    # Wait until broke by CTRL+C
    while 1:            # Do nothing for ever
        pass
except KeyboardInterrupt:
    AIIk("<\x1B[31m" + "INTERRUPTED BY USER!>")
except ValueError:
    AIIk("<\x1B[31m" + "VALUE ERROR!>")
finally:
    # Kill all Threads
    cleanup(Streams, f)
# EOF