#!/usr/bin/env python

import fileinput
from pprint import pprint


def rfunc(accum_value, c):
    if len(accum_value) == 0:
        return [(c, 1)]

    last = accum_value[-1]
    if last[0] == c:
        t = (last[0], last[1] + 1)
        accum_value.pop()
    else:
        t = (c, 1)

    accum_value.append(t)
    return accum_value


def substrCount(unused, str):
    chars = list(str)
    # print str, len(str)
    # print chars
    charcounts = reduce(rfunc, chars, [])

    # traverse the result.
    # if any char count is > 1, add n(n + 1)/2 to result
    # if any char count is 1, check preceding and following char.  if they are the same, add 1.
    pprint(charcounts)

    result = 0
    n = charcounts[0][1]
    result += n * (n + 1) / 2
    if len(charcounts) > 1:
        n = charcounts[-1][1]
        result += n * (n + 1) / 2

    # do it this way so we don't have to do a bounds check on every iteration
    for i in xrange(1, len(charcounts) - 1):
        # print charcounts[i]
        n = charcounts[i][1]
        result += n * (n + 1) / 2
        if n == 1:
            pred = charcounts[i - 1][0]
            succ = charcounts[i + 1][0]
            if pred == succ:
                predcount = charcounts[i - 1][1]
                succcount = charcounts[i + 1][1]
                result += min(predcount, succcount)

    return result


if __name__ == '__main__':
    fi = fileinput.FileInput()
    nchars = fi.readline().strip()
    str = fi.readline().strip()

    result = substrCount(nchars, str)
    print "result = %s" % result
