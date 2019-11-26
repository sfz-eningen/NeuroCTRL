import os
import time


class SWriter(): 
    """
    ## Sample Writer
    ### Usage (Python 3.x.x):
    ```
    >>> s = SWriter()
    >>> s.write(wvar) # Write to File
    >>> type(wvar)
    str
    ```
    """
    # Variables
    dirc = __file__.replace(
        os.path.basename(__file__), "")
    sdir = f"{dirc}samples\\"
    i = 0
    f = None

    def __init__(self, sname):
        self.sdir = self.sdir + sname
        print("Output Folder:", self.sdir)
        if not(os.path.exists(self.sdir)): 
            try:
                os.mkdir(self.sdir)
            except OSError:
                print("Creation of the directory %s failed"
                 % self.sdir)
        self.sname = sname
        self.cnf()
    # Write Data to file
    def write(self, data): 
        if self.i > 512: 
            self.cnf()
        self.f.write(str(data) + "\n")
        self.i += 1
    # Create New File
    def cnf(self): 
        try:
            self.f.close()
        except:
            pass
        name = f"{self.sdir}\\{self.sname}_{time.time()}.smp"
        self.f = open(name, "w")
        self.i = 0
        print("\n", name)

w = SWriter("Session1")