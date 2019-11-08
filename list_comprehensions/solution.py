#!/usr/bin/env python

import unittest
import fileinput


def coordinates(x, y, z, n):
    """
    return a list of all 3-tuples (i, j, k) such that:

    0 <= i <= x
    0 <= j <= y
    0 <= k <= z

    i + j + k != n

    :param x:
    :param y:
    :param z:
    :param n:
    :return:
    """

    return [[i, j, k] for i in xrange(x + 1) for j in xrange(y + 1) for k in xrange(z + 1) if i + j + k != n]


if __name__ == '__main__':
    fi = fileinput.FileInput()
    x = int(fi.readline().strip)
    y = int(fi.readline().strip)
    z = int(fi.readline().strip)
    n = int(fi.readline().strip)

    print coordinates(x, y, z, n)


class MyTest(unittest.TestCase):
    def test1(self):
        coordinates(2, 3, 4, 4)
