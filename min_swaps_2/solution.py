#!/usr/bin/env python

import random

LIMIT=10

if __name__ == '__main__':
    arr = random.sample(xrange(1, LIMIT + 1), LIMIT)
    print arr
    checks = [x for x in [0] * LIMIT]
    print checks

    zeroes = filter(lambda x: x[1] == 0, enumerate(checks))
    zeroes_itr = iter(zeroes)
    t = None
    try:
        t = zeroes_itr.next()
    except StopIteration as no_mo:
        pass

    if t:
        pos = t[0]
        while checks[pos] == 0:
            checks[pos] = 1
            e = arr[pos]
            if e == pos + 1:
                print "arr[%s] == %s, nothing to do" % (pos, e)
                break

            print "arr[%s] is %s but belongs at position %s" % (pos, e, e - 1)
            pos = e - 1
        
    print checks
