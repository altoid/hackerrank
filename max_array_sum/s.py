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

def solution(arr):
    max_sum = None

    for s in subsets(arr):
        current_sum = sum(s)
        if max_sum is None:
            max_sum = current_sum

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

class SumTest(unittest.TestCase):
    def test1(self):
        arr = [3,5,-7,8,10]
        self.assertEqual(15, solution(arr))

    def test2(self):
        arr = [3,7,4,6,5]
        self.assertEqual(13, solution(arr))

    def test3(self):
        with open('input00.txt') as f:
            f.readline()  # throw it away
            arr = map(int, f.readline().strip().split(' '))
        print arr[0]
        print len(arr)
        self.assertEqual(151598486, solution(arr))

class SubsetTest(unittest.TestCase):

    def test1(self):
        print
        arr = [1]
        for s in subsets(arr):
            print s

    def test2(self):
        print
        arr = [1,2]
        for s in subsets(arr):
            print s

    def test3(self):
        print
        arr = [1,2, 3]
        for s in subsets(arr):
            print s

    def test4(self):
        print
        arr = [1,2, 3, 4]
        for s in subsets(arr):
            print s

    def test5(self):
        print
        arr = [1,2, 3, 4, 5]
        for s in subsets(arr):
            print s

    def test6(self):
        print
        arr = [1,2, 3, 4, 5, 6]
        for s in subsets(arr):
            print s

    def test7(self):
        print
        arr = [1,2, 3, 4, 5, 6, 7]
        for s in subsets(arr):
            print s
