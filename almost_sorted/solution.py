#!/usr/bin/env python

import fileinput
from pprint import pprint, pformat


def almostSorted(arr):
    left = None
    right = None
    intervals = []
    for i in xrange(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if left is None:
                left = i
            right = i + 1
        else:
            if left is not None and right is not None:
                intervals.append(tuple([left, right]))
                left = None
                right = None

    if left is not None and right is not None:
        intervals.append(tuple([left, right]))

    # pprint(intervals)

    # we have every descending subsequence in the array.  deal with all the cases.
    if not intervals:
        # already sorted
        print 'yes'
        return

    if len(intervals) > 2:
        print 'no'
        return

    if len(intervals) == 1:
        interval = intervals[0]
        diff = interval[1] - interval[0]

        # have to make sure the swap/reverse preserves order
        if interval[1] < len(arr) - 1:
            l = arr[interval[0]]
            r = arr[interval[1] + 1]
            if l > r:
                print 'no'
                return

        if interval[0] > 0:
            l = arr[interval[0] - 1]
            r = arr[interval[1]]
            if l > r:
                print 'no'
                return

        print 'yes'
        operation = "reverse" if diff > 1 else "swap"
        print "%s %s %s" % (operation, interval[0] + 1, interval[1] + 1)
        return

    i0 = intervals[0]
    i1 = intervals[1]
    d0 = i0[1] - i0[0]
    d1 = i1[1] - i1[0]
    if d0 != 1 or d1 != 1:
        print 'no'
        return

    # if this is truly a swap condition, then the first interval will be a bump and the second will be a dip.
    # swap the first value pointed to by the first interval and the second
    # value pointed to by the second interval

    left_value = arr[i1[1]]
    right_value = arr[i0[0]]
    left_is_good = False
    right_is_good = False

    if i0[0] > 0:
        l = arr[i0[0] - 1]
        m = left_value
        r = arr[i0[1]]
        if l < m < r:
            left_is_good = True
    else:
        m = left_value
        r = arr[i0[1]]
        if m < r:
            left_is_good = True

    if i1[1] < len(arr) - 1:
        l = arr[i1[0]]
        m = right_value
        r = arr[i1[1] + 1]
        if l < m < r:
            right_is_good = True
    else:
        l = arr[i1[0]]
        m = right_value
        if l < m:
            right_is_good = True

    if left_is_good and right_is_good:
        print 'yes'
        print 'swap %s %s' % (i0[0] + 1, i1[1] + 1)
        return

    print 'no'


if __name__ == '__main__':
    fi = fileinput.FileInput()

    nelements = fi.readline()
    elements = map(int, fi.readline().split(' '))

    almostSorted(elements)