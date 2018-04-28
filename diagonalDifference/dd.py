#!/usr/bin/env python

import sys

def diagonalDifference(a):
    n = len(a)
    d1 = reduce(lambda a, x: a + x, [a[i][i] for i in xrange(n)])
    d2 = reduce(lambda a, x: a + x, [a[n - 1 - i][i] for i in xrange(n)])
    return abs(d1 - d2)

if __name__ == "__main__":
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int,raw_input().strip().split(' '))
        a.append(a_temp)
    result = diagonalDifference(a)
    print result
