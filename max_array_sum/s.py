#!/usr/bin/env python

import unittest
from pprint import pprint


def subsets_helper(arr):
    yield [arr[0]]

    if len(arr) == 1:
        return

    for s in subsets_helper(arr[1:]):
        yield [arr[0]] + s

    for s in subsets_helper(arr[1:]):
        yield s


def subsets(arr):
    for s in subsets_helper(arr):
        yield tuple(s)

    yield ()


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
        arr = [3, 5, -7, 8, 10]
        self.assertEqual(15, solution(arr))

    def test5b(self):
        arr = [3, 7, 4, 6, 5]
        self.assertEqual(13, solution(arr))

    def test_file(self):
        with open('input00.txt') as f:
            f.readline()  # throw it away
            arr = list(map(int, f.readline().strip().split(' ')))
        self.assertEqual(151598486, solution(arr))


class SubsetTest(unittest.TestCase):

    def test1(self):
        print()
        arr = [1]
        for s in subsets(arr):
            print(s)

    def test2(self):
        print()
        arr = [1, 2]
        for s in subsets(arr):
            print(s)

    def test3(self):
        print()
        arr = [1, 2, 3]
        for s in subsets(arr):
            print(s)

    def test4(self):
        arr = [1, 2, 3, 4]
        expected = {(1,),
                    (1, 2),
                    (1, 2, 3),
                    (1, 2, 3, 4),
                    (1, 2, 4),
                    (1, 3),
                    (1, 3, 4),
                    (1, 4),
                    (2,),
                    (2, 3),
                    (2, 3, 4),
                    (2, 4),
                    (3,),
                    (3, 4),
                    (4,),
                    ()
                    }

        result = set(subsets(arr))
        self.assertEqual(expected, result)

    def test5(self):
        arr = [1, 2, 3, 4, 5]
        expected = {(1,),
                    (1, 2),
                    (1, 2, 3),
                    (1, 2, 3, 4),
                    (1, 2, 3, 4, 5),
                    (1, 2, 3, 5),
                    (1, 2, 4),
                    (1, 2, 4, 5),
                    (1, 2, 5),
                    (1, 3),
                    (1, 3, 4),
                    (1, 3, 4, 5),
                    (1, 3, 5),
                    (1, 4),
                    (1, 4, 5),
                    (1, 5),
                    (2, ),
                    (2, 3),
                    (2, 3, 4),
                    (2, 3, 4, 5),
                    (2, 3, 5),
                    (2, 4),
                    (2, 4, 5),
                    (2, 5),
                    (3, ),
                    (3, 4),
                    (3, 4, 5),
                    (3, 5),
                    (4, ),
                    (4, 5),
                    (5, ),
                    ()
                    }
        result = set(subsets(arr))
        self.assertEqual(expected, result)

    def test6(self):
        print()
        arr = [1, 2, 3, 4, 5, 6]
        for s in subsets(arr):
            print(s)

    def test7(self):
        print()
        arr = [1, 2, 3, 4, 5, 6, 7]
        for s in subsets(arr):
            print(s)
