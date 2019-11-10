from communication import AutoStream, bprepr
import sys

s = AutoStream("band")
try:
  while 1:
    for x in s.read():
      bprepr(x)
except:
  s.stop()
s.stop()