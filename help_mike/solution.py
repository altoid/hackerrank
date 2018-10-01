#!/usr/bin/env python

import unittest

def howmany(a, b):
    return (a + b - 1) / b

def get_summands(k):
    # maps i to k - i
    # for 1 <= i <= k/2
    summands = {}

    for i in xrange(1, (k / 2) + 1):
        summands[i] = k - i

    # for k even, do not put k/2 into the summands dict
    # because we will handle it as a special case

    if k % 2 == 0:
        summands.pop(k / 2, None)

    return summands

def get_cardinalities(n, k):
    # cardinalities of the equivalence classes
    # keys are 0 <= i < k
    cardinalities = {}

    # compute cardinalities of the equivalence classes
    for i in xrange(n - k, n + 1):
        cardinalities[i % k] = howmany(i, k)

    return cardinalities

def solve(n, k):
    # if k is 1, special case; answer is number of pairs with unique values
    if k == 1:
        return (n * (n - 1)) / 2
        
    cardinalities = get_cardinalities(n, k)
    summands = get_summands(k)

    total = 0
    for s in summands:
        total += (cardinalities[s] * cardinalities[k - s])

    # the 0 equivalence class
    x = cardinalities[0]
    total += ((x * (x - 1)) / 2)

    # for k even, do the same thing with k/2
    if k % 2 == 0:
        x = cardinalities[k / 2]
        total += ((x * (x - 1)) / 2)

    return total

class Tests(unittest.TestCase):
    def test_cards(self):
        c = get_cardinalities(10, 4)
        self.assertEqual({0: 2, 1: 3, 2: 3, 3: 2}, c)

        c = get_cardinalities(11, 4)
        self.assertEqual({0: 2, 1: 3, 2: 3, 3: 3}, c)

    def check_cards(self):
        # the sums of all the cardinalities has to be n.
        n, k = 21, 5
        c = get_cardinalities(n, k)
        self.assertEqual(n, sum(c.values()))

    def test_summands(self):
        s = get_summands(12)
        self.assertEqual({1: 11, 2: 10, 3: 9, 4: 8, 5: 7}, s)

        s = get_summands(13)
        self.assertEqual({1: 12, 2: 11, 3: 10, 4: 9, 5: 8, 6: 7}, s)

    def test_solve(self):
        self.assertEqual(10, solve(10, 4))
        self.assertEqual(7, solve(7, 3))
