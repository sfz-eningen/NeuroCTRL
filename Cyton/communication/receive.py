# IMPORTS
from communication import gData
import logging
import threading
from threading import Thread
import time
from queue import Queue
import ctypes
import sys
# FUNCTIONS
def bprepr(data):
  for x in data:
    for y in x:
      sys.stdout.write(str(y) + " ")
    sys.stdout.write("\n")
  sys.stdout.write("\n\n")

# CLASSES
class Looper(Thread): 
  prog = []
  def __init__(self, name, q, stream): 
    Thread.__init__(self) 
    self.name = name 
    self.q = q
    self.stream = stream
            
  def run(self): 
    # target function of the thread class 
    try: 
      while True: 
        dat = self.stream.read()
        # self.q.put(dat)
        self.prog.append(dat)
    finally: 
      print('ended') 
          
  def get_id(self): 
    # returns id of the respective thread 
    if hasattr(self, '_thread_id'): 
      return self._thread_id 
    for id, thread in threading._active.items(): 
      if thread is self: 
        return id
  
  def raise_exception(self): 
    thread_id = self.get_id() 
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 
          ctypes.py_object(SystemExit)) 
    if res > 1: 
      ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0) 
      print('Exception raise failure') 

class ProtocolUnknown(Exception):
    pass

class Stream():
  # VARIABLES
  port, protocol, bufs, host = 0, 1, 200, "127.0.0.1"
  handle = None
  active = 1
  # INIT
  def __init__(self, port, protocol=1, bufs=200, host="127.0.0.1"):
    self.port, self.protocol, self.bufs, self.host = port, protocol, bufs, host
    del port, protocol, bufs, host
    if self.protocol == 1:
      self.handle = gData.getUDP(host=self.host, port=self.port, buff=1024*16)
    elif self.protocol == 2:
      self.handle = gData.getTCP(host=self.host, port=self.port, buff=1024*16)
    else:
      raise ProtocolUnknown(f"Unknown Protocol: '{self.protocol}'")
  # FUNCTIONS
  def convert(self, data):
    print(data)
  def start(self):
    self.q = Queue()
    self.th = Looper("Lp1", self.q, self.handle)
    self.th.start()
  def stop(self):
    self.th.raise_exception()
  def get(self):
    while self.th.prog == []:
      pass
    dat = self.th.prog
    self.th.prog = []
    return dat
  def read(self):
    for x in self.get():
      yield eval(str(x)[2:-5])



class AutoStream():
  plist = {
    "band": 12345,
    "fft": 12346,
    "focus": 12347
    }
  def __init__(self, dtype):
    self.s = Stream(self.plist[dtype])
    self.s.start()
  def read(self):
    return self.s.read()
  def stop(self):
    self.s.stop()
