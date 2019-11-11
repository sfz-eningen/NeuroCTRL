class AIStream():
  plist = {
    "band": 12345,
    "fft": 12346,
    "focus": 12347
    }
  def __init__(self, host="127.0.0.1"):
    self.sb = Stream(self.plist["band"], host=host)
    self.sb.start()
    self.sf = Stream(self.plist["focus"], host=host)
    self.sf.start()
  def read(self):
    sbd = self.sb.read()
    sfd = self.sf.read()
    sfm = []
    sbm = []
    for x in sbd:
      yield x["data"]
    for y in sfd:
      yield y["data"]
  def stop(self):
    self.sb.stop()
    self.sf.stop()