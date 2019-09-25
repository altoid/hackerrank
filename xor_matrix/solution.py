#!/usr/bin/env python

import unittest
import fileinput


def next_row(r):
    result = []
    for i in xrange(len(r) - 1):
        result.append(r[i] ^ r[i + 1])
    result.append(r[0] ^ r[len(r) - 1])
    return result


class MyTest(unittest.TestCase):
    def test1(self):
        counter = 1
        row = [6, 7, 1, 3, 9, 2,4,6,11,13,55,66,44,11,38,49]
        #row = [23,45, 55]
        print counter, row
        for i in xrange(128):
            row = next_row(row)
            counter += 1
            print counter, row
