#!/bin/python
# import
import serial
import socket
import time
from time import *
import sys
import os
#import tensorflow as tf
#from tensorflow import keras
import numpy as np
import sys
import termios
import tty
#import cv2
import keyboard
import utils
from utils import *
from utils.windows import *
import random
from random import *
import math
from math import *
import string
# ---
rows_s, columns_s = os.popen('stty size', 'r').read().split()
rows = int(rows_s)
columns = int(columns_s)
middlex = int(columns/2)
middley = int(rows/2)

for y in range(0, int(rows) + 1):
    for x in range(0, int(columns) + 1):
        sys.stdout.write("\x1B[37m\x1B[40m\x1B[%d;%dH%s" % (y, x, " "))
    sleep(0.005)
    sys.stdout.flush()
xp = 0
while True:
    for x in range(0, columns):
        if(-1*sin(x/8 - xp) - -1*sin(x/8 + xp) < 0):
            chr = "▞"
        if (-1*sin(x/8 - xp) - -1*sin(x/8 + xp) > 0):
            chr = "▚"
        if ((int((-1*sin(x/8 - xp) - -1*sin(x/8 + xp))*10) == 0) and ((cos(x/8 - xp) - cos(x/8 + xp)) < 0)):
            chr = "▀"
        if ((int((-1*sin(x/8 - xp) - -1*sin(x/8 + xp))*10) == 0) and ((cos(x/8 - xp) - cos(x/8 + xp)) > 0)):
            chr = "▄"
        if ((int((-1*sin(x/8 - xp) - -1*sin(x/8 + xp))*10) == 0) and ((cos(x/8 - xp) - cos(x/8 + xp)) == 0)):
            chr = "█"

        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 4, 0,rows/4*3 + 5 + int((cos(x/8 - xp)*4) - (cos(x/8 + xp)*4)), int(x), chr))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + 5 + 1 + int((cos(x/8 - xp)*4) - (cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + 5 + 2 + int((cos(x/8 - xp)*4) - (cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + 5 + 3 + int((cos(x/8 - xp)*4) - (cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + 5 - 1 + int((cos(x/8 - xp)*4) - (cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + 5 - 2 + int((cos(x/8 - xp)*4) - (cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + 5 - 3 + int((cos(x/8 - xp)*4) - (cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 2, 0,rows/4*3 + - 15 - 7 + int((cos(x/8 - xp)*4)), int(x),  "+"))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 6 + int((cos(x/8 - xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 5 + int((cos(x/8 - xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 4 + int((cos(x/8 - xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 8 + int((cos(x/8 - xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 9 + int((cos(x/8 - xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 10 + int((cos(x/8 - xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 2, 0,rows/4*3 + - 15  - 25 - int((cos(x/8 + xp)*4)), int(x), "+"))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 24 - int((cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 23 - int((cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 22 - int((cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 26 - int((cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 27 - int((cos(x/8 + xp)*4)), int(x), " "))
        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,rows/4*3 + - 15  - 28 - int((cos(x/8 + xp)*4)), int(x), " "))
        sleep(0.0001)
        sys.stdout.flush()

        sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (1, 0, 0,randint(0, 10), int(x), " "))
    xp = xp + 0.06125/2
while True:
    y = randint(0, rows)
    x = randint(0, columns)
    sys.stdout.write("\x1B[%dm\x1B[3%dm\x1B[4%dm\x1B[%d;%dH%s" % (choice([0, 1, 2, 3, 4, 5, 8]), choice([0, 1, 2, 3, 4, 5, 5, 5, 6]), choice([0, 1, 2, 3, 4, 5, 5, 5, 6]), int(y), int(x), "▀"))
    sys.stdout.flush()
sleep(2)
rp = [20, int(rows)/2 + 10]
rpt = [int(columns)/2 - 20, int(rows)/2]
rp2 = [179/4 - 6,20]
asbt = [0, 0, 0, 0]
pcco = print_co
def drawAll():

    pcco(rp2[0] + 1, rp2[1] - 4, "\x1B[37mKanal 1 (GELB)".rjust(26) + "\x1B[37mKanal 2 (ORANGE)".rjust(31) + "\x1B[37mKanal 3 (ROT)".rjust(31) + "\x1B[37mKanal 4 (BRAUN)".rjust(31))
    tfft = [30, 4]
    drawCase([stfft[0] - 2, stfft[1] + 2], [126, 3])
    tm(rpt)
    cd(rp)
    drawCase([38, 15], [107, 5])
    drawCase([70, int(int(rows)/2 + 9)], [40, 10])
    drawCase([69, int(int(rows)/2 + 8)], [42, 12])

    pcco(73, int(int(rows)/2 + 10), "Focus:")
    pcco(73, int(int(rows)/2 + 12), "OpenBCI-GUI: ")
    pcco(73, int(int(rows)/2 + 14), "Int. Algorithm: ")
    pcco(73, int(int(rows)/2 + 16), "ALPHA: ")
    pcco(73, int(int(rows)/2 + 17), "BETA:  ")
    w1()
    sleep(3)
