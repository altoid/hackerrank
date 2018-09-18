#!/usr/bin/env python

import fileinput
from pprint import pprint, pformat
import unittest


def locate_helper(arr, a, b, e):
    # arr is a sorted array.  do a binary search to see where a should be located in arr so that arr remains sorted.

    if b >= e:
        return b

    # find the index of the smallest element in arr that is > a.

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

    for i in xrange(len(arr)):
        if arr[i] > a:
            return i
    return -1


def findMedian(array):
    """
    find the median of an unsorted array.  the number of elements in the array is guaranteed to be
    odd.

    :param array:
    :return:
    """

    if len(array) == 1:
        return array[0]

    left = []
    right = []

    for a in array:
        # invariants:
        # - left and right are both sorted
        # - len(left) - len(right) is 0 or 1
        if len(left) == 0:
            left.append(a)
            continue

        # stick it in the left.  scoot one over to the right if we have to
        split = locate(left, a)
        if split == -1:
            left.append(a)
        else:
            left = left[:split] + [a] + left[split:]

        if len(left) - len(right) > 1:
            pluck = left[-1]
            left = left[:-1]
            right = [pluck] + right

    return left[-1]


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


if __name__ == '__main__':
    fi = fileinput.FileInput()
    count = int(fi.readline().strip())
    array = map(int, fi.readline().strip().split())
    result = findMedian(array)

    print result
