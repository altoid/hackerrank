#!/usr/bin/env python

import fileinput


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


def substrCount(str):
    chars = list(str)
    print chars
    result = reduce(rfunc, chars, [])
    print result
    return 0


if __name__ == '__main__':
    fi = fileinput.FileInput()
    nchars = fi.readline().strip()
    str = fi.readline().strip()

    result = substrCount(str)