#!/usr/bin/env python

import fileinput
import unittest

block_combos_cache = {}


def block_combos(w):
    # return the number of ways to build one row

    if w < 1:
        raise Exception("now stop that (width == %s)" % w)

    if w not in block_combos_cache:
        if w == 1:
            result = 1
        elif w == 2:
            result = 1 + block_combos(w - 1)
        elif w == 3:
            result = 1 + block_combos(w - 1) + block_combos(w - 2)
        elif w == 4:
            result = 1 + block_combos(w - 1) + block_combos(w - 2) + block_combos(w - 3)
        else:
            result = block_combos(w - 1) + block_combos(w - 2) + block_combos(w - 3) + block_combos(w - 4)

        block_combos_cache[w] = result

    return block_combos_cache[w]


def legoBlocks(h, w):
    if h == 1:
        if w > 4:
            return 0
        return 1

    total = block_combos(w) ** h
    sign = -1 if w > 1 else 0
    for i in xrange(1, w - 1):
        addend = (w - 1) * (2 ** (h * (w - 1 - i)))
        addend *= sign
        total += addend
        sign = -sign

    total += sign * 1

    return total % 1000000007


if __name__ == '__main__':
    fi = fileinput.FileInput()
    ncases = int(fi.readline().strip())
    for _ in xrange(ncases):
        h, w = map(int, fi.readline().strip().split())
        print legoBlocks(h, w)


class Tests(unittest.TestCase):

    # def test1(self):
    #     for i in xrange(1, 1000):
    #         print i, block_combos(i)

    def test_samples(self):
        self.assertEqual(3, legoBlocks(2, 2))
        self.assertEqual(7, legoBlocks(3, 2))
        self.assertEqual(9, legoBlocks(2, 3))
        self.assertEqual(3375, legoBlocks(4, 4))

    def test_basis(self):
        self.assertEqual(1, legoBlocks(1, 1))
        self.assertEqual(1, legoBlocks(1, 3))
        self.assertEqual(0, legoBlocks(1, 5))

        self.assertEqual(1, legoBlocks(5, 1))
