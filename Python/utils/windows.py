#!/bin/python
import sys
import os
import utils.draw
from utils.draw import *
def w1():
    rowss, columnss = os.popen('stty size', 'r').read().split()
    rows = int(rowss)
    columns = int(columnss)
    rpw1 = [int((columns/4)*3 - 20), int(rows/2) - 10]
    rpwx = rpw1[0]
    rpwy = rpw1[1]
    print_co(rpwx, rpwy - 1,   "                        \x1B[1m\x1B[37m\x1B[44m")
    print_co(rpwx, rpwy - 1,   "                        ┏━━━━━━━━━━━━┓")
    print_co(rpwx, rpwy    ,   "                        ┃  Ganglion  ┠━━━━━━━━━━┓")
    print_co(rpwx, rpwy + 1,   "                        ┃    4CH     ┃        ╭─┸─╮")
    print_co(rpwx, rpwy + 2,   "                        ┃    BCI     ┃        │ ᛒ │ Simblee")
    print_co(rpwx, rpwy + 3,   "                        ┃    CHIP    ┃        ╰─┰─╯")
    print_co(rpwx, rpwy + 4,   "                        ┗━━━━┳┳┳┳━━━━┛          \x1B[35m╏\x1B[37m")
    print_co(rpwx, rpwy + 5,   "                             \x1B[33m┃┃┃┃\x1B[37m            \x1B[32m╭──\x1B[35m╇\x1B[32m──╮ ⎫\x1B[37m")
    print_co(rpwx, rpwy + 6,   "                             \x1B[33m╿╿╿╿\x1B[37m            \x1B[32m│  \x1B[35m╧\x1B[32m  │ ⎪\x1B[37m")
    print_co(rpwx, rpwy + 7,   "┏━━━━━━━━━━━━━━━━━━━━┓    Elektroden         \x1B[32m│  \x1B[35mᛒ\x1B[32m  │ ⎬ Bluetooth\x1B[37m")
    print_co(rpwx, rpwy + 8,   "┃     Console App    ┃                       \x1B[32m│  \x1B[35m╤\x1B[32m  │ ⎪\x1B[37m")
    print_co(rpwx, rpwy + 9,   "┣━━━━━━━━━━━━━━━━━━━━┫                       \x1B[32m╰──\x1B[35m╈\x1B[32m──╯ ⎭\x1B[37m")
    print_co(rpwx, rpwy + 10,  "┃ ┏━━━ FFT Table     ┃                          \x1B[35m╏\x1B[37m")
    print_co(rpwx, rpwy + 11,  "┃ ┗━━━ Freq. Table ━━╋━━━━━━ TSS ━┓           ╭─┸─╮")
    print_co(rpwx, rpwy + 12,  "┃                    ┃            ┃           │ ᛒ │ BT Dongle")
    print_co(rpwx, rpwy + 13,  "┃ ┏━━ Focus ━━ α/β ━━╋━━ Band x5 ━┫           ╰─┰─╯")
    print_co(rpwx, rpwy + 14,  "┃ ┃                  ┃            ┣━ 4CH ━┓    ┍╋┙  Serial Port IN")
    print_co(rpwx, rpwy + 15,  "┃ ┃ ┏━━ α/β ━━ cut ┳━╋━━━━━━ FFT ━┛       ┃     ┃")
    print_co(rpwx, rpwy + 16,  "┃ ┃ ┗ Focus ┓      ┃ ┃                 ┏━━┻━━━━━┻━━━━━━┓")
    print_co(rpwx, rpwy + 17,  "┃ ┗━━━━━━━━━┫      ┃ ┃                 ┃ UDP   TTY     ┃")
    print_co(rpwx, rpwy + 18,  "┃           ┃      ┃ ┃                 ┃ OpenBCI -GUI  ┃")
    print_co(rpwx, rpwy + 19,  "┃     Focus Widget ┃ ┃   Display Out ━━┫               ┃")
    print_co(rpwx, rpwy + 20,  "┃                  ┃ ┃                 ┗━━━━━━━━━━━━━━━┛")
    print_co(rpwx, rpwy + 21,  "┃       FFT Widget ┛ ┃")
    print_co(rpwx, rpwy + 22,  "┗━━━━━━━━━━━━━━━━━━━━┛")
