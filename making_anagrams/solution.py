#!/usr/bin/env python

from pprint import pprint
import unittest
import fileinput


def char_counts(s):
    result = {}
    for c in s:
        if c not in result:
            result[c] = 0
        result[c] += 1

    return result


def makeAnagram(a, b):
    a_counts = char_counts(a)
    b_counts = char_counts(b)

    result = 0

    # remove all the chars not in both strings
    for a in a_counts.items():
        if a[0] not in b_counts:
            result += a[1]
        else:
            result += abs(b_counts[a[0]] - a_counts[a[0]])

    for b in b_counts.items():
        if b[0] not in a_counts:
            result += b[1]

    return result


if __name__ == '__main__':
    fi = fileinput.FileInput()
    s1 = fi.readline().strip()
    s2 = fi.readline().strip()

    print s1
    print s2
    print makeAnagram(s1, s2)


class MyTest(unittest.TestCase):
    def test0(self):
        d = char_counts('tumulus')

        i = d.items()
        del d['t']
        pprint(i)
        pprint(d)

    def test1(self):
        fi = fileinput.FileInput(files=('input/input00.txt'))
        s1 = fi.readline().strip()
        s2 = fi.readline().strip()

        self.assertEqual(4, makeAnagram(s1, s2))