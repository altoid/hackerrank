#!/usr/bin/env python

# maps n to the nth modfibo number

import unittest

def helper(n, cache):
    if n in cache:
        return cache[n]

    tmp = helper(n - 1, cache)
    result = helper(n - 2, cache) + tmp * tmp
    cache[n] = result
    return result

def fibonacciModified(t1, t2, n):

    cache = {
        1: t1,
        2: t2,
        }

    return helper(n, cache)


class MyTest(unittest.TestCase):

    def test1(self):
        self.assertEqual(5, fibonacciModified(0, 1, 5))

    def test2(self):
        print fibonacciModified(0, 1, 17)

