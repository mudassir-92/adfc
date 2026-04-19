# all system args related things
import sys

import os # al operating system related things like creating folder

import  platform # to check whether we are running on window or linux or window

from adfc.addUtil.addMain import  addMain
from adfc.__about__ import __version__

def main():
    args=sys.argv[1:] # [0] is all about system path
    ## based on args implement all the things
    print(args)


args=sys.argv[1:] # [0] is all about system path
    ## based on args implement all the things

if(args[0]=='--help'):
    print("Hello from adfc")
elif(args[0]=='--version'):
    print("adfc",__version__)
elif(args[0]=='add'):
    addMain(args[1:]) # all nxt commands go to
elif(args[0]=='rollback'):
    print("rollback")


# print(args)