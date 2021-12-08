#!/usr/bin/env python

# https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_r=internal-search

import unittest


def reducer(encoding, s_right):
    """
    :param encoding:
    :param s_right:  the part of s we haven't consumed yet
    :return:
    """
    if not s_right:
        return encoding

    c = s_right[0]
    if encoding and encoding[-1][0] == c:
        t = (c, encoding[-1][1] + 1)
        encoding.pop()
    else:
        t = (c, 1)

    encoding.append(t)
    return encoding


def run_length_encode(s):
    """
    given a string, produce a list containing tuples of (char, count).  example:

    mnonopoo ==> [(m 1) (n 1) (o 1) (n 1) (o 1) (p 1) (o 2)
    aaaabaaa ==> [(a 4) (b 1) (a 3)]
    :param s:
    :return:
    """
    return reduce(reducer, s, [])


def substrCount(ignore_me, s):
    e = run_length_encode(s)
    result = 0

    if len(e) == 0:
        return result

    n = e[0][1]
    result += n * (n + 1) / 2
    if len(e) == 1:
        return result

    n = e[-1][1]
    result += n * (n + 1) / 2

    for i in xrange(1, len(e) - 1):
        print e[i]
        n = e[i][1]
        result += n * (n + 1) / 2
        if n == 1 and e[i - 1][0] == e[i + 1][0]:
            pred_count = e[i - 1][1]
            succ_count = e[i + 1][1]
            result += min(pred_count, succ_count)

    return result


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(7, substrCount('asasd'))

    def test2(self):
        self.assertEqual(10, substrCount('abcbaba'))

    def test3(self):
        self.assertEqual(10, substrCount('aaaa'))

    def test4(self):
        self.assertEqual(0, substrCount(''))


def test(s):
    print s, run_length_encode(s)


if __name__ == '__main__':
    test('')
    test('mnonopoo')
    test('aaabaacaa')

