from flask import Flask  
from flaskwebgui import FlaskUI   # get the FlaskUI class
from flask_restful import Resource, Api

class RCase(Resource):
    handle = None
    def __init__(self, handle):
        self.handle = handle
    def get(self):
        st = self.handle.st
        self.handle.st = []
        return st



class webAPI(): 
    # VARIABLES
    name, app, api, handle = None, None, None, None
    # Functions
    def __init__(self, handle, name="CLI"): 
        self.handle = handle
        self.name = name
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(handle, '/')

