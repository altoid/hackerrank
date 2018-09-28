#!/usr/bin/env python

import math

SIZE = 10000

arr = [x for x in xrange(SIZE)]

def sieve(arr):
    arr[0] = 0
    arr[1] = 0
    primes = []

    # find index of next prime in arr
    
    i = 0
    
    while i < math.sqrt(SIZE):
        while arr[i] == 0:
            i += 1
        
        primes.append(i)
        
        for j in xrange(i * 2, SIZE, i):
            arr[j] = 0
    
        i += 1

    print primes

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

LARGE = 10 ** 3
SEGMENT_SIZE = 10 ** 2

def segmented_sieve(arr, primes_so_far, left, right):
    arr = [x for x in xrange(left, right)]
    print arr[0], arr[SEGMENT_SIZE - 1]

i = 0
while i < LARGE:
    segmented_sieve([], [], i, i + SEGMENT_SIZE)
    i += SEGMENT_SIZE
