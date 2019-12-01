"""
Beispiele, um Maximilian Python beizubringen
"""


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

# for h in range(10):
#     print(f(h))

class Hund():
    name = "Strolch"
    alter = 3.5
    rasse = "Dalmatiner"
    tricks = {"pfote": True, "maennchen": True, "bellen": True, "typ": "wuff"}

    def __init__(self, name, alter, rasse, tricks={}):
        if not tricks == {}:
            for x in tricks:
                if x in self.tricks:
                    self.tricks[x] = tricks[x]
                else:
                    print("wuff?")

        self.name = name
        self.alter = alter
        self.rasse = rasse
        typ = f'{self.tricks["typ"]} '
        print(f"{name}:\t\t * {random.randint(1,3)*typ}*")
    def bellen(self):
        if self.tricks["bellen"] == True:
            typ = f'{self.tricks["typ"]} '
            print(f"{self.name}:\t\t * {typ}*")
        else:
            typ = f'{self.tricks["typ"]} '
            print(f"{self.name}:\t\t * {random.randint(1,3)*typ}*")
    def pfote(self):
        if self.tricks["pfote"] == True:
            print(f"{self.name}:\t\t * pfote *")
        else:
            typ = f'{self.tricks["typ"]} '
            print(f"{self.name}:\t\t * {random.randint(1,3)*typ}*")
    def maennchen(self):
        if self.tricks["maennchen"] == True:
            print(f"{self.name}:\t\t * maennchen *")
        else:
            typ = f'{self.tricks["typ"]} '
            print(f"{self.name}:\t\t * {random.randint(1,3)*typ}*")

hund1 = Hund("Zafra", 12, "Wachtel", {"bellen": False})
print(f"Herrchen:\t {hund1.name}! Bellen!")
hund1.bellen()
print(f"Herrchen:\t {hund1.name}! Pfote!")
hund1.pfote()

print()

hund2 = Hund("Kiwi", 12, "Wachtel", {"pfote": False, "bellen": True, "typ": "wouuff"})
print(f"Herrchen:\t {hund2.name}! Bellen!")
hund2.bellen()
print(f"Herrchen:\t {hund2.name}! Pfote!")
hund2.pfote()

print()