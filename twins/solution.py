#!/usr/bin/env python

import math
import unittest


def sieve(arr):
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

#sieve(arr)
#print filter(lambda x: x != 0, arr)

# segmented sieve:  for n large (e.g. 10 ** 9)
# work on subarrays of size at most 10 ** 7
# collect the primes from the first segment
# use those to sieve out primes in the next segment
# etc.
#
# for this problem, stop at the first segment whose right hand endpoint
# is bigger than m.


def roundup(a, b):
    """
    round up a to the nearest multiple of b
    """
    return ((a + b - 1) / b) * b


def segmented_sieve_helper(primes_so_far, left, right, segment_size):
    arr = [x for x in xrange(left, right)]

    # zero out 1
    if left == 0:
        arr[1] = 0

#    print arr

    # sieve out elements using primes collected from previous iterations
    for p in primes_so_far:
        if p * 2 > right:
            break

        # smallest multiple of p that is >= than max(left, p * 2)
        m = max(left, p * 2)
        r = roundup(m, p)

        for j in xrange(r, right, p):
            arr[j - left] = 0

    # now sieve out primes from arr using prime factors we don't have yet
    
    # find index of next prime in arr
    i = 0
    
    while i < segment_size and arr[i] < math.sqrt(right):
        while i < segment_size and arr[i] == 0:
            i += 1

        if i >= segment_size or arr[i] >= math.sqrt(right):
            break

        for j in xrange(arr[i] * 2, right, arr[i]):
            arr[j - left] = 0

        i += 1

    # new batch of primes
    primes_so_far += filter(lambda x: x != 0, arr)


def segmented_sieve(size, segment_size):
    i = 0
    collected_primes = []
    while i < size:
        segmented_sieve_helper(collected_primes, i, i + segment_size, segment_size)
        i += segment_size
    return collected_primes


class Tests(unittest.TestCase):
    def test1(self):
        size = 100
        segment_size = 10

        old_way = sieve([x for x in xrange(size)])
        new_way = segmented_sieve(size, segment_size)

        print old_way
        print new_way

        self.assertEqual(old_way, new_way)
