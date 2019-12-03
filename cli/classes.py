### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as you credit the author by keeping this header intact.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben
# Last edit:  13.11.2019
# Purpose:    This script is used to display collected EEG-Data.
###
# IMPORTS
import os
import time
from mam import waclean, SectionBanner, inp
from __init__ import AutoStream, SWriter, bprepr, sys
# SCRIPT
st = []
class ncCLI():
    st = []
    def __init__(self, name):
        """
        ## Command Line Interface.
        ### Usage (Python 3.x.x):
        ```
        \t c = ncCLI()
        \t c.start() # Start CLI UI
        ```
        """
        self.name = name
        return None

    def UI(self):
        s1 = AutoStream("band")
        # ini()
        w = SWriter(self.name)
        while 1:
                for e in [s1.read()]:
                    self.st.append(e)
                    for x in e:
                        # waclean()
                        print("\x1B[7;2H")
                        bprepr(x)
                        w.write(x["data"])
                        # time.sleep(.9)
        try:
            while 1:
                for e in [s1.read()]:
                    self.st.append(e)
                    for x in e:
                        # waclean()
                        print("\x1B[7;2H")
                        bprepr(x)
                        w.write(x["data"])
                        # time.sleep(.9)
        finally:
            sys.stdout.write("\x1B[8;2H")
            waclean()
            s1.stop()
            time.sleep(0.2)

    def start(self):
        os.system("cls")
        SectionBanner("IMPORT")
        sys.stdout.write("\x1B[6;2H")
        SectionBanner("DISPLAY")
        self.UI()
        try:
            os.system("cls")
            SectionBanner("IMPORT")
            sys.stdout.write("\x1B[6;2H")
            SectionBanner("DISPLAY")
            self.UI()
        except:
            pass
        if inp() in ["RES", "res", "1", "r", "resume", "Resume", "RESUME"]:
            print("\x1B[0m")
        else:
            print("\x1B[0m")
            return None