### INFO AND LICENSING ###
# This code is licensed under the GNU GPL V3.
# You may use this script or it´s contents as long as this header is left intact or you credit the author.
#             © NeuroCTRL 2019
# Author:     Frederik Beimgraben
# Last edit:  13.11.2019
# Purpose:    This script is used to display collected EEG-Data
###
# IMPORTS
from mam import *
import os
import time

# SCRIPT
def UI():
  s1 = AutoStream("band")
  # ini()
  try:
    while 1:
      for e in [s1.read()]:
        for x in e:
          # waclean()
          print("\x1B[7;2H")
          bprepr(x)
          # time.sleep(.9)
  finally:
    sys.stdout.write("\x1B[8;2H")
    waclean()
    s1.stop()
    time.sleep(0.2)
while 1:
  try:
    os.system("cls")
    SectionBanner("IMPORT")
    from __init__ import *
    sys.stdout.write("\x1B[6;2H")
    SectionBanner("DISPLAY")
    UI()
  except:
    pass
  if inp() in ["RES", "res", "1", "r", "resume", "Resume", "RESUME"]:
    print("\x1B[0m")
    pass
    
  else:
    print("\x1B[0m")
    break