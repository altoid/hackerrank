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
    # assumes there is at least 1 element in the array

    current_max = arr[0]
    if len(arr) == 1:
        return current_max

    back1 = current_max
    current_max = max(back1, arr[1])

    if len(arr) == 2:
        return current_max

    abs_max = current_max
    for a in arr[2:]:
        back2 = back1
        back1 = current_max
        current_max = max(a, a + back2, back1)
        abs_max = max(abs_max, current_max)

    return abs_max

class SumTest(unittest.TestCase):
    def test1(self):
        arr = [3]
        self.assertEqual(3, solution(arr))

    def test2(self):
        arr = [3, 4]
        self.assertEqual(4, solution(arr))

    def test3(self):
        arr = [3, 4, 5]
        self.assertEqual(8, solution(arr))

    def test5a(self):
        arr = [3,5,-7,8,10]
        self.assertEqual(15, solution(arr))

    def test5b(self):
        arr = [3,7,4,6,5]
        self.assertEqual(13, solution(arr))

    def test_file(self):
        with open('input00.txt') as f:
            f.readline()  # throw it away
            arr = map(int, f.readline().strip().split(' '))
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
