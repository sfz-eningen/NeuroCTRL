# WATCHDOG
from Cyton.basic_libs import *
w = fwatcher(__file__)
# IMPORTS
from Cyton import *
# SCRIPT
try:
  SectionBanner("MAIN", 0)
  s1 = AutoStream("band")
  try:
    while 1:
      for e in [s1.read()]:
        for x in e:
          bprepr(x)
  except:
    SectionBanner("MAIN", 1)
    s1.stop()
finally: 
  w.eof()