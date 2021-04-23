#!/usr/bin/env python

# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

import unittest

def maxMin(k, arr):
    sarr = sorted(arr)
    return min([sarr[i + k - 1] - sarr[i] for i in xrange(len(arr) - (k - 1))])


class MyTest(unittest.TestCase):
    def test1(self):
        arr = [10, 100, 300, 200, 1000, 20, 30]
        k = 3
        self.assertEqual(20, maxMin(k, arr))

    def test2(self):
        arr = [1, 2, 3, 4, 10, 20, 30, 40, 100, 200]
        k = 4
        self.assertEqual(3, maxMin(k, arr))

    def test3(self):
        arr = [1, 1, 1, 2, 2]
        k = 2
        self.assertEqual(0, maxMin(k, arr))

