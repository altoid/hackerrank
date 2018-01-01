#!/usr/bin/env python

# https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

import pprint

pp = pprint.PrettyPrinter()


def testValid(s):
    d = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0,
        'e': 0,
        'f': 0,
        'g': 0,
        'h': 0,
        'i': 0,
        'j': 0,
        'k': 0,
        'l': 0,
        'm': 0,
        'n': 0,
        'o': 0,
        'p': 0,
        'q': 0,
        'r': 0,
        's': 0,
        't': 0,
        'u': 0,
        'v': 0,
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0,
    }

    for c in s:
        d[c] += 1

    # get the dict as items list and remove those with 0 counts
    i = d.items()
    i = filter(lambda x: x[1] > 0, i)
    # pp.pprint(i)

    # get the char counts as a list
    counts = sorted([x[1] for x in i])
    # print counts

    if len(counts) == 1:
        return True

    if counts[0] == counts[-1]:
        return True

    last = counts[-1]
    if counts[0] == counts[-2]:
        if last == counts[-2] + 1:
            return True

    if counts[0] == 1:
        return counts[1] == counts[-1]

    return False


def isValid(s):
    if testValid(s):
        print 'YES'
    else:
        print 'NO'

