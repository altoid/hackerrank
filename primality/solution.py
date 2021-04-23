#!/usr/bin/env python

# https://www.hackerrank.com/challenges/ctci-big-o/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=miscellaneous

import fileinput
import math
import unittest


def isprime(p):
    # we know 1 <= p <= 10 ** 9

    if p == 1:
        return False

    if p == 2 or p == 3:
        return True

    if p % 2 == 0:
        return False

    if p % 3 == 0:
        return False

    sqt = math.sqrt(p)

    k = 5

    while k <= sqt:
        if p % (k + 2) == 0:
            return False

        if p % k == 0:
            return False

        k += 6

    return True


def primality(n):
    if isprime(n):
        return 'Prime'

    return 'Not prime'


class MyTest(unittest.TestCase):

    def test1(self):
        self.assertTrue(isprime(2))
        self.assertFalse(isprime(4))
        self.assertFalse(isprime(6))
        self.assertTrue(isprime(3))
        self.assertTrue(isprime(5))
        self.assertTrue(isprime(7))
        self.assertTrue(isprime(2))

        self.assertTrue(isprime(31))
        self.assertFalse(isprime(25))
        self.assertTrue(isprime(3514443767))


if __name__ == '__main__':
    fi = fileinput.FileInput()
    while True:
        line = fi.readline().strip()
        if not line:
            break

        if fi.isfirstline():
            continue

        print primality(int(line))

