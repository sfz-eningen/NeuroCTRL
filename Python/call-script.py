#!/bin/python
import main
import sys
import utils
from utils.draw import *
import os
import random
import time
import math
from math import *
rows, columns = os.popen('stty size', 'r').read().split()
for y in range(0, int(rows) + 1):
    for x in range(0, int(columns) + 1):
        sys.stdout.write("\x1B[37m\x1B[47m\x1B[%d;%dH%s" % (y, x, " "))
    time.sleep(0.005)
    sys.stdout.flush()
time.sleep(0.5)

from main import *
try:
    fftprint()
except:
    for y in range(0, int(rows) + 1):
        for x in range(0, int(columns) + 1):
            sys.stdout.write("\x1B[37m\x1B[40m\x1B[%d;%dH%s" % (y, x, " "))
        time.sleep(0.005)
        sys.stdout.flush()
    os.system('cls')
    exit()
