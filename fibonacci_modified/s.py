#!/usr/bin/env python

# maps n to the nth modfibo number

import unittest

cache = {
    1: 0,
    2: 1,
}


def modfibo(n):
    if n in cache:
        return cache[n]

    tmp = modfibo(n - 1)
    result = modfibo(n - 2) + tmp * tmp
    cache[n] = result
    return result


class MyTest(unittest.TestCase):

    def test1(self):
        print modfibo(1)
        print modfibo(7)
        print modfibo(11)
        print modfibo(20)

