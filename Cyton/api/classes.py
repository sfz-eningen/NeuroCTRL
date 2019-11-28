from flask import Flask  
from flaskwebgui import FlaskUI   # get the FlaskUI class
from flask_restful import Resource, Api
from threading import Thread


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

class flaskAPI(Thread):
    def __init__(self, handle):
        Thread.__init__(self)
        self.handle = handle
        self.app = Flask(__name__)
        @self.app.route("/")
        def SendData():
            st = self.handle.read()
            so = []
            for x in st:
                so.append(x["data"])
            return {"data": so}

    def run(self):
        self.app.run(host= '0.0.0.0')

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