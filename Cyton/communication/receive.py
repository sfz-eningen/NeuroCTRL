# IMPORTLIB
import importlib.util
ibd = ""
for x in __file__.split("\\")[:-2]:
  ibd = f"{ibd}{x}\\"
spec = importlib.util.spec_from_file_location("pwatcher", f"{ibd}\\basic_libs\\general.py"); gen = importlib.util.module_from_spec(spec); spec.loader.exec_module(gen); pwatcher = gen.pwatcher
from .gData import *
# NORMAL IMPORTS
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
  """
  Displays Band-Power data
  """
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

# CLASSES
class Looper(Thread): 
  # DESCRIPTION
  """
  Thread to read and collect OpenBCI-GUI data.\n
  Usage:\n
   >>> Looper(name, q, stream)\n
  How to read:\n
    >>> l = Looper("L1", Queue(), s)
   >>> [...]
   >>> def read():
   >>>   while l.prog == []:
   >>>     pass
   >>>   d = l.prog
   >>>   l.prog = []
   >>>   return d
   >>> [...]
   >>> data = read() 
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
    t = time.time()
    sys.stdout.write(f'\n\x1B[1;35mThread "{self.name}" has been started!\n\x1B[1;34m  RUNTIME: {round((time.time()-t)*100)/100}s\n  stream-info:\n\t{self.stream}\x1B[0m\n') 
    try: 
      while True: 
        dat = self.stream.read()
        # self.q.put(dat)
        self.prog.append(dat)
    except: 
      # Stop Message
      sys.stdout.write(f'\n\n\x1B[1;31mThread "{self.name}" has been stopped!\n\x1B[1;33m  RUNTIME: {round((time.time()-t)*100)/100}s\n  stream-info:\n\t{self.stream}\x1B[0m') 
          
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
   >>> Stream(port[, protocol, bufs, host])\n
  Returns:\n
   >>> self():    None
   >>> .start():  None
   >>> .stop():   None
   >>> .read():   <generator object Stream.read>
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
      self.handle = getUDP(host=self.host, port=self.port, buff=1024*16)
    elif self.protocol == 2:
      self.handle = getTCP(host=self.host, port=self.port, buff=1024*16)
    else:
      raise ProtocolUnknown(f"Unknown Protocol: '{self.protocol}'")
  # FUNCTIONS
  def start(self):
    """
    Start the Stream-Thread:\n
     >>> Looper(f"L{self.idd}P{self.protocol}", self.q, self.handle)
    """
    self.q = Queue()
    self.th = Looper(f"L{self.idd}P{self.protocol}", self.q, self.handle)
    self.th.start()
    sys.stdout.write(f'\n\x1B[1;35mStream "{self.name}" has been started!\n\x1B[1;34m  stream-info:\n\t{self.handle}\x1B[0m\n') 
  def stop(self):
    """
    Stop the Stream-Thread:\n
     >>> self.th.raiseexception()
    """
    self.th.raiseexception()
    time.sleep(0.1)
    sys.stdout.write(f'\n\n\x1B[1;31mStream "{self.name}" has been stopped!\n\x1B[1;33m  stream-info:\n\t{self.handle}\x1B[0m') 
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
   >>> AutoStream({band|fft|focus})
  Returns:\n
   >>> self:\tNone
   >>> stop:\tNone
   >>> read:\t<generator object Stream.read>
  """
  plist = {
    "band": 12345,
    "fft": 12346,
    "focus": 12347
    }
  def __init__(self, dtype):
    self.dtype = dtype
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
     >>> self.th.raiseexception()
    """
    self.s.stop()