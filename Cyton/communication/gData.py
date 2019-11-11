# IMPORTS
import socket
# CLASSES
class getUDP():
  """
  UDP Data Receiver
  """
  # VARIABLES
  sock = None
  host="127.0.0.1"
  port="67671"
  buff=1024
  # INIT
  def __init__(self, host="127.0.0.1", port="12345", buff=1024):
    self.host, self.port, self.buff = host, int(port), int(buff)
    del host, port, buff
    self.sock = socket.socket(socket.AF_INET,    # Internet
                              socket.SOCK_DGRAM) # UDP
    self.sock.bind((self.host, self.port))
  
  # FUNCTIONS
  def read(self):
    data, addr = self.sock.recvfrom(self.buff) # buffer size is 1024 bytes
    del addr
    return data
  def __repr__(self):
    ostr = "UDP Data Receiver\n\tHOST={host}\n\tPORT={port}".format(host=self.host, port=self.port)
    return ostr

class getTCP():
  """
  TCP Data Receiver
  """
  # VARIABLES
  sock = None
  host="127.0.0.1"
  port="67671"
  buff=1024
  # INIT
  def __init__(self, host="127.0.0.1", port="65535", buff=1024):
    self.host, self.port, self.buff= host, int(port), buff
    del host, port, buff
    self.sock = socket.socket(socket.AF_INET,    # Internet
                              socket.SOCK_STREAM) # UDP
    self.sock.bind((self.host, self.port))
    self.sock.listen(1)
    self.addr, self.conn = self.sock.accept()

  # FUNCTIONS
  def read(self):
    data = self.conn.recv(self.buff)
    if not(data): return None
    self.conn.send(data)               # echo
    return data
  def stop(self):
    self.conn.close()
  def __repr__(self):
    ostr = "TCP Data Receiver\n\tHOST={host}\n\tPORT={port}".format(host=self.host, port=self.port)
    return ostr
