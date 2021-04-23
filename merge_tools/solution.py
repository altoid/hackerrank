#!/usr/bin/env python

# https://www.hackerrank.com/challenges/merge-the-tools/problem

import unittest
import fileinput


def unique_subsequence(s):
    seenit = {}
    result = []
    for c in s:
        if c not in seenit:
            seenit[c] = c
            result.append(c)
    return ''.join(result)


def merge_the_tools(s, k):
    """
    k | len(s)
    :param s:
    :param k:
    :return:
    """
    result = []
    for i in xrange(0, len(s), k):
        result.append(unique_subsequence(s[i:i+k]))

    for r in result:
        print r


class MyTest(unittest.TestCase):
    def test_subsequence_1(self):
        self.assertEqual('a', unique_subsequence('a'))
        self.assertEqual('a', unique_subsequence('aa'))
        self.assertEqual('a', unique_subsequence('aaa'))
        self.assertEqual('ab', unique_subsequence('aba'))
        self.assertEqual('ab', unique_subsequence('abaa'))
        self.assertEqual('ba', unique_subsequence('bbbbbaaaaa'))
        self.assertEqual('abcdefh', unique_subsequence('abcdeefh'))

    def test_splitstring(self):
        merge_the_tools('aabcaaada', 3)