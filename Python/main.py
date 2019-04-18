#!/bin/python
# __________________________________________________________________________________________
#|  Streaming Application for streaming of Data from OpenBCI Ganglion to Google Tensorflow  |
#|__________________________________________________________________________________________|
# import
import serial
import socket
import time
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
# ---
# DEFINE
# DEFS
dv = ""
stfft = []
ptb = [[], [], [], []]
chm = []
tmm = time.time()
def print_there(text):

    sys.stdout.write("\x1B[0;0H" + str(text))
    sys.stdout.flush()
def print_tp1(text):
    sys.stdout.write("\x1B[%d;0H%s" % (int(rows) - 5, text))
    sys.stdout.flush()
def print_tp2(text):
    sys.stdout.write("\x1B[%d;0H%s" % (int(rows) - 7, text))
    sys.stdout.flush()
def pcco(x, y, text):
    sys.stdout.write("\x1B[%d;%dH%s" % (y, x, text))

    sys.stdout.flush()
def linex(x1, x2, y, ansi):
    for x in range(x1, x2):
        sys.stdout.write("%s\x1B[%d;%dH━\x1B[44m\x1B[36m" % (ansi, y, x))
    sys.stdout.flush()
def cornur(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┓"))
    sys.stdout.flush()
def cornul(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┏"))
    sys.stdout.flush()
def cornlr(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┛"))
    sys.stdout.flush()
def cornll(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┗"))
    sys.stdout.flush()
def liney(y1, y2, x, ansi):
    for y in range(y1, y2):
        sys.stdout.write("%s\x1B[%d;%dH┃\x1B[44m\x1B[36m" % (ansi, y, x))
    sys.stdout.flush()
def linecly(y1, y2, x):
    for y in range(y1, y2):
        sys.stdout.write("%s\x1B[%d;%dH \x1B[44m\x1B[36m" % ("\x1B[44m\x1B[34m", y, x))
    sys.stdout.flush()
def lineclx(x1, x2, y):
    for x in range(x1, x2):
        sys.stdout.write("%s\x1B[%d;%dH \x1B[44m\x1B[36m" % ("\x1B[44m\x1B[34m", y, x))
    sys.stdout.flush()
def reader(fl, iz):
    sm = str(fl.read()[0:-2]).split('|')
    si = []
    for x in range(0, len(sm)):
        ptb[iz].append(sm[x].replace('\U00002013', '-'))
        si.append(float(sm[x].replace('\U00002013', '-')))
    return si

def inkey():
    fd=sys.stdin.fileno()
    remember_attributes=termios.tcgetattr(fd)
    tty.setraw(sys.stdin.fileno())
    character=sys.stdin.read(inkey_buffer)
    termios.tcsetattr(fd,termios.TCSADRAIN, remember_attributes)
    return character
def linew():
    sfil = "\x1B[34m\x1B[44m"
    for x in range(0, 4*22+14):
        sfil = sfil + "#"
    sfil = sfil + "\x1B[0m"
    print(sfil)
def linewp():
    sfil = "\x1B[34m\x1B[44m"
    for x in range(0, 4*22+21):
        sfil = sfil + "#"
    sfil = sfil + "\x1B[0m"
    print(sfil)
# \DEFINE\
inkey_buffer = 1
# OPEN
mi0 = open("./files/smpi.opt.0.dat","r")
mi1 = open("./files/smpi.opt.1.dat","r")
mi2 = open("./files/smpi.opt.2.dat","r")
mi3 = open("./files/smpi.opt.3.dat","r")
# SAMPLE
smpi = [reader(mi0, 0), reader(mi1, 1), reader(mi2, 2), reader(mi3, 3)]
smp0 = [sum(smpi[0])/len(smpi[0]), sum(smpi[1])/len(smpi[1]), sum(smpi[2])/len(smpi[2]), sum(smpi[3])/len(smpi[3])]
smp1 = [0, 0, 0, 0]
# prtb
blue = "\x1B[35m"
yellow = "\x1B[33m"
yellow2 = "\x1B[33m\x1B[44m"
red = "\x1B[31m"
red2 = "\x1B[31m\x1B[44m"
hbl = "\x1B[36m"
hbl2 = "\x1B[36m\x1B[44m"
norm = "\x1B[0m"
bb = "\x1B[37m\x1B[44m"
wlin = "\x1B[34m\x1B[44m##\x1B[0m "
wlin1 = "\x1B[34m\x1B[44m##\x1B[36m "
w2 = "\x1B[34m\x1B[44m#\x1B[0m"
w3 = " \x1B[34m\x1B[44m#\x1B[0m "
fill = "\x1B[34m\x1B[44m##\x1B[0m"
col_width = 22
#print(wlin1 + str("Channel 1 (μVrms)").ljust(col_width) + wlin1 + str("Channel 2 (μVrms)").ljust(col_width) + wlin1 + str("Channel 3 (μVrms)").ljust(col_width) + wlin1 + str("Channel 4 (μVrms)").ljust(col_width) + wlin)
#for x in range(0, len(ptb[0])):
#    print(wlin + blue + str(ptb[0][x]).ljust(col_width) + wlin + yellow + str(ptb[1][x]).ljust(col_width) + wlin  + blue + str(ptb[2][x]).ljust(col_width) + wlin  + yellow + str(ptb[3][x]).ljust(col_width) + norm + fill)
#linew()
# \SAMPLE\
# import matplotlib.pyplot as plt
# print(tf.__version__)
# ---
sti = time.time()
sleep = time.sleep
# \import\

UDP_IP = "127.0.0.1"
UDP_PORT_TSS = 56571
UDP_PORT_BND = 56572
UDP_PORT_FFT = 56573
sock_tss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_bnd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_fft = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_tss.bind((UDP_IP, UDP_PORT_TSS))
sock_bnd.bind((UDP_IP, UDP_PORT_BND))
sock_fft.bind((UDP_IP, UDP_PORT_FFT))
ts, addr = sock_tss.recvfrom(1024) # buffer size is 1024 bytes
bnd, addr2 = sock_bnd.recvfrom(1024)
#focus = str(foc)[25:-7]
foma = []
rows, columns = os.popen('stty size', 'r').read().split()
sfilf = "\x1B[34m\x1B[44m"
for x in range(1, int(columns) + 1):
    sfilf = sfilf + "#"
sfilf = sfilf + "\x1B[0m"
def sff():
    print(sfilf)
# \DEFS\
# MAIN

# \MAIN\
# Functions
def tm(rp):
    pcco(rp[0], rp[1] - 1, "\x1B[30m\x1B[40m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\x1B[36m\x1B[44m")
    pcco(rp[0], rp[1]    , "\x1B[30m\x1B[40m┃\x1B[37m     OpenBCI Readout Server v1.0.0      \x1B[30m┃\x1B[36m\x1B[44m")
    pcco(rp[0], rp[1] + 1, "\x1B[30m\x1B[40m┃\x1B[37m       © Frederik Beimgraben 2019       \x1B[30m┃\x1B[36m\x1B[44m")
    pcco(rp[0], rp[1] + 2, "\x1B[30m\x1B[40m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\x1B[36m\x1B[44m")
def cd(rp):
    rx = rp[0]
    ry = int(rp[1])
    dv = "\x1B[37m\x1B[44m\x1B[1m\x1B[2m"
    pcco(rp[0], rp[1]    , "   Current Device:                       ")
    pcco(rp[0], rp[1] + 1, "                                         ")
    pcco(rp[0], rp[1] + 2, "   4 CH OpenBCI Ganglion                 ")
    pcco(rp[0], rp[1] + 3, "                                         ")
    pcco(rp[0], rp[1] + 4, "   UDP Datastream from OpenBCI-GUI:      ")
    pcco(rp[0], rp[1] + 5, " \x1B[35m" + str("   ⊳ \x1B[33m" + UDP_IP + "\x1B[37m:\x1B[32m" + str(UDP_PORT_TSS) + "\x1B[37m" + "  Time Series".ljust(13) + "\x1B[31m" + "4CH".rjust(6)).ljust(40) + "\x1B[36m\x1B[44m ")
    pcco(rp[0], rp[1] + 6, " \x1B[35m" + str("   ⊳ \x1B[33m" + UDP_IP + "\x1B[37m:\x1B[32m" + str(UDP_PORT_BND) + "\x1B[37m" + "  Band".ljust(13) + "\x1B[31m" + "1CH".rjust(6)).ljust(40) + "\x1B[36m\x1B[44m ")
    pcco(rp[0], rp[1] + 7, " \x1B[35m" + str("   ⊳ \x1B[33m" + UDP_IP + "\x1B[37m:\x1B[32m" + str(UDP_PORT_FFT) + "\x1B[37m" + "  FFT".ljust(13) + "\x1B[31m" + "125CH".rjust(6)).ljust(40) + "\x1B[36m\x1B[44m ")
    linex(rx + 1, rx + 42,  ry - 1, dv)
    liney(ry, ry + 9, rx, dv)
    linex(rx + 1, rx + 42,  ry + 9, dv)
    liney(ry, ry + 9, rx + 42, dv)
    cornur(rx + 42, ry - 1, dv)
    cornul(rx, ry-1, dv)
    cornll(rx, ry+9, dv)
    cornlr(rx + 42, ry + 9, dv)
    pcco(int(columns), int(rows), " ")
def fftd(stx, sty, dv):
    drawCase([stx, sty - 1], [122, 3])

def drawCase(stm, sm):
    w = sm[0]
    h = sm[1]
    stx = stm[0]
    sty = stm[1]
    ds = "\x1B[37m\x1B[44m\x1B[1m\x1B[2m"
    cornul(stx,         sty,  ds)
    cornll(stx,     sty + h,  ds)
    cornur(stx + w,     sty,  ds)
    cornlr(stx + w, sty + h,  ds)
    linex(stx + 1, stx + w, sty, ds)
    linex(stx + 1, stx + w, sty + h, ds)
    liney(sty + 1, sty + h, stx, ds)
    liney(sty + 1, sty + h, stx + w, ds)
    lineclx(stx, stx + w + 1, sty - 1)
def drawCaseEff(stm, sm, ds):
    w = sm[0]
    h = sm[1]
    stx = stm[0]
    sty = stm[1]
    cornul(stx,         sty,  ds)
    cornll(stx,     sty + h,  ds)
    cornur(stx + w,     sty,  ds)
    cornlr(stx + w, sty + h,  ds)
    linex(stx + 1, stx + w, sty, ds)
    linex(stx + 1, stx + w, sty + h, ds)
    liney(sty + 1, sty + h, stx, ds)
    liney(sty + 1, sty + h, stx + w, ds)
    #lineclx(stx, stx + w + 1, sty - 1)
    #lineclx(stx, stx + w + 1, sty - 2)

def dCrD(stm, sm):
    drawCase(stm, [sm[0]*2, sm[1]])

def ffc(invar, inma):
    return str(round(float(str(inma[invar]))*1000)/1000).rjust(7)
rp = [20, int(rows)/2 + 10]
rpt = [int(columns)/2 - 20, int(rows)/2]
rp2 = [179/4 - 6,20]
asbt = [0, 0, 0, 0]

def fftprint():
    ffto, addr3 = sock_fft.recvfrom(8192) # buffer size is 1024 bytes
    fch0 = str(str(ffto).split(']')[0])[25:-1].split(',')
    fch1 = str(str(ffto).split(']')[1])[2:-1].split(',')
    fch2 = str(str(ffto).split(']')[2])[2:-1].split(',')
    fch3 = str(str(ffto).split(']')[3])[2:-1].split(',')
    avgfft = []
    for x in range(0, 124):
        avgfft.append(((float(fch0[x]) + float(fch1[x]) + float(fch2[x]) + float(fch3[x]))/4))
    # print(str(fch0) + str(len(fch0)))
    # print(str(fch1) + str(len(fch1)))
    # print(str(fch2) + str(len(fch2)))
    # print(str(fch3) + str(len(fch3)))

    fftt = str(ffto)[25:-8].split(',')
    ffft = [[], [], [], []]
    for x in range(1, len(fch0)):
        ffft[0].append(fch0)
        ffft[1].append(fch1)
        ffft[2].append(fch2)
        ffft[3].append(fch3)
    # sff()
    schr=12
    # print(wlin + str("Signals:" + str(len(fftt))).ljust(int(columns) - 5) + "\x1B[44m  \x1B[0m")
    # sff()
    strln = str(str("\x1B[44m\x1B[34m" + "#".ljust(4) + "\x1B[37mFreq.\x1B[34m" + "#".ljust(2) + "\x1B[37m" + "1 Hz".rjust(8) + "  " + str(str(schr) + " Hz").rjust(8)  + "  " + str(str(schr*2) + " Hz").rjust(8)  + "  " + str(str(schr*3) + " Hz").rjust(8)  + "  " + str(str(schr*4) + " Hz").rjust(8) + "  " + str(str(schr*5) + " Hz").rjust(8) + "  " + str(str(schr*6) + " Hz").rjust(8) + "  " + str(str(schr*7) + " Hz").rjust(8) + "  " + str(str(schr*8) + " Hz").rjust(8)  + "  " + str(str(schr*9) + " Hz").rjust(8) + "  " + str(str(schr*10) + " Hz").rjust(8) + "\x1B[44m\x1B[34m##"))
    # print(str(str("\x1B[44m\x1B[34m" + "#".ljust(11) + "\x1B[37m" + "1 Hz".rjust(8) + "  " + str(str(schr) + " Hz").rjust(8)  + "  " + str(str(schr*2) + " Hz").rjust(8)  + "  " + str(str(schr*3) + " Hz").rjust(8)  + "  " + str(str(schr*4) + " Hz").rjust(8) + "  " + str(str(schr*5) + " Hz").rjust(8) + "  " + str(str(schr*6) + " Hz").rjust(8) + "  " + str(str(schr*7) + " Hz").rjust(8) + "  " + str(str(schr*8) + " Hz").rjust(8)  + "  " + str(str(schr*9) + " Hz").rjust(8) + "  " + str(str(schr*10) + " Hz").rjust(8) + "\x1B[44m\x1B[34m##")).ljust(int(columns ) + 25))
    sgnstr = str(w2 + w2 + w2 + w2 + bb + "FFTs" + "\x1B[44m\x1B[34m###\x1B[0m " + str(ffc(0, avgfft)) + w3 +  str(ffc(1*schr - 1, avgfft)) + w3 +   str(ffc(2*schr - 1, avgfft)) + w3 + str(ffc(3*schr - 1, avgfft)) + w3 + str(ffc(4*schr - 1, avgfft)) + w3 + str(ffc(5*schr - 1, avgfft)) + w3 + str(ffc(6*schr - 1, avgfft))  + w3 + str(ffc(7*schr - 1, avgfft))  + w3 + str(ffc(8*schr - 1, avgfft))  + w3 + str(ffc(9*schr - 1, avgfft)) + w3 + str(ffc(10*schr - 1, avgfft)) + " \x1B[0m")
    # print(sgnstr.ljust(int(columns) + 1))
    bll=0
    #for y in range(0, int(rows)):
    #    for x in range(0, int(columns)):
    #        pcco(x+1, y+1, "\x1B[2m\x1B[47m ")
    #        sleep(0.000001)
    for y in range(3, int(rows) - 2):
        for x in range(7, int(columns) - 3):
            pcco(x+1, y+1, "\x1B[2m\x1B[40m\x1B[37m░")
        sleep(0.010)
    pcco(int(columns), int(rows), "\x1B[0m\x1B[36m\x1B[44m")
    for y in range(2, int(rows) - 3):
        for x in range(4, int(columns) - 5):
            pcco(x+1, y+1, "\x1B[44m ")
        sleep(0.010)
    pcco(5, 3, "\x1B[44;37m⎍⎍ ▎ OpenBCI Readout Server ")
    for x in range(5, int(columns) - 4):
        pcco(x, 4, "\x1B[44;37m▔")
        pcco(x, 2, "\x1B[47;37m▁")
    dig = [" ", "①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨"]
    txt = "❐ 4 ▍⏦ 200Hz ▍⏱ Uptime (s) =           ▍❖ Device = ⯃ Ganglion"
    pcco(int(columns) - 5 - len(txt), 3, "\x1B[44;37m" + txt + "\x1B[37m▕")
    dv = "\x1B[37m\x1B[44m\x1B[1m\x1B[2m"
    stfft = [30, 3]
    drawAll()
    pcco(int(columns), int(rows), "\x1B[47m ")
    wtf = 0
    focs = ""
    asbt = [0, 0, 0, 0]

    while True:
        # DATA WORK #
        ts, addr = sock_tss.recvfrom(1024) # buffer size is 1024 bytes
        bnd, addr = sock_bnd.recvfrom(1024)
        formf = ts[22:-4]
        ch = str(formf).split(',')
        cu = [time.time(), float(ch[0][2:-4].replace("E-", "")), float(ch[1][0:-1].replace("E-", "")), float(ch[2][0:-1].replace("E-", "")), float(ch[3][0:-2].replace("E-", ""))]
        ffto, addr3 = sock_fft.recvfrom(8192) # buffer size is 1024 bytes
        fch0 = str(str(ffto).split(']')[0])[25:-1].split(',')
        fch1 = str(str(ffto).split(']')[1])[2:-1].split(',')
        fch2 = str(str(ffto).split(']')[2])[2:-1].split(',')
        fch3 = str(str(ffto).split(']')[3])[2:-1].split(',')
        avgfft = []
        for x in range(0, 124):
            avgfft.append(((float(fch0[x]) + float(fch1[x]) + float(fch2[x]) + float(fch3[x]))/4))
        fftt = str(ffto)[25:-8].split(',')
        ffft = [[], [], [], []]
        for x in range(1, len(fch0)):
            ffft[0].append(float(fch0[x-1]))
            ffft[1].append(float(fch1[x-1]))
            ffft[2].append(float(fch2[x-1]))
            ffft[3].append(float(fch3[x-1]))
        # FOCUS #

        inc4 = [[], [], [], []]
        # ALPHA #
        alpha = [[0], [0], [0], [0]]
        lca = inc4
        hca = inc4
        freq = [7, 11]
        bcga = inc4
        asb = inc4
        asa = 0
        alpha[0] = avg(ffft[0][freq[0]:freq[1]])
        alpha[1] = avg(ffft[1][freq[0]:freq[1]])
        alpha[2] = avg(ffft[2][freq[0]:freq[1]])
        alpha[3] = avg(ffft[3][freq[0]:freq[1]])
        lca[0] = avg(ffft[0][freq[0] - 2:freq[0]])
        lca[1] = avg(ffft[1][freq[0] - 2:freq[0]])
        lca[2] = avg(ffft[2][freq[0] - 2:freq[0]])
        lca[3] = avg(ffft[3][freq[0] - 2:freq[0]])
        hca[0] = avg(ffft[0][freq[1]:freq[1] + 2])
        hca[1] = avg(ffft[1][freq[1]:freq[1] + 2])
        hca[2] = avg(ffft[2][freq[1]:freq[1] + 2])
        hca[3] = avg(ffft[3][freq[1]:freq[1] + 2])
        for x in range(0, 124):
            bcga[0] = avg([lca[0], hca[0]])
            bcga[1] = avg([lca[1], hca[1]])
            bcga[2] = avg([lca[2], hca[2]])
            bcga[3] = avg([lca[3], hca[3]])
        asb[0] = alpha[0]/bcga[0]
        asb[1] = alpha[1]/bcga[1]
        asb[2] = alpha[2]/bcga[2]
        asb[3] = alpha[3]/bcga[3]
        asa = avg(alpha) - avg([avg(asb), avg(asbt)])
        asbt = inc4
        asbt[0] = asb[0]
        asbt[1] = asb[1]
        asbt[2] = asb[2]
        asbt[3] = asb[3]
        aous = asa - 0.3
        if aous > 0:
            alpdout = 1
        else:
            alpdout = 0

        # BETA #
        lcb = inc4
        hcb = inc4
        freq = [15, 29]
        bcgb = inc4
        bsb = inc4
        bsa = 0
        beta = [[0], [0], [0], [0]]
        beta[0] = avg(ffft[0][freq[0]:freq[1]])
        beta[1] = avg(ffft[1][freq[0]:freq[1]])
        beta[2] = avg(ffft[2][freq[0]:freq[1]])
        beta[3] = avg(ffft[3][freq[0]:freq[1]])
        lcb[0] = avg(ffft[0][freq[0] - 2:freq[0]])
        lcb[1] = avg(ffft[1][freq[0] - 2:freq[0]])
        lcb[2] = avg(ffft[2][freq[0] - 2:freq[0]])
        lcb[3] = avg(ffft[3][freq[0] - 2:freq[0]])
        hcb[0] = avg(ffft[0][freq[1]:freq[1] + 2])
        hcb[1] = avg(ffft[1][freq[1]:freq[1] + 2])
        hcb[2] = avg(ffft[2][freq[1]:freq[1] + 2])
        hcb[3] = avg(ffft[3][freq[1]:freq[1] + 2])
        for x in range(0, 124):
            bcgb[0] = avg([lcb[0], hcb[0]])
            bcgb[1] = avg([lcb[1], hcb[1]])
            bcgb[2] = avg([lcb[2], hcb[2]])
            bcgb[3] = avg([lcb[3], hcb[3]])
        bsb[0] = beta[0]/bcgb[0]
        bsb[1] = beta[1]/bcgb[1]
        bsb[2] = beta[2]/bcgb[2]
        bsb[3] = beta[3]/bcgb[3]
        bsa = avg(alpha) - avg([avg(asb), avg(asbt)])
        bsbt = inc4
        bsbt[0] = asb[0]
        bsbt[1] = asb[1]
        bsbt[2] = asb[2]
        bsbt[3] = asb[3]
        bous = bsa - 0.3
        if bous > 0:
            blpdout = 1
        else:
            blpdout = 0
        # FOCUS #
        if (asa >= 0.7) and (asa <= 2.0) and (bsa <= 0.7) and (bsa >= 0):
            focout = 1
            focstri = "\x1B[32mFocused!\x1B[36m".rjust(28)
            focPi = "\x1B[32m⏿\x1B[36m"
            drawCaseEff([69, int(int(rows)/2 + 8)], [42, 12], "\x1B[32m\x1B[44m\x1B[1m\x1B[2m")
        else:
            focout = 0
            focstri = "\x1B[31mNot Focused!\x1B[36m".rjust(28)
            focPi = "\x1B[31m⏳\x1B[36m"
            drawCaseEff([69, int(int(rows)/2 + 8)], [42, 12], "\x1B[31m\x1B[44m\x1B[1m\x1B[2m")
        pcco(85, int(int(rows)/2 + 14), focstri + " " + focPi)
        # DES #
        # BAND #
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

        pcco(85, int(int(rows)/2 + 16), str(round(alphav * 100)/100).rjust(20) + " ")
        pcco(85, int(int(rows)/2 + 17), str(round(betav * 100)/100).rjust(20) + " ")
        # DISPLAY #
        if ((betav - 0.5) <= 0.7) and ((betav - 0.5) >= 0.0) and (alphav <= 2.0) and (alphav >= 0.7):
            focstr = "\x1B[32mFocused!\x1B[36m".rjust(28)
            focP = "\x1B[32m⏿\x1B[36m"
            drawCaseEff([70, int(int(rows)/2 + 9)], [40, 10], "\x1B[32m\x1B[44m\x1B[1m\x1B[2m")
        else:
            focstr = "\x1B[31mNot Focused!\x1B[36m".rjust(28)
            focP = "\x1B[31m⏳\x1B[36m"
            drawCaseEff([70, int(int(rows)/2 + 9)], [40, 10], "\x1B[31m\x1B[44m\x1B[1m\x1B[2m")
        pcco(85, int(int(rows)/2 + 12), focstr + " " + focP)
        # DESIGN WORK #
        pcco(rp2[0] + 1, rp2[1] - 2,str(wlin + red + str(cu[1]).rjust(col_width) + " "  + wlin + hbl + str(cu[2]).rjust(col_width) + " " + wlin + red + str(cu[3]).rjust(col_width) + " "  + wlin + hbl + str(cu[4]).rjust(col_width) + " " + "\x1B[44m"))
        pcco(stfft[0], stfft[1] + 4, strln)
        sgnstr = str(w2 + w2 + w2 + w2 + bb + "FFTs" + "\x1B[44m\x1B[34m###\x1B[0m " + str(ffc(0, avgfft)) + w3 +  str(ffc(1*schr - 1, avgfft)) + w3 +   str(ffc(2*schr - 1, avgfft)) + w3 + str(ffc(3*schr - 1, avgfft)) + w3 + str(ffc(4*schr - 1, avgfft)) + w3 + str(ffc(5*schr - 1, avgfft)) + w3 + str(ffc(6*schr - 1, avgfft))  + w3 + str(ffc(7*schr - 1, avgfft))  + w3 + str(ffc(8*schr - 1, avgfft))  + w3 + str(ffc(9*schr - 1, avgfft)) + w3 + str(ffc(10*schr - 1, avgfft)) + " \x1B[44m")
        pcco(stfft[0], stfft[1]+5, sgnstr)
        #wtf = wtf + 1
        #if wtf>30:
        #    drawAll()
        #    wtf = 0
        #pcco(2, 20, " \n \n \n ")
        pcco(int(columns) - 33, 3, str(int(abs(tmm - time.time()))).rjust(5))
        pcco(5, 20, "          ")
        pcco(5, 20, "")
        sleep(0.01)

def drawAll():

    pcco(rp2[0] + 1, rp2[1] - 4, "\x1B[37;44mKanal 1 (GELB)".rjust(26) + "\x1B[37mKanal 2 (ORANGE)".rjust(31) + "\x1B[37mKanal 3 (ROT)".rjust(31) + "\x1B[37mKanal 4 (BRAUN)".rjust(31))
    stfft = [30, 4]
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
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
def avg(x):
    ma = []
    for a in range (0, len(x) - 1):
        ma.append(float(x[a]))
    return float(sum(ma))/float(len(ma))
def tprint():
    try:
        linewp()
        while True:
            key = (inkey())
            ts, addr = sock_tss.recvfrom(1024) # buffer size is 1024 bytes
            foc, addr2 = sock_foc.recvfrom(1024)
            formf = ts[22:-4]
            ch = str(formf).split(',')
            cu = [time.time(), float(ch[0][2:-1]), float(ch[1]), float(ch[2]), float(ch[3][0:-1])]
            sleep(.004)
            sys.stdout.write(wlin + red + str(cu[1]).ljust(col_width) + wlin + hbl + str(cu[2]).ljust(col_width) + wlin + red + str(cu[3]).ljust(col_width) + wlin + hbl + str(cu[4]).ljust(col_width) + wlin + str(str(foc)[25:-7]).ljust(4) + wlin + "\n")
            if key in ['o', ' ']:
                   smpi[0].append(cu[1])
                   smpi[1].append(cu[2])
                   smpi[2].append(cu[3])
                   smpi[3].append(cu[4])
                   foma.append(str(foc)[25:-7])
            if key == 'q':
                   exit()
    except:
        smp0 = [sum(smpi[0])/len(smpi[0]), sum(smpi[1])/len(smpi[1]), sum(smpi[2])/len(smpi[2]), sum(smpi[3])/len(smpi[3])]
        linewp()
        print(wlin1 + str(smp0[0]).ljust(col_width) + wlin1 + str(smp0[1]).ljust(col_width) + wlin1 + str(smp0[2]).ljust(col_width) + wlin1 + str(smp0[3]).ljust(col_width) + wlin)
        linew()
        term(smp0, smpi)
        exit()

# ---

def term(inv1, inv2):
    m0 = open("./files/smpi.opt.0.dat","w")
    m1 = open("./files/smpi.opt.1.dat","w")
    m2 = open("./files/smpi.opt.2.dat","w")
    m3 = open("./files/smpi.opt.3.dat","w")
    fo = open("./files/focus.opt.3.dat","w")
    ml = open("./files/smpi.log.dat","a")
    ow1 = ""
    ow2 = ""
    ow3 = ""
    ow4 = ""
    for i in range(0, len(inv2[0])):
        ow1 = ow1 + str(inv2[0][i]) + "|"
    for i in range(0, len(inv2[1])):
        ow2 = ow2 + str(inv2[1][i]) + "|"
    for i in range(0, len(inv2[2])):
        ow3 = ow3 + str(inv2[2][i]) + "|"
    for i in range(0, len(inv2[3])):
        ow4 = ow4 + str(inv2[3][i]) + "|"
    m0.write(str(ow1))
    m1.write(str(ow2))
    m2.write(str(ow3))
    m3.write(str(ow4))
    ml.write(str(inv2))
    fo.write(str(foma))
    exit()

def delt():
    m0 = open("./files/smpi.opt.0.dat","w")
    m1 = open("./files/smpi.opt.1.dat","w")
    m2 = open("./files/smpi.opt.2.dat","w")
    m3 = open("./files/smpi.opt.3.dat","w")
    m0.write("1.0")
    m1.write("1.0")
    m2.write("1.0")
    m3.write("1.0")
    exit()
def prout():
    while True:
        ts, addr = sock_tss.recvfrom(1024) # buffer size is 1024 bytes
        formf = ts[22:-4]
        ch = str(formf).split(',')
        cu = [time.time(), float(ch[0][2:-1]), float(ch[1]), float(ch[2]), float(ch[3][0:-1])]
        sleep(.004)
        sys.stdout.write(wlin + red + str(cu[1]).ljust(col_width) + wlin + hbl + str(cu[2]).ljust(col_width) + wlin + red + str(cu[3]).ljust(col_width) + wlin + hbl + str(cu[4]).ljust(col_width) + wlin + "\n")
        sleep(.2)
#ser = serial.Serial()
#ser.port = '/dev/ttyS0'
#ser.baudrate = 115200
#ser.open()
#print(ser.name)
#ser.close()
