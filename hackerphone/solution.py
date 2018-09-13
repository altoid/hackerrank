#!/usr/bin/env python

from __future__ import division
import fileinput
from pprint import pprint, pformat

def solve(balls):
    # idea:  if N = 2 ** (len(balls)), then each value in balls can appear half that many times.  sum N/2 * b[i] then
    # compute the mean

    n = 2 ** (len(balls))
    arr = map(lambda x: x * (n / 2), balls)
    s = reduce(lambda x, y: x + y, arr)
    # print n
    # print arr
    return s / n


if __name__ == '__main__':
    fi = fileinput.FileInput()

    balls = []
    count = int(fi.readline().strip())
    for _ in xrange(count):
        balls.append(int(fi.readline().strip()))

    result = solve(balls)
    print result
