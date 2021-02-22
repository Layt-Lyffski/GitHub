'''
def make_class(x):
    class Dog:
        def __init__(self, name):
            self.name = name  
            def es(self):
                print("es")
            es(self)

        def print_value(self):
            print(x)

    return Dog

cls = make_class(10)
d = cls("Layt")  
d.print_value() # the value
print(d.name)  # The layt
'''

from queue import Queue as q 
import inspect
#print(inspect.getsource(q))

class Queue(q): 
    def __repr__(self):
        return f"Queue({self._qsize()})"

    def __add__(self, item):
            self.put(item)

    def __sub__(self, item):
            self.get()

qu = Queue()
qu + 9
qu + 23
qu + 8
qu - 32

print(qu)
x = qu._get()
print(x)


import colorama
from colorama import Fore, Back, Style

print(Fore.RED + "text estd")


