#!/usr/bin/env python

import fileinput
import unittest


class Solution(object):
    def __init__(self, arr):
        self.left = [0] * len(arr)
        self.right = [0] * len(arr)
        self.arr = arr
        self.maxproduct = 0
        self.products = []
        if arr:
            self.lefts()
            self.rights()

            self.products = [a * b for a, b in zip(self.left, self.right)]
            self.maxproduct = max(self.products)

    def lefts(self):
        """
        compute left(i) for every element in arr
        left[0] == left[-len] == 0
        """
        lstack = [len(self.arr)]
        i = len(self.arr) - 1
        while i >= 0:
            if self.arr[i] <= self.arr[lstack[-1] - 1]:
                lstack.append(i + 1)
            else:
                while lstack and self.arr[i] > self.arr[lstack[-1] - 1]:
                    x = lstack.pop()
                    self.left[x - 1] = i + 1
                lstack.append(i + 1)
            i -= 1

    def rights(self):
        """
        compute right(i) for every element in arr
        right[len - 1] = 0

        create an empty stack
        put first element on it
        for each successive element
            if it is smaller than top of stack, put it on
            else pull everything off the stack that is smaller
            their rights are the index of the current element
            put current element on stack
        anything left on the stack has a right of 0
        """
        rstack = [1]
        i = 1
        while i < len(self.arr):
            if self.arr[i] <= self.arr[rstack[-1] - 1]:
                rstack.append(i + 1)
            else:
                while rstack and self.arr[i] > self.arr[rstack[-1] - 1]:
                    x = rstack.pop()
                    self.right[x - 1] = i + 1
                rstack.append(i + 1)
            i += 1


def solve(arr):
    if len(arr) < 3:
        return 0

    sol = Solution(arr)
    return sol.maxproduct


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
        self.assertEqual([2, 0], sol.right)

    def test_right_1(self):
        arr = [5, 4, 3, 2, 1, 6]
        sol = Solution(arr)
        self.assertEqual([6, 6, 6, 6, 6, 0], sol.right)

    def test_right_2(self):
        arr = [1, 2, 3, 4, 5, 6]
        sol = Solution(arr)
        self.assertEqual([2, 3, 4, 5, 6, 0], sol.right)

    def test_right_3(self):
        arr = [1, 1, 1, 1, 1, 6]
        sol = Solution(arr)
        self.assertEqual([6, 6, 6, 6, 6, 0], sol.right)

    def test_right_4(self):
        arr = [1, 2, 1, 3, 1, 4, 1, 5]
        sol = Solution(arr)
        self.assertEqual([2, 4, 4, 6, 6, 8, 8, 0], sol.right)

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
        self.assertEqual([0, 1, 1, 1, 1, 1], sol.left)

    def test_left_2(self):
        arr = [5, 6, 4, 3, 2, 1]
        sol = Solution(arr)
        self.assertEqual([0, 0, 2, 3, 4, 5], sol.left)

    def test_left_3(self):
        arr = [1, 6, 1, 1, 1, 1]
        sol = Solution(arr)
        self.assertEqual([0, 0, 2, 2, 2, 2], sol.left)

    def test_left_4(self):
        arr = [5, 1, 4, 1, 3, 1, 2, 1]
        sol = Solution(arr)
        self.assertEqual([0, 1, 1, 3, 3, 5, 5, 7], sol.left)

    ###

    def test_both_5(self):
        arr = [6, 2, 5, 3, 4, 1, 7]
        sol = Solution(arr)
        self.assertEqual([7, 3, 7, 5, 7, 7, 0], sol.right)
        self.assertEqual([0, 1, 1, 3, 3, 5, 0], sol.left)

    def test_both_6(self):
        arr = [6, 2, 5, 4, 5, 1, 6]
        sol = Solution(arr)
        self.assertEqual([0, 3, 7, 5, 7, 7, 0], sol.right)
        self.assertEqual([0, 1, 1, 3, 1, 5, 0], sol.left)

    def test_example(self):
        arr = [5, 4, 3, 4, 5]
        sol = Solution(arr)
        self.assertEqual([0, 5, 8, 5, 0], sol.products)
        self.assertEqual(8, sol.maxproduct)