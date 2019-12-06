from communication import AutoStream
# from AI import dimc
import keyboard
from datetime import datetime
import sys
import msvcrt

def dimc(dct):
    data = dct["data"]
    dout = []
    if len(data) == 16:
        for channel in data:
            for band in channel:
                dout.append(band)
    elif len(data) == 8:
        for channel in data:
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
    elif len(data) == 4:
        for channel in data:
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
    else:
        raise Exception(f"UNKNOWN DATA FORMAT: {len(data)} Channels; VALID COUNTS: " + "{4, 8, 16}")
    return dout

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
        inpt = input("\n\nENTER TRAINED STATE! (int/q) > ")
        if inpt == "q":
            break
        while 1:
            print("LOOP")

            while keypress()==114:
                lineo = ""
                v = 0
                for v in Stream.read():
                    pass
                for val in dimc(v):
                    lineo += f"{val}; "
                f.write(f"{lineo}{inpt}\n")
                sys.stdout.write(".")
                sys.stdout.flush()
            
            if keypress()==113:
                break
except KeyboardInterrupt:
    pass
finally:
    f.close()
    Stream.stop()