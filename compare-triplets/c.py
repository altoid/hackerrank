#!/usr/bin/env python

import sys

def solve(a0, a1, a2, b0, b1, b2):
    a = [a0, a1, a2]
    b = [b0, b1, b2]

    z = zip(a, b)
    funcs = [
        lambda t: t[0] > t[1],
        lambda t: t[0] < t[1],
        ]

    return [len(filter(f, z)) for f in funcs]
    

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
