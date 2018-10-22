#!/usr/bin/env python

import unittest
import fileinput


def solve(exp, modulus):
    result = 2
    for _ in xrange(exp):
        result = (result ** 2) % modulus

    return result


class Tests(unittest.TestCase):
    def test_case2(self):
        self.assertEqual(16, solve(290, 443))

    def test_extreme(self):
        print solve(1000000, 2699)