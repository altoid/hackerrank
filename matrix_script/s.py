#!/usr/bin/env python

import unittest
from pprint import pprint

if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])  # columns

    matrix = []

    for _ in xrange(n):
        matrix_item = raw_input()
        matrix.append(matrix_item)

    pprint(matrix)

    # no if statements allowed

    lines = [[row[i] for row in matrix] for i in xrange(m)]
    print lines

    l2 = [''.join(line) for line in lines]
    print l2

    l3 = ''.join(l2)
    print l3
