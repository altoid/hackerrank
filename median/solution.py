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
    if a < arr[m]: # arr[b] <= a <= arr[m - 1]
        e = m - 1
    else: # arr[m] <= a <= arr[e]
        b = m + 1
    return locate_helper(arr, a, b, e)


def locate(arr, a):
    return locate_helper(arr, a, 0, len(arr) - 1)


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

    pprint(array)
    return 0


class Tests(unittest.TestCase):
    def test1(self):
        arr = [1]
        a = 1
        split = locate(arr, a)
        self.assertEqual(0, split)

        a = 0
        split = locate(arr, a)
        self.assertEqual(0, split)

    def test2(self):
        arr = [2, 4, 6]

        # print locate(arr, 1)
        # print locate(arr, 2)
        # print locate(arr, 3)
        print locate(arr, 4)

        print locate([2,4,4,6], 4)
        print locate([2, 4, 4, 4, 6], 4)
        print locate([2, 4, 4, 4, 6], 7)


if __name__ == '__main__':
    fi = fileinput.FileInput()
    count = int(fi.readline().strip())
    array = map(int, fi.readline().strip().split())
    result = findMedian(array)

    print result
