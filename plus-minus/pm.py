#!/usr/bin/env python

import sys

def plusMinus(arr):
    filters = [
        lambda x: x > 0,
        lambda x: x < 0,
        lambda x: x == 0,
        ]

    d = float(len(arr))

    for x in [len(filter(f, arr)) / d for f in filters]:
        print x


if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))
    plusMinus(arr)
