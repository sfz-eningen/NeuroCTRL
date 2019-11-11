from basic_libs import *
w = fwatcher(__file__)
from communication import AutoStream, bprepr
from aiprep import AIStream
import sys

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