import .configparser

class Config():
  files = ["board.ini", "neural.ini", "ports.ini", "settings.ini"]
  def __init__(self):
    config = configparser.ConfigParser()
    for x in self.files:
      config.read(x)
      pass
    