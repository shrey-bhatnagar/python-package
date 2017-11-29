#!/usr/bin/python

#from mainShrey.main import main
#from mainShrey.aa import a
#from mainShrey.bb import b
#from mainShrey.cc import c
#from mainShrey.dd import d
import mainpackage
from mainpackage import main_func
def new():
    print('\r\n we are in file-new.py \r\n')
    return 10

print(new())
print(main_func())
print(mainpackage.a())
print(mainpackage.b())
print(mainpackage.c())
print(mainpackage.d())

def shrey_assert(val):
    assert (val >= 0),"val is less than ZERO!"
    return val**val

shrey_assert(1)### negative value to raise assert


