#!/usr/bin/env python

import fileinput


def almostSorted(arr):
    left = None
    right = None
    interval = None
    for i in xrange(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            if interval:
                print 'no'
                return

            if left is None:
                left = i
            right = i + 1
        else:
            if left and right:
                interval = (left, right)

    if left is not None and right is not None and interval is None:
        interval = (left, right)

    if not interval:
        # no decreasing subsequences
        print 'yes'
        return

    # check if we are sorted after swap/reverse
    left, right = interval
    if left > 0:
        if arr[left - 1] > arr[right]:
            print 'no'
            return

    if right < len(arr) - 1:
        if arr[right + 1] < arr[left]:
            print 'no'
            return

    print 'yes'
    operation = 'reverse' if right - left > 1 else 'swap'
    print '%s %s %s' % (operation, left + 1, right + 1)


if __name__ == '__main__':
    fi = fileinput.FileInput()

    nelements = fi.readline()
    elements = map(int, fi.readline().split(' '))

    almostSorted(elements)