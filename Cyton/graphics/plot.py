#!/usr/bin/env python
import pylab
import tkinter
from pylab import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import multiprocessing
import numpy as np
import time
import shlex
from subprocess import Popen, PIPE, STDOUT
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
class LivePlot():
  def __init__(self, axrange=[100.0, 50, -50], axes=["Time (ms)", "Amplitude (Vrms)"], title="Live Plot", timew = 0.01, funcstr="random()*3-1.5", defs="f=1"):
    exec(defs)
    self.axl = axrange[2]
    self.axu = axrange[1]
    self.axlen = axrange[0]
    
    self.funcstr = funcstr
    self.timew = timew
    self.xAchse=pylab.arange(0,100,1)
    self.yAchse=pylab.array([0]*100)

    self.fig = pylab.figure(1)
    self.ax = self.fig.add_subplot(111)
    self.ax.grid(True)
    self.ax.set_title(title)
    self.ax.set_xlabel(axes[0])
    self.ax.set_ylabel(axes[1])
    self.ax.axis([0,axrange[0],axrange[2],axrange[1]])
    self.line1=self.ax.plot(self.xAchse,self.yAchse,'-')

    self.manager = pylab.get_current_fig_manager()

    self.values=[]
    self.values = [0 for x in range(int(self.axlen))]

    self.Ta=0.01
    self.fa=1.0/self.Ta
    self.fcos=3.5

    self.Konstant=cos(2*pi*self.fcos*self.Ta)
    self.T0=1.0
    self.T1=self.Konstant
    self.vsa = self.values
  def SinwaveformGenerator(self, arg):
    #global self.values,self.T1,self.Konstant,self.T0
    #ohmegaCos=arccos(T1)/Ta
    #print "fcos=", ohmegaCos/(2*pi), "Hz"
    #print("SinwaveformGenerator(%s, %s)" % (self, arg))
    if self.values != self.vsa:
      #print("self.values != self.vsa")
      self.Tnext=((self.Konstant*self.T1)*2)-self.T0
      self.T0=self.T1
      self.T1=self.Tnext
      self.vsa = self.values

  def RealtimePloter(self, arg):
    #print("RealtimePloter(%s, %s)" % (self, arg))
    #global self.values
    self.CurrentXAxis=pylab.arange(len(self.values)-int(self.axlen),len(self.values),1)
    self.line1[0].set_data(self.CurrentXAxis,pylab.array(self.values[-int(self.axlen):]))
    self.ax.axis([self.CurrentXAxis.min(),self.CurrentXAxis.max(),self.axl,self.axu])
    self.manager.canvas.draw()
    #manager.show()
  def start(self):
    #print("start(%s)" % (self))
    #print("timer")
    self.timer = self.fig.canvas.new_timer(interval=20)
    #print("timer.add_callback")
    self.timer.add_callback(self.RealtimePloter, ())
    #print("timer2")
    self.timer2 = self.fig.canvas.new_timer(interval=20)
    #print("timer2.add_callback")
    self.timer2.add_callback(self.SinwaveformGenerator, ())
    #print("timer.start")
    self.timer.start()
    #print("timer2.start")
    self.timer2.start()
    # self.t = Thread(target=self.ufunc, args=())
    # self.t.daemon = True
    # self.t.start()
    #print("show")
    pylab.show()
    print("TERMINATED (" + str(os.path.basename(__file__)) + ")")
  def update(self, value, delay=0.000):
    if not(type(value) == list):
      value = [value]
    #sys.stdout.write("UPDATE: " + str(value) + "\n")
    times = time.time()
    for x in value:
      self.values.append(x)
    time.sleep(0.001*len(value))
    pass

from threading import Thread

class PlotUpdater():
  """
  Use the Function "write({data})" to update the Data
  """
  def __init__(self, handle, code="print(\"CODE\")", timew=0.000, init="print(\"INIT\")", lenw=0.001):
    print("HANDLE:", handle)
    print("CODE:\n" + code, "\nEOC")
    self.handle = handle
    if type(code) != str:
      raise(Exception,"WrongDataTypeException")
    self.lenw = lenw
    self.timew = timew
    self.code = code
    self.t = Thread( target=self.putData, args=())
    self.t.daemon = True
    self.init = init
  def putData(self):
    print("Starting Updater")
    handle = self.handle
    write = handle.update
    exec(self.init)
    times = time.time()
    while 1:
      exec(self.code)
      sys.stdout.write(str(time.time()-times) + "\n")
      times = time.time()
  def start(self):
    self.t.start()