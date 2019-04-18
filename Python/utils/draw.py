#!/bin/python
import sys
def print_co(x, y, text):
    sys.stdout.write("\x1B[%d;%dH%s" % (y, x, text))
    sys.stdout.flush()
def line_x(x1, x2, y, ansi):
    for x in range(x1, x2):
        sys.stdout.write("%s\x1B[%d;%dH━\x1B[44m\x1B[36m" % (ansi, y, x))
    sys.stdout.flush()
def corn_ur(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┓"))
    sys.stdout.flush()
def corn_ul(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┏"))
    sys.stdout.flush()
def corn_lr(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┛"))
    sys.stdout.flush()
def corn_ll(x, y, ansi):
    sys.stdout.write("%s\x1B[%d;%dH%s\x1B[44m\x1B[36m" % (ansi, y, x, "┗"))
    sys.stdout.flush()
def line_y(y1, y2, x, ansi):
    for y in range(y1, y2):
        sys.stdout.write("%s\x1B[%d;%dH┃\x1B[44m\x1B[36m" % (ansi, y, x))
    sys.stdout.flush()
def line_cl_y(y1, y2, x):
    for y in range(y1, y2):
        sys.stdout.write("%s\x1B[%d;%dH \x1B[44m\x1B[36m" % ("\x1B[44m\x1B[34m", y, x))
    sys.stdout.flush()
def line_cl_x(x1, x2, y):
    for x in range(x1, x2):
        sys.stdout.write("%s\x1B[%d;%dH \x1B[44m\x1B[36m" % ("\x1B[44m\x1B[34m", y, x))
    sys.stdout.flush()
