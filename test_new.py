#!/usr/bin/env python

from new import shrey_assert


def test_1():
    assert shrey_assert(1) == 1

def test_2():
    assert shrey_assert(0) == 0

def test_3():
    assert shrey_assert(-1) == 1#None #1
