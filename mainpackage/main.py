#!/usr/bin/python

from aa import a
from bb import b
from cc import c
from dd import d

def main_func():
    print('\r\n we are in file-main.py \r\n')
    return 10


if __name__ == "__main__":
    print(main_func())
    print(a())
    print(b())
    print(c())
    print(d())
else :
    print('my __name__ is %s' % (__name__))
