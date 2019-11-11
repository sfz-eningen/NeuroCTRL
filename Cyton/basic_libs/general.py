import os
import time



class fwatcher():
    t = 0.0
    def __init__(self, file):
        self.t, self.file = time.time(), os.path.basename(file)
    def eof(self):
        co = f"""\x1B[33;1m{self.file}:EOF\n  \x1B[32;1mExecution took: {round(100*(time.time()-self.t))/100}s\x1B[0m\n"""
        print(co)

class swatcher():
    t = 0.0
    def __init__(self, file):
        self.t, self.file = time.time(), name
    def eof(self):
        co = f"""\x1B[33;1m{self.file}:EOS\n  \x1B[32;1mExecution took: {round(100*(time.time()-self.t))/100}s\x1B[0m\n"""
        print(co)

class iwatcher():
    t = 0.0
    def __init__(self, file):
        self.t, self.file = time.time(), os.path.basename(file)
    def eof(self):
        co = f"""\x1B[33;1m{self.file}:EOI\n  \x1B[32;1mImport took: {round(100*(time.time()-self.t))/100}s\x1B[0m\n"""
        print(co)


def SectionBanner(section, status):
    if status == 0:
        status = "START"
    else:
        status = "STOP"
    print("\n\x1B[34;1m\t" + f"""---------- {section}:{status} ----------""".center(44, "-") + "\x1B[0m\n")