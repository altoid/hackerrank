#!/usr/bin/env python

# https://www.hackerrank.com/challenges/encryption/problem

import unittest
import math


def encrypt(s):
    ss = s.replace(' ', '')

    sqrt = math.sqrt(len(ss))
    r = int(math.floor(sqrt))
    c = int(math.ceil(sqrt))

    print ss, r, c

    for i in xrange(c):
        print ss[i::c]

    trans = [ss[x::c] for x in xrange(c)]
    return ' '.join(trans)


class MyTest(unittest.TestCase):
    def test1(self):
        s = 'if man was meant to stay on the ground god would have given us roots'
        e = 'imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau'

        test = encrypt(s)
        self.assertEqual(e, test)
