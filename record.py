from communication import AutoStream
from AI import dimc
import keyboard
from datetime import datetime
import sys
import msvcrt

def keypress(): 
    import msvcrt               
    while 1:
        if msvcrt.kbhit():              # Key pressed?
            a = ord(msvcrt.getch())     # get first byte of keyscan code
            if a == 0 or a == 224:      # is it a function key?
                msvcrt.getch()          # discard second byte of key scan code
                return 0                # return 0
            else:
                return a                # else return ascii code

Stream = AutoStream("band")

inpt = int(input("ENTER TRAINED STATE! (int) > "))
file = f"./samples/sample_record_{str(datetime.now()).replace(':', '-').replace(' ', '--')}.csv"
f = open(file, "w+")
topline = ""
for ch in range(16):
    for band in ["delta", "theta", "alpha", "beta", "gamma"]:
        topline += f"{band}_{ch}; "


f.write(f"{topline}ACTION\n")
f.close()

f = open(file, "a+")

try:
    while 1:
        print("LOOP")

        while keypress()==114:
            lineo = ""
            v = 0
            for v in Stream.read():
                pass
            for val in dimc(v):
                lineo += f"{val}; "
            f.write(f"{lineo}1\n")
            sys.stdout.write(".")
            sys.stdout.flush()
        
        if keypress()==113:
            sys.exit()

except KeyboardInterrupt:
    pass
finally:
    f.close()
    Stream.stop()