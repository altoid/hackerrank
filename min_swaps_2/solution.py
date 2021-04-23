#!/usr/bin/env python

import random
import fileinput

LIMIT = 10


def minimumSwaps(arr):
    # print arr
    checks = [0] * len(arr)
    # print checks
    total_swaps = 0

    nextpos = 0

    while nextpos < len(arr):
        # print "========== orbit"
        orbit_len = -1
        pos = nextpos
        while checks[pos] == 0:
            checks[pos] = 1
            orbit_len += 1
            e = arr[pos]
            if e == pos + 1:
                # print "arr[%s] == %s, nothing to do" % (pos, e)
                break

            # print "arr[%s] is %s but belongs at position %s" % (pos, e, e - 1)
            pos = e - 1

        # print checks, "orbit_len = %s" % orbit_len
        total_swaps += orbit_len

        while nextpos < len(arr) and checks[nextpos] == 1:
            nextpos += 1

    return total_swaps


if __name__ == '__main__':
    fi = fileinput.FileInput()
    nelements = map(int, fi.readline().strip().split(' '))
    elements = map(int, fi.readline().strip().split(' '))

    print minimumSwaps(elements)
