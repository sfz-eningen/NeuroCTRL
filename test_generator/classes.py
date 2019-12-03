from threading import Thread
import threading
import ctypes
import random
import sys
import socket

class TestStreamer(Thread):
    UDP_IP = "127.0.0.1"
    UDP_PORT = 12345

    def __init__(self): 
        Thread.__init__(self)
        self.sock = socket.socket(socket.AF_INET, # Internet
                             socket.SOCK_DGRAM) # UDP

    def run(self):
        sys.stdout.write(f'\n\x1B[1;35mTEST-Thread has been started!\n\x1B[0m\t\x1B[34;1mHOST={self.UDP_IP}\n\n\n\x1B[0m') 
        sys.stdout.flush()
        try:
            while 1:
                ms = []
                for x in range(16):
                    ms.append([random.random()*10, random.random()*10, random.random()*10, random.random()*10, random.random()*10])
                data = {"typ": "bandPower", "data": ms}
                self.sock.sendto(bytes(str(data), "utf-8"), (self.UDP_IP, self.UDP_PORT))
        finally:
            sys.stdout.write(f'\n\n\x1B[1;31mAPI-Thread has been stopped!\n\x1B[0m\t\x1B[33;1mHOST={self.UDP_IP}\n\n\x1B[0m') 
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