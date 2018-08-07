#!/usr/bin/env python

import fileinput


def worker(n):
#    print "worker: %s" % n
    if len(n) == 1:
        return n

    l = map(int, list(n))

    s = reduce(lambda x, y: x + y, l)

    return worker(str(s))


def superDigit(n, k):
    sd = int(worker(n)) * int(k)

    return worker(str(sd))

if __name__ == '__main__':
    fi = fileinput.FileInput()
    n, k = fi.readline().strip().split(' ')

    result = superDigit(n, k)
    print result


