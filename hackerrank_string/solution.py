#!/usr/bin/env python

import unittest


def solution(lookfor, lookhere):
    i = 0
    for c in lookhere:
        if c == lookfor[i]:
            i += 1
            if i == len(lookfor):
                break
    return i == len(lookfor)


if __name__ == '__main__':
    handle = open('input01')

    l = handle.readline()
    for line in handle:
        l = line.strip()
        print 'YES' if solution('hackerrank', l) else 'NO'


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertTrue(solution('hackerrank', 'hereiamstackerrank'))
        self.assertFalse(solution('hackerrank', 'hackerworld'))
