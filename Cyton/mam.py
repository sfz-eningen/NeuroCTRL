import shutil
import sys
import time

def SectionBanner(section, status=0):
    columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    del rows
    if status == 0:
        status = "START"
    else:
        status = "END"
    print("\n\x1B[34;1m" + f""" {section} """.center(columns - 1, "-") + "\x1B[0m")

def SectionSwitch(section1, section2):
    columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    del rows
    print("\n\x1B[34;1m" + f""" {section1}:END -> {section2}:START""".center(columns - 1, "-") + "\x1B[0m")

def waclean():
    columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    sys.stdout.write(f"\x1B[6;0m" + "".ljust(columns*22, " "))
    sys.stdout.write("\x1B[6;2H")

def inp():
    columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    sys.stdout.write(f"\x1B[{rows-1}H\x1B[31;1;42m" + "[STOP|RES] > ".center(columns) + "\x1B[0m")
    return input(f"\x1B[{rows-1}H\x1B[31;1;47m" + "[STOP|RES] > \x1B[33;1;42m ")

def ini():
    sys.stdout.write(f"\x1B[{rows-1}H\x1B[31;1;42m" + "".center(columns) + "\x1B[0m")