#!/usr/bin/env python

import unittest
from pprint import pprint

def subsets(arr):
    if len(arr) == 1:
        yield [arr[0]]
        return

    if len(arr) == 2:
        yield [arr[0]]
        yield [arr[1]]
        return

    yield [arr[0]]

    for s in subsets(arr[2:]):
        yield [arr[0]] + s

    for s in subsets(arr[1:]):
        yield s

class MyTest(unittest.TestCase):

    def test1(self):
        arr = [1]
        for s in subsets(arr):
            print s

    def test2(self):
        arr = [1,2]
        for s in subsets(arr):
            print s

    def test3(self):
        arr = [1,2, 3]
        for s in subsets(arr):
            print s

    def test4(self):
        arr = [1,2, 3, 4]
        for s in subsets(arr):
            print s

    def test5(self):
        arr = [1,2, 3, 4, 5]
        for s in subsets(arr):
            print s
