#!/usr/bin/env python

import fileinput
from pprint import pprint, pformat
import unittest


def locate_helper(arr, a, b, e):
    if b >= e:
        return b

    # find the index of the smallest element in arr that is > a.
    # just find the index of a and scan rightward until we find
    # what we want.

    m = (b + e) / 2

    if a < arr[m]:  # arr[b] <= a <= arr[m - 1]
        e = m - 1
    else:  # arr[m] <= a <= arr[e]
        b = m + 1
    return locate_helper(arr, a, b, e)


def locate(arr, a):
    """

    :param arr:
    :param a:
    :return:  the index of the smallest element in arr that is > a.  if there is nothing larger than a in arr,
    return -1.
    """

    # for i in xrange(len(arr)):
    #     if arr[i] > a:
    #         return i
    # return -1

    if not arr:
        return -1

    if arr[-1] <= a:
        return -1

    split = locate_helper(arr, a, 0, len(arr) - 1)
    while arr[split] <= a:
        split += 1
    return split


def findMedian(array):
    """
    find the median of an unsorted array.  the number of elements in the array is guaranteed to be
    odd.

    :param array:
    :return:
    """

    if len(array) == 1:
        return array[0]

    scratch = []

    for a in array:
        split = locate(scratch, a)
        if split == -1:
            scratch.append(a)
        else:
            scratch = scratch[:split] + [a] + scratch[split:]

    return scratch[len(scratch) / 2]


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
