from communication import AutoStream, bprepr
from aiprep import AIStream
import sys

s1 = AutoStream("band")
try:
  while 1:
    for e in [s1.read()]:
      for x in e:
        bprepr(x)
except:
  s1.stop()