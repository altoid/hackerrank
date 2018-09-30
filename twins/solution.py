#!/usr/bin/env python

import math

SIZE = 100

LARGE = 10 ** 2
SEGMENT_SIZE = 10 ** 1


def sieve(arr):
    arr[0] = 0
    arr[1] = 0

    # find index of next prime in arr
    
    i = 0
    
    while i < math.sqrt(SIZE):
        while arr[i] == 0:
            i += 1
        
        for j in xrange(i * 2, SIZE, i):
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


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def roundup(a, b):
    """
    round up a to the nearest multiple of b
    """
    return ((a + b - 1) / b) * b


def segmented_sieve(primes_so_far, left, right):
    arr = [x for x in xrange(left, right)]

    # zero out 1
    if left == 0:
        arr[1] = 0

    print arr

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
    
    while i < SEGMENT_SIZE and arr[i] < math.sqrt(right):
        while i < SEGMENT_SIZE and arr[i] == 0:
            i += 1

        if i >= SEGMENT_SIZE or arr[i] < math.sqrt(right):
            break

        for j in xrange(arr[i] * 2, right, arr[i]):
            arr[j - left] = 0

        i += 1

    # new batch of primes
    primes_so_far += filter(lambda x: x != 0, arr)


i = 0
collected_primes = []
while i < LARGE:
    segmented_sieve(collected_primes, i, i + SEGMENT_SIZE)
    i += SEGMENT_SIZE

print "segmented_sieve: ", collected_primes

primes = sieve([x for x in xrange(SIZE)])

print "regular sieve: ", primes
