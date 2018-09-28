#!/usr/bin/env python

from __future__ import division

import fileinput
from pprint import pprint, pformat
import unittest
import heapq


def findMedian(array):
    """
    find the median of an unsorted array.  the number of elements in the array is guaranteed to be
    odd.

    :param array:
    :return:
    """

    arr = sorted(array)
    return arr[len(arr) / 2]


def continuous_median(array):
    # compute the median of each subarray [0 .. i]
    left_heap = []
    right_heap = []

    def current_median():
        ll = len(left_heap)
        lr = len(right_heap)

        if ll == 0:
            return None

        if lr == 0:
            return -left_heap[0]

        if (ll + lr) % 2 == 0:
            return (-left_heap[0] + right_heap[0]) / 2

        return -left_heap[0]

    for a in array:
        cm = current_median()
        if cm is None:
            heapq.heappush(left_heap, -a)
            continue

        if a > cm:
            heapq.heappush(right_heap, a)
        else:
            heapq.heappush(left_heap, -a)

        if len(right_heap) > len(left_heap):
            m = heapq.heappop(right_heap)
            heapq.heappush(left_heap, -m)
        elif len(left_heap) - len(right_heap) > 1:
            m = -heapq.heappop(left_heap)
            heapq.heappush(right_heap, m)

        print cm

    return current_median()


class Tests(unittest.TestCase):

    def testFind(self):
        arr = [1, 7, 2, 4, 5, 1, 8, 0, 3]
        self.assertEqual(3, findMedian(arr))

        arr = [0, 1, 2, 4, 6, 5, 3]
        self.assertEqual(3, findMedian(arr))

    def test_continuous(self):
        arr = [1, 7, 2, 4, 5, 1, 8, 0, 3]
        continuous_median(arr)

if __name__ == '__main__':
    fi = fileinput.FileInput()
    count = int(fi.readline().strip())
    array = map(int, fi.readline().strip().split())
    #result = findMedian(array)
    result = continuous_median(array)

    print result
