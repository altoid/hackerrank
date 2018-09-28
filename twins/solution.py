#!/usr/bin/env python

import math

SIZE = 100

arr = [x for x in xrange(SIZE)]

def sieve(arr):
    arr[0] = 0
    arr[1] = 0
    
    # find index of next prime in arr
    
    i = 0
    
    while i < math.sqrt(SIZE):
        while arr[i] == 0:
            i += 1
        
        print arr[i]
        
        for j in xrange(i * 2, SIZE, i):
            arr[j] = 0
    
        i += 1

sieve(arr)
print arr
