import os
import time

def highlight_module(stg, typ="module"):
    so = ""
    for y in stg.split("."):
        so = f"{so}\x1B[33;1m{y}\x1B[32m."
    so = f"{so[:-1]}\x1B[0m"
    return f"\x1B[32;1m<\x1B[35;1m{typ} {so}\x1B[32;1m>\x1B[0m"

def highlight_script(file):
    so = ""
    so = f"{so[:-1]}\x1B[0m"
    return f"\x1B[32;1m<\x1B[35;1mscript \x1B[33;1m{file}\x1B[32;1m>\x1B[0m"


class fwatcher():
    t = 0.0
    def __init__(self, file):
        self.t, self.file = time.time(), highlight_script(os.path.basename(file))
    def eof(self):
        co = f"""\x1B[33;1m{self.file}\x1B[34;1m:\x1B[32;1mEOF\n  \x1B[32;1mExecution took: {round(100*(time.time()-self.t))/100}s\x1B[0m\n"""
        print(co)

class swatcher():
    t = 0.0
    def __init__(self, file):
        self.t, self.file = time.time(), name
    def eof(self):
        co = f"""\x1B[33;1m{self.file}\x1B[34;1m:\x1B[32;1mEOS\n  \x1B[32;1mExecution took: {round(100*(time.time()-self.t))/100}s\x1B[0m\n"""
        print(co)

class iwatcher():
    t = 0.0
    def __init__(self, file):
        self.t, self.file = time.time(), os.path.basename(file)
    def eof(self):
        co = f"""\x1B[33;1m{self.file}\x1B[34;1m:\x1B[32;1mEOI\n  \x1B[32;1mImport took: {round(100*(time.time()-self.t))/100}s\x1B[0m\n"""
        print(co)

class pwatcher():
    t = 0.0
    def __init__(self, name, typ="module"):
        self.t, self.file = time.time(), highlight_module(name, typ=typ)
    def eof(self):
        co = f"""\x1B[33;1m{self.file}\x1B[34;1m:\x1B[32;1mEOI\n  \x1B[32;1mImport took: {round(100*(time.time()-self.t))/100}s\x1B[0m\n"""
        print(co)

def SectionBanner(section, status):
    import shutil
    columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    del rows
    if status == 0:
        status = "START"
    else:
        status = "STOP"
    print("\n\x1B[34;1m\t" + f"""---------- {section}:{status} ----------""".center(columns - 12, "-") + "\x1B[0m")