#!/bin/python
# Imports
import numpy as np
import math
from math import *
import utils
from utils import draw
from utils.draw import *
import sys
import time
from time import *
import socket
import os
import termios
import tty
UDP_IP = "127.0.0.1"
UDP_PORT_BND = 56572
sock_bnd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_bnd.bind((UDP_IP, UDP_PORT_BND))
bnd, addr2 = sock_bnd.recvfrom(1024)
# Functions
rows, columns = os.popen('stty size', 'r').read().split()
def avg(x):
    ma = []
    for a in range (0, len(x) - 1):
        ma.append(float(x[a]))
    return float(sum(ma))/float(len(ma))
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_grid():
    print_co(int(int(columns)/2) - 7, int(int(rows)/2), "Press 'g', when ready!")
    if(getch() == 'g'):
        smst = []
        for v in range(0, 10):
            bnd, addr = sock_bnd.recvfrom(1024)
            band0 = []
            band1 = []
            band2 = []
            band3 = []
            band  = []
            bands = str(bnd)[31:-8].split(']')
            band0s = bands[0].split(',')
            band1s = bands[1][2:-1].split(',')
            band2s = bands[2][2:-1].split(',')
            band3s = bands[3][2:-1].split(',')
            for x in range(0, 5):
                band0.append(float(band0s[x]))
                band1.append(float(band1s[x]))
                band2.append(float(band2s[x]))
                band3.append(float(band3s[x]))
            deltab = [band0[0], band1[0], band2[0], band3[0]]
            thetab = [band0[1], band1[1], band2[1], band3[1]]
            alphab = [band0[2], band1[2], band2[2], band3[2]]
            betab  = [band0[3], band1[3], band2[3], band3[3]]
            gammab = [band0[4], band1[4], band2[4], band3[4]]
            deltav = avg(deltab)
            thetav = avg(thetab)
            alphav = avg(alphab)
            betav  = avg(betab)
            gammav = avg(gammab)

            band.append(band0)
            band.append(band1)
            band.append(band2)
            band.append(band3)
            bandavg = [deltav, thetav, alphav, betav, gammav]
            smst.append(bandavg)
        smsa = []
        for x in range(0, 5):
            smsa.append(avg(smst[x]))
    return [smsa, smst]
def callAll():
    rows, columns = os.popen('stty size', 'r').read().split()
    for y in range(0, int(rows) + 1):
        for x in range(0, int(columns) + 1):
            sys.stdout.write("\x1B[37m\x1B[40m\x1B[%d;%dH%s" % (y, x, " "))
        sleep(0.005)
        sys.stdout.flush()
    mat = get_grid()
    smsa = mat[0]
    smst = mat[1]
    for y in range(0, int(rows) + 1):
        for x in range(0, int(columns) + 1):
            sys.stdout.write("\x1B[37m\x1B[40m\x1B[%d;%dH%s" % (y, x, " "))
        sleep(0.005)
        sys.stdout.flush()
    print_co(int(int(columns)/2), int(int(rows)/2), "SMSA: %s" % (str(smsa)))
