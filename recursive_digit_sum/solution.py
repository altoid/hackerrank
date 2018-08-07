#!/usr/bin/env python

import fileinput


def worker(n):
    print "worker: %s" % n
    if len(n) == 1:
        return n

    l = map(int, list(n))

    s = reduce(lambda x, y: x + y, l)

    return worker(str(s))


def superDigit(n, k):
    bigga = ''
    for _ in xrange(int(k)):
        bigga += n

    return worker(bigga)

if __name__ == '__main__':
    fi = fileinput.FileInput()
    n, k = fi.readline().strip().split(' ')
    print n
    print k

    result = superDigit(n, k)
    print "result = %s" % result

