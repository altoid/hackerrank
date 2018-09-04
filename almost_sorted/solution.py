#!/usr/bin/env python

import fileinput


def check_swap(arr):
    # len(arr) > 2
    toobig = []
    toosmall = []
    if arr[0] > arr[1]:
        toobig.append(0)
    if arr[-2] > arr[-1]:
        toosmall.append(len(arr) - 1)

    for i in xrange(1, len(arr) - 1):
        l = arr[i - 1]
        m = arr[i]
        r = arr[i + 1]
        if l > r:
            return
        if m < l:
            toosmall.append(i)
            continue

        if m > r:
            toobig.append(i)
            continue

    if len(toobig) != 1:
        return

    if len(toosmall) != 1:
        return

    # see if swapping preserves order
    left = toobig[0]
    right = toosmall[0]
    leftisgood = False
    rightisgood = False
    if left > 0:
        l = arr[left - 1]
        m = arr[right]
        r = arr[left + 1]
        if l < m < r:
            leftisgood = True
    else:
        m = arr[right]
        r = arr[left + 1]
        if m < r:
            leftisgood = True

    if right < len(arr) - 1:
        l = arr[right - 1]
        m = arr[left]
        r = arr[right + 1]
        if l < m < r:
            rightisgood = True
    else:
        l = arr[right - 1]
        m = arr[left]
        if m < r:
            rightisgood = True

    if leftisgood and rightisgood:
        return "swap %s and %s" % (left, right)


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
            if left is not None and right is not None:
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