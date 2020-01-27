### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2020
# Author:     Frederik Beimgraben, Maximilian Menzel
# Purpose:    This script is used to test the accuracy of the Random Forest Regressor
###
# Argument Parser
from argparse import ArgumentParser
parser = ArgumentParser(description="Sample Options")
parser.add_argument("file", metavar='f', type=str, nargs='+',
                    help="File to be validated")
args = parser.parse_args()
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
AIIk("<CREATED AI>")


AIIk("<TRAIN AI>")
try:
    for file in args.file[1:]:
        AIf.train(file=file)
except KeyboardInterrupt:
    cleanup([], f)
    sys.exit("\n\n\x1B[31;1m" + "INTERRUPTED BY USER!\x1B[0m\n")
except FileNotFoundError:
    sys.exit("\n\n\x1B[31;1m" + "FILE NOT FOUND!\x1B[0m\n")
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
AIIk("<READER LOOP>")
try:                    # Wait until broke by CTRL+C
    while 1:            # Do nothing for ever
        m = []
        for e in Streams[0].read():
            # Read and convert data
            m.append(dimc(e))
        # AI-Analyze data
        anaf = AIf.analyze(m)
        #anat = AIt.analyze(m)
        for x in anat:
            # Print Result
            sys.stdout.write("\n" + str(x).ljust(4, "0"))
except KeyboardInterrupt:
    AIIk("<\x1B[31m" + "INTERRUPTED BY USER!>")
except ValueError:
    AIIk("<\x1B[31m" + "VALUE ERROR!>")
# finally:
#     # Kill all Threads
#     cleanup(Streams, f)
# EOF