# IMPORTS
from __init__ import *
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
  pass