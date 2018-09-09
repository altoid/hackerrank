#!/usr/bin/env python

import fileinput
from pprint import pprint, pformat


def arrayManipulation(n, queries):
    # queries is list of lists
    pprint(n)
    pprint(queries)

    return 0


if __name__ == '__main__':
    fi = fileinput.FileInput()
    nelements, nqueries = map(int, fi.readline().split(' '))
    queries = []
    for _ in xrange(nqueries):
        queries.append(map(int, fi.readline().split(' ')))

    result = arrayManipulation(nelements, queries)

    print result
