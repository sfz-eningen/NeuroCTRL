from flask import Flask  
from flaskwebgui import FlaskUI   # get the FlaskUI class
from flask_restful import Resource, Api
from threading import Thread
import threading
import ctypes
import sys
import random

def dimc(dct):
    data = dct["data"]
    dout = []
    if len(data) == 16:
        for channel in data:
            for band in channel:
                dout.append(band)
    elif len(data) == 8:
        for channel in data:
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
    elif len(data) == 4:
        for channel in data:
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
            for band in channel:
                dout.append(band)
    else:
        raise Exception(f"UNKNOWN DATA FORMAT: {len(data)} Channels; VALID COUNTS: " + "{4, 8, 16}")
    return dout

def rename(newname):
    def decorator(f):
        f.__name__ = newname
        return f
    return decorator

class flaskAPI(Thread):
    """
    API Thread to send data via {Host}:5000/
    Usage:
    >>> flaskAPI(handle [, local=0, page="/"])
    """
    pagesL = {}
    def __init__(self, local=0):
        print("API Online")
        Thread.__init__(self)
        self.local = local
        self.app = Flask(__name__)
        @self.app.route("/<page>")
        def Send(page):
            so = []
            pred = []
            page = self.pagesL['/'+page]
            for x in page['handle'].read():
                d = dimc(x)
            for x in page['ai']:
                print(page['ai'])
                pred.append(float(x.analyze([d])))
                print(pred)
            return {"data": pred}

    def addR(self, handle, ais, page="/"):
        print("Adding...")
        self.pagesL[page] = {"handle": handle, "ai": ais}
        print(self.pagesL[page])
        vt = random.randint(100000, 999999)
    

    def run(self):
        host="0.0.0.0"
        # if self.local == "0": host='0.0.0.0'
        # else: host="127.0.0.1"
        sys.stdout.write(f'\n\x1B[1;35mAPI-Thread has been started!\n\x1B[0m\t\x1B[34;1mHOST={host}\n\n\n\x1B[0m') 
        sys.stdout.flush()
        try:
            self.app.run(host=host)
        except:
            sys.stdout.write(f'\n\n\x1B[1;31mAPI-Thread has been stopped!\n\x1B[0m\t\x1B[33;1mHOST={host}\n\n\x1B[0m') 
            sys.stdout.flush()

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