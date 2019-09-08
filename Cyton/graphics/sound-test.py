import plot
from plot import *
import sys
from time import sleep
from threading import Thread
import multiprocessing
import random
import os
import numpy
init=\
"""
import random
import numpy
from random import random
i = 1
def pp(ind):
  return ind + 1
"""
code=\
"""
m = []
for x in range(100):
  m.append(cos(i)/abs(cos(i))*1)
write(m)
i = pp(i)
"""
plt = LivePlot(title="Sharp Wave Plot over Time", axrange=[1000.0, 3, -3], axes=["Read ([t] = 1s)", "Voltage ([U]∕10⁶ = 1μV)"])
PlotUpdater(plt, code=code, init=init, lenw=0.01).start()
plt.start()
sys.exit("TERMINATED (" + os.path.basename(__file__) + ")")