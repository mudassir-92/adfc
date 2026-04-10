# all system args related things
import sys

import os # al operating system related things like creating folder

import  platform # to check whether we are running on window or linux or window

args=sys.argv[1:] # [0] is all about system path

# now command setup and full structure via setup

print(platform.system())

print(os.getcwd())

