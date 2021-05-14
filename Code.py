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
    elif I.startswith("*"):
        SP = I.split("* ")
        index = data['y'].index(str(SP[1]))
        print(data['x'][index])
    elif I.startswith('let'):
        SP = I.split(" ")
        data['x'].append(SP[1])
        data['y'].append(SP[2])
        with open("Js.json", "w+") as f:
            json.dump(data, f, indent=4)
    elif I.startswith('if'):
        SP = I.split(" ")
        SPP = SP[1].split("=")
        if SPP[0] in data['x']:
            if SPP[1] in data['y']:
                index = data['x'].index(SPP[0])
                X = data['x'][index]
                Y = data['y'][index]
                if X == SPP[0] and Y == SPP[1]:
                    if len(I) >= 15: 
                        if SP[2] == "return":
                            print(SP[3])
                    else:
                        print("True")
                else:
                    print("False")
            else:
                print("False")
        else:
            print("False")
    elif I.startswith('println'):
        SP = I.split(" ")
        print(SP[1])
    
universal()