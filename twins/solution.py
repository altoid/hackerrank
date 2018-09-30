#!/usr/bin/env python

import unittest
import fileinput

import math

def simple_sieve(up_to):
    arr = [x for x in xrange(up_to + 1)]
    arr[0] = 0
    arr[1] = 0

    # find index of next prime in arr
    
    i = 0
    size = len(arr)
    while i < math.sqrt(size):
        while arr[i] == 0:
            i += 1
        
        for j in xrange(i * 2, size, i):
            arr[j] = 0
    
        i += 1

    return filter(lambda x: x != 0, arr)


def roundup(a, b):
    """
    round up a to the nearest multiple of b
    """
    return ((a + b - 1) / b) * b


def segmented_sieve(a, b):
    # gimme all primes in the interval [a, b]

    # keep caller from being a dick
    a, b = min(a, b), max(a, b)

    if a < 0 or b < 0:
        raise Exception("don't be a dick")

    # get all the primes up to sqrt(size) using simple sieve
    squirt = int(math.sqrt(b))
    if squirt == 1:
        squirt = b
    primes = simple_sieve(squirt)

    upto = b + 1  # want ranges to include b
    arr = [x for x in xrange(a, upto)]

    for p in primes:
        if p * 2 > b:
            break

        # smallest multiple of p that is >= than max(a, p * 2)
        m = max(a, p * 2)
        r = roundup(m, p)

        for j in xrange(r, upto, p):
            arr[j - a] = 0

    result = filter(lambda x: x > 1, arr)
    return result


def solve(n, m):
    # 1 <= n <= m <= 10 ** 9
    # m - n <= 10 ** 6

    result = 0
    if m - n > 1:
        primes = segmented_sieve(n, m)
        if len(primes) > 1:
            for i in xrange(len(primes) - 1):
                if primes[i + 1] - primes[i] == 2:
                    result += 1
    return result

if __name__ == '__main__':
    fi = fileinput.FileInput()
    n, m = map(int, fi.readline().strip().split(' '))
    result = solve(n, m)
    print result


class Tests(unittest.TestCase):

    def test_simple_sieve(self):
        primes = simple_sieve(3)
        self.assertEqual([2, 3], primes)

    def test1(self):
        size = 101

        old_way = simple_sieve(size)
        new_way = segmented_sieve(0, size)

        self.assertEqual(old_way, new_way)

    def test2(self):
        size = 10000

        old_way = simple_sieve(size)
        new_way = segmented_sieve(0, size)

        self.maxDiff = None
        self.assertEqual(old_way, new_way)

    # def test3(self):
    #     size = 10 ** 9
    #     primes = segmented_sieve(size - 10 ** 6, size)
    #     print len(primes)

    def test_range_is_1(self):
        primes = segmented_sieve(13, 13)
        self.assertEqual([13], primes)

        primes = segmented_sieve(12, 12)
        self.assertEqual([], primes)

    def test4(self):
        primes = segmented_sieve(0, 13)
        self.assertEqual([2, 3, 5, 7, 11, 13], primes)

    def test_sample0(self):
        result = solve(3, 13)
        self.assertEqual(3, result)

    def test_case_25(self):
        result = solve(3, 3)
        self.assertEqual(0, result)

    def test_case_27(self):
        result = solve(1, 1)
        self.assertEqual(0, result)
