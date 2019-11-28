from flask import Flask  
from flaskwebgui import FlaskUI   # get the FlaskUI class
from flask_restful import Resource, Api
from threading import Thread
import threading
import ctypes
# class RCase(Resource):
#     def get(self):
#         return {"focused": 0, "detect": 0}



# class webAPI(): 
#     # VARIABLES
#     name, app, api, handle = None, None, None, None
#     # Functions
#     def __init__(self, handle, name="CLI"): 
#         self.handle = handle
#         self.name = name
#         self.app = Flask(__name__)
#         self.api = Api(self.app)
#         self.api.add_resource(RCase, '/detector')
#     def start(self):
#         self.app.run()
import random

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
    handle = []
    def __init__(self, local=0):
        Thread.__init__(self)
        self.local = local
        self.app = Flask(__name__)
    def addR(self, handle, page="/"):
        self.handle.append(handle)
        @self.app.route(page)
        @rename(str(random.randint(1000000, 9999999)))
        def SendData():
            st = self.handle[len(self.handle)-1].read()
            so = []
            for x in st:
                so.append(x["data"])
            return {"data": so}

    def run(self):
        try:
            if self.local == "0": host='0.0.0.0'
            else: host="127.0.0.1"
            self.app.run(host=host)
        except:
            print(f'\n\n\x1B[1;31mAPI Thread has been stopped!\n\x1B[0m') 

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