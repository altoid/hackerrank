#!/usr/bin/env python

import fileinput
import unittest


class Solution(object):
    def __init__(self, arr):
        self.left = [0] * len(arr)
        self.right = [0] * len(arr)
        self.arr = arr
        if arr:
            self.rights()

    def rights(self):
        """
        compute right(i) for every element in arr
        right[0] = 0
        right[len - 1] = 0
        """
        i = 0
        while True:
            left = i
            interval = [left, left]
            i += 1
            while i < len(self.arr):
                if self.arr[i] > self.arr[left]:
                    break
                interval[1] = i
                i += 1
            if i == len(self.arr):
                break

            # self.arr[i] > self.arr[l]
            interval[1] = i
            for j in xrange(interval[0], interval[1]):
                self.right[j] = interval[1]


def solve(arr):
    if len(arr) < 3:
        return 0

    return 0


class MyTest(unittest.TestCase):
    def test_right_00(self):
        # trivial cases
        arr = []
        sol = Solution(arr)
        self.assertEqual([], sol.right)

    def test_right_01(self):
        # trivial cases
        arr = [1]
        sol = Solution(arr)
        self.assertEqual([0], sol.right)

    def test_right_02(self):
        # trivial cases
        arr = [1, 2]
        sol = Solution(arr)
        self.assertEqual([1, 0], sol.right)

    def test_right_1(self):
        arr = [5, 4, 3, 2, 1, 6]
        sol = Solution(arr)
        self.assertEqual([5, 5, 5, 5, 5, 0], sol.right)

    def test_right_2(self):
        arr = [1, 2, 3, 4, 5, 6]
        sol = Solution(arr)
        self.assertEqual([1, 2, 3, 4, 5, 0], sol.right)

    def test_right_3(self):
        arr = [1, 1, 1, 1, 1, 6]
        sol = Solution(arr)
        self.assertEqual([5, 5, 5, 5, 5, 0], sol.right)

    def test_right_4(self):
        arr = [1, 2, 1, 3, 1, 4, 1, 5]
        sol = Solution(arr)
        self.assertEqual([1, 3, 3, 5, 5, 7, 7, 0], sol.right)

