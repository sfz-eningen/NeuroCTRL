import random
import time
import math
l = ["Hello World", "I am here", "I am Groot", "Frederik ist cool"]

def scramble(lt):
    ltt = list(lt)
    for i in range(len(ltt)):
        v = random.choice(ltt)
        yield v
        ltt.remove(v)

x = range(361)
def singen(h):
    for j in h:
        yield math.sin(j)

def f(x):
    return pow(x, 2)

for h in range(10):
    print(f(h))