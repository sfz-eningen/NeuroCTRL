# IMPORTS
from basic_libs import *
i = iwatcher(__file__)
from communication import gData
import logging
import threading
from threading import Thread
import time
from queue import Queue
import ctypes
import sys
import random
# FUNCTIONS
def bprepr(data):
  bold = "\x1B[1m"
  clear = "\x1B[0m"
  nstr = ["delta", "theta", "alpha", "beta", "gamma"]
  cstr = ["35;2;1", "33;2;1"]
  sys.stdout.write(f"{bold} ")
  for x in nstr:
    sys.stdout.write(str(x)[0:8].ljust(8) + " ")
  dt = data["data"]
  sys.stdout.write(clear)
  for x in dt:
    sys.stdout.write("\n")
    if round(dt.index(x)/2)*2 == dt.index(x): stt = cstr[0] 
    else: stt = cstr[1]
    for y in x:
      sys.stdout.write("\x1B[" + stt + "m " + str(y)[0:8].ljust(8) + clear + "")
  sys.stdout.write("\n\n")

# CLASSES
class Looper(Thread): 
  # DESCRIPTION
  """
  Thread to read and collect OpenBCI-GUI data.\n
  Usage:\n
    \tLooper(name, q, stream)\n
  How to read:\n
    \tl = Looper("L1", Queue(), s)
    \t[...]
    \tdef read():
    \t  while l.prog == []:
    \t    pass
    \t  d = l.prog
    \t  l.prog = []
    \t  return d
    \t[...]
    \tdata = read() 
  """
  # VARIABLES
  prog = []
  # INIT
  def __init__(self, name, q, stream): 
    Thread.__init__(self) 
    self.name = name 
    self.q = q
    self.stream = stream
            
  def run(self): 
    """Collector Loop"""
    try: 
      while True: 
        dat = self.stream.read()
        # self.q.put(dat)
        self.prog.append(dat)
    except: 
      # Stop Message
      print(f'\n\n\x1B[1;31mThread "{self.name}" has been stopped!\n\x1B[1;33m  stream-id:\n\t{self.stream}\n\x1B[0m') 
          
  def get_id(self): 
    """returns id of the respective thread"""
    for id, thread in threading._active.items(): 
      if thread is self: 
        return id
  
  def raiseexception(self): 
    """Internal stop function."""
    thread_id = self.get_id() 
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
          ctypes.py_object(SystemExit)) 
    if res > 1: 
      ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
      print(f'\n\n\tException raise failure on Thread {self.name}!\n')

class ProtocolUnknown(Exception):
    pass

class Stream():
  """
  Data Stream Element to receive OpenBCI-GUI data.\n
  Usage:\n
    \tStream(port[, protocol, bufs, host])\n
  Returns:\n
    \tself():    None
    \t.start():  None
    \t.stop():   None
    \t.read():   <generator object Stream.read>
  """
  # VARIABLES
  port, protocol, bufs, host, name, idd, handle, active = 0, 1, 200, "127.0.0.1", "", 0, None, 1
  # INIT
  def __init__(self, port, protocol=1, bufs=200, host="127.0.0.1"):
    self.port, self.protocol, self.bufs, self.host = port, protocol, bufs, host
    self.idd = random.randint(100000, 999999)
    self.name = f"S{self.idd}P{self.protocol}"
    del port, protocol, bufs, host
    if self.protocol == 1:
      self.handle = gData.getUDP(host=self.host, port=self.port, buff=1024*16)
    elif self.protocol == 2:
      self.handle = gData.getTCP(host=self.host, port=self.port, buff=1024*16)
    else:
      raise ProtocolUnknown(f"Unknown Protocol: '{self.protocol}'")
  # FUNCTIONS
  def start(self):
    """
    Start the Stream-Thread:\n
      \tLooper(f"L{self.idd}P{self.protocol}", self.q, self.handle)
    """
    self.q = Queue()
    self.th = Looper(f"L{self.idd}P{self.protocol}", self.q, self.handle)
    self.th.start()
  def stop(self):
    """
    Stop the Stream-Thread:\n
      \tself.th.raiseexception()
    """
    self.th.raiseexception()
    time.sleep(0.1)
    print(f'\n\n\x1B[1;31mStream "{self.name}" has been stopped!\n\x1B[1;33m  stream-id:\n\t{self.handle}\n\x1B[0m') 
  def get(self):
    while self.th.prog == []:
      pass
    dat = self.th.prog
    self.th.prog = []
    return dat
  def read(self):
    """
    Read the data collected by the Stream-Thread
    """
    for x in self.get():
      try:
        yield eval(str(x)[2:-5])
      except:
        pass

class AutoStream():
  """
  Automanaged Stream starter: \n
  Usage:\n
    \tAutoStream({band|fft|focus})
  Returns:\n
    \tself:\tNone
    \tstop:\tNone
    \tread:\t<generator object Stream.read>
  """
  plist = {
    "band": 12345,
    "fft": 12346,
    "focus": 12347
    }
  def __init__(self, dtype):
    self.s = Stream(self.plist[dtype])
    self.s.start()
  def read(self):
    """
    Read the data collected by the Stream-Thread
    """
    return self.s.read()
  def stop(self):
    """
    Stop the Stream-Thread:\n
      \tself.th.raiseexception()
    """
    self.s.stop()
i.eof()