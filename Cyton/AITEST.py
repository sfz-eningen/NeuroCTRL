import AI
import time
from random import random

a = AI.brainAI()
a.train()
print("Trained")
t = time.time()
print(a.analyze(dataset))
print(time.time()-t)