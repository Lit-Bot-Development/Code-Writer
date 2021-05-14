import sys
import sysconfig
import time
import os
from os import system
import json

cls = lambda: system('cls')
cls()

with open("Js.json") as f:
    data = json.load(f)

def universal():
    I = input("<> ")
    if I.startswith('['):
        SP = I.split(" ")
        print(SP[0])
    elif I.startswith('#'):
        SP = I.split("# ")
        index = data['x'].index(str(SP[1]))
        print(data['y'][index])
    elif I.startswith('let'):
        SP = I.split(" ")
        data['x'].append(SP[1])
        data['y'].append(SP[2])
        with open("Js.json", "w+") as f:
            json.dump(data, f, indent=4)
        

    
universal()