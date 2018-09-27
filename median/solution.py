#!/usr/bin/env python

import fileinput
from pprint import pprint, pformat
import unittest


def findMedian(array):
    """
    find the median of an unsorted array.  the number of elements in the array is guaranteed to be
    odd.

    :param array:
    :return:
    """

    arr = sorted(array)
    return arr[len(arr) / 2]


class Tests(unittest.TestCase):
    def test1(self):
        arr = [1]
        a = 1
        split = locate(arr, a)
        self.assertEqual(-1, split)

        a = 0
        split = locate(arr, a)
        self.assertEqual(0, split)

    def test2(self):
        self.assertEqual(1, locate([2, 4, 6], 2))

    def test3(self):
        self.assertEqual(3, locate([2, 4, 4, 6], 4))

        arr = [2, 4, 4, 4, 6]
        self.assertEqual(0, locate(arr, 0))
        self.assertEqual(1, locate(arr, 2))
        self.assertEqual(4, locate(arr, 4))
        self.assertEqual(0, locate(arr, 0))
        self.assertEqual(-1, locate(arr, 7))

    def testFind(self):
        arr = [1, 7, 2, 4, 5, 1, 8, 0, 3]
        self.assertEqual(3, findMedian(arr))

        arr = [0, 1, 2, 4, 6, 5, 3]
        self.assertEqual(3, findMedian(arr))


if __name__ == '__main__':
    fi = fileinput.FileInput()
    count = int(fi.readline().strip())
    array = map(int, fi.readline().strip().split())
    result = findMedian(array)

    print result
