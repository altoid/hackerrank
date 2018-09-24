#!/usr/bin/env python

import fileinput
import unittest

block_combos_cache = {}
all_walls_cache = {}
lego_blocks_cache = {}

MODULUS = 1000000007


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


def all_walls(h, w):
    t = tuple([h, w])
    if t not in all_walls_cache:
        result = block_combos(w) ** h
        all_walls_cache[t] = result
    return all_walls_cache[t]


def legoBlocks(h, w):
    t = tuple([h, w])
    if t not in lego_blocks_cache:
        if h == 1:
            result = 0 if w > 4 else 1
        elif w == 1:
            result = 1
        elif w == 2:
            result = 2 ** h - 1
        else:
            total = all_walls(h, w)
            s = 0
            for j in xrange(1, w):
                s += all_walls(h, w - j) * legoBlocks(h, j)
            result = total - s

        lego_blocks_cache[t] = result % MODULUS
    return lego_blocks_cache[t]


if __name__ == '__main__':
    fi = fileinput.FileInput()
    ncases = int(fi.readline().strip())
    for _ in xrange(ncases):
        h, w = map(int, fi.readline().strip().split())
        print legoBlocks(h, w)


class Tests(unittest.TestCase):

    def test_samples(self):
        self.assertEqual(1, legoBlocks(2, 1))
        self.assertEqual(3, legoBlocks(2, 2))
        self.assertEqual(7, legoBlocks(3, 2))
        self.assertEqual(9, legoBlocks(2, 3))

    def test_height_4(self):
        self.assertEqual(1, legoBlocks(4, 1))
        self.assertEqual(15, legoBlocks(4, 2))
        self.assertEqual(225, legoBlocks(4, 3))
        self.assertEqual(3375, legoBlocks(4, 4))
        self.assertEqual(35714, legoBlocks(4, 5))
        self.assertEqual(447902, legoBlocks(4, 6))
        self.assertEqual(5562914, legoBlocks(4, 7))

    def test_basis(self):
        self.assertEqual(1, legoBlocks(1, 1))
        self.assertEqual(1, legoBlocks(1, 3))
        self.assertEqual(0, legoBlocks(1, 5))

    def test_height_5(self):
        self.assertEqual(1, legoBlocks(5, 1))

    def test_height_8(self):
        self.assertEqual(402844528, legoBlocks(8, 6))

    def test_width_5(self):
        self.assertEqual(50, legoBlocks(2, 5))
        self.assertEqual(35714, legoBlocks(4, 5))
        self.assertEqual(908059021, legoBlocks(9, 5))

    def test_input01(self):
        self.assertEqual(27, legoBlocks(2, 4))
        self.assertEqual(122, legoBlocks(2, 6))

