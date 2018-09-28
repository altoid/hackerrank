#!/usr/bin/env python

def findit(n):
    i = 1
    while True:
        b = int(str(bin(i))[2:]) * 9
        if b % n == 0:
            return str(b)
        i += 1

longest = ''
for i in xrange(1, 501):
    r = findit(i)
    if len(r) > len(longest):
        longest = r
    print i, r

print longest

