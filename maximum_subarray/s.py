#!/usr/bin/env python

import unittest

def max_subarray(arr):

    max_ending_here = max_so_far = arr[0]

    for a in arr[1:]:
        max_ending_here = max(a, max_ending_here + a)
        max_so_far = max(max_ending_here, max_so_far)

    return max_so_far

def max_subsequence(arr):

    max_ending_here = arr[0]
    for a in arr[1:]:
        max_ending_here = max(a, max_ending_here, max_ending_here + a)

    return max_ending_here

def maxSubarray(arr):
    return [max_subarray(arr), max_subsequence(arr)]

class MyTest(unittest.TestCase):

    def test1(self):
        arr = [2, -1, 2, 3, 4, -5]
        result = max_subarray(arr)
        self.assertEqual(10, result)

        result = max_subsequence(arr)
        self.assertEqual(11, result)
        
    def test2(self):
        arr = [2]
        result = max_subarray(arr)
        self.assertEqual(2, result)

        result = max_subsequence(arr)
        self.assertEqual(2, result)
                
    def test3(self):
        arr = [-1]
        result = max_subarray(arr)
        self.assertEqual(-1, result)

        result = max_subsequence(arr)
        self.assertEqual(-1, result)
                        
    def test4(self):
        arr = [-5, -4,-1,-2,-3]
        result = max_subarray(arr)
        self.assertEqual(-1, result)

        result = max_subsequence(arr)
        self.assertEqual(-1, result)
        
