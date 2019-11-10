# IMPORTS
import gData


# CLASSES

class Stream():
  # VARIABLES
  port, protocol, bufs, host = 0, 1, 200, "127.0.0.1"
  handle = None
  # SUBCLASSES
  class ProtocolUnknown(Exception):
    pass
  # INIT
  def __init__(self, port, protocol=1, bufs=200, host="127.0.0.1"):
    self.port, self.protocol, self.bufs, self.host = port, protocol, bufs, host
    del port, protocol, bufs, host
    if self.protocol == 1:
      self.handle = gData.getUDP(host=self.host, port=self.port, buff={1024})
    elif self.protocol == 2:
      self.handle = gData.getTCP(host=self.host, port=self.port, buff={1024})
    else:
      raise self.ProtocolUnknown(f"Unknown Protocol: '{self.protocol}'")
  # FUNCTIONS
  def convert(self, data):
    print(data)
  def read(self):
    pass


# Stream(35353, protocol=1)