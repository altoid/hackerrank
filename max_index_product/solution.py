#!/usr/bin/env python

import fileinput
import unittest


class Solution(object):
    def __init__(self, arr):
        self.left = [0] * len(arr)
        self.right = [0] * len(arr)
        self.arr = arr
        if arr:
            self.lefts()
            self.rights()

    def lefts(self):
        """
        compute left(i) for every element in arr
        left[0] == left[-len] == 0
        """
        i = len(self.arr) - 1
        halt = -1
        while True:
            right = i
            interval = [right, right]
            i -= 1
            while i > halt:
                if self.arr[i] > self.arr[right]:
                    break
                interval[0] = i
                i -= 1
            if i == halt:
                break

            # self.arr[i] > self.arr[right]
            interval[0] = i
            for j in xrange(interval[1], interval[0], -1):
                self.left[j] = interval[0]
    
    def rights(self):
        """
        compute right(i) for every element in arr
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

            # self.arr[i] > self.arr[left]
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

    ####
    
    def test_left_00(self):
        # trivial cases
        arr = []
        sol = Solution(arr)
        self.assertEqual([], sol.left)

    def test_left_01(self):
        # trivial cases
        arr = [1]
        sol = Solution(arr)
        self.assertEqual([0], sol.left)

    def test_left_02(self):
        # trivial cases
        arr = [2, 1]
        sol = Solution(arr)
        self.assertEqual([0, 1], sol.left)

    def test_left_1(self):
        arr = [6, 1, 2, 3, 4, 5]
        sol = Solution(arr)
        self.assertEqual([0, 0, 0, 0, 0, 0], sol.left)

    def test_left_2(self):
        arr = [5, 6, 4, 3, 2, 1]
        sol = Solution(arr)
        self.assertEqual([0, 0, 1, 2, 3, 4], sol.left)

    def test_left_3(self):
        arr = [1, 6, 1, 1, 1, 1]
        sol = Solution(arr)
        self.assertEqual([0, 0, 1, 1, 1, 1], sol.left)

    def test_left_4(self):
        arr = [5, 1, 4, 1, 3, 1, 2, 1]
        sol = Solution(arr)
        self.assertEqual([0, 0, 0, 2, 2, 4, 4, 6], sol.left)

