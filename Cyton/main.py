import communication as com
import sys

s = com.AutoStream("band")
try:
  while 1:
    for x in s.read():
      sys.stdout.write(str(x["data"]))
finally:
  s.stop()