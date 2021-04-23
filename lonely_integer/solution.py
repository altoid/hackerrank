#!/usr/bin/env python

import unittest


def findLonely(arr):
    return reduce(lambda x, y: x ^ y, arr)


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(4, findLonely([0,1,2,3,4,3,2,1,0]))
