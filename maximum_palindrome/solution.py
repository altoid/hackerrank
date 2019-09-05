#!/usr/bin/env python

# idea:  given the subrange, tally the letters in it.  a palindrome would consist
# optionally of letters which appear an even number of times, and optionally an additional letter that appears
# an odd number of times.
#
# suppose we have
#
# a 2
# b 4
# c 5
# d 1
# e 5
#
# we want max length palindromes, so we have to use all the letters that appear an even number of times, and every
# letter that appears the largest odd number of times.
#
# so we have   a1 b2 c2
# i.e. the number of unique strings we can get by scrambling abbcc
#
# which is 5!/(1!2!2!) == 120/(4) == 30
#
# and abbee, another 30.  so, 60.
#

import unittest
from pprint import pprint, pformat

# compute a 2d array of character counts.  arr[c][i] is the number of times character c appears in the substring
# that ends at index i, using 1-based indexing

lettercounts = {}
factorials = {}

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def factorial(n):
    if n in factorials:
        return factorials[n]

    if n == 0:
        result = 1
    elif n == 1:
        result = 1
    else:
        result = n * factorial(n - 1)

    factorials[n] = result
    return result


def range_lettercount(c, l, r):
    # give me the number of times letter c appears in the range l, r (inclusive).
    # l, r are 1-based
    return lettercounts[c][r] - lettercounts[c][l - 1]


def initialize(s):

    for l in alphabet:
        lettercounts[l] = [0] * (len(s) + 1)

    i = 1
    ln = len(s)
    for k in s:
        # every time we see a letter, add 1 to lettercounts[k][i:]
        for j in xrange(i, ln + 1):
            lettercounts[k][j] += 1
        i += 1


def answerQuery(l, r):
    # l, r are 1-based
    # Return the answer for this query modulo 1000000007

    lettercounts_range = {}
    # count the number of times each letter appears in the interval
    for k in alphabet:
        lettercounts_range[k] = range_lettercount(k, l, r)

    items = lettercounts_range.items()
    even_letters = filter(lambda x: x[1] % 2 == 0 and x[1] > 0, items)
    odd_letters = filter(lambda x: x[1] % 2 == 1, items)
    max_odd_value = max(odd_letters, key=lambda x: x[1])[1]
    max_odd_items = filter(lambda x: x[1] == max_odd_value, odd_letters)
    pprint(lettercounts_range)
    pprint(even_letters)
    pprint(odd_letters)
    print max_odd_value
    print max_odd_items
    max_odd_count = len(max_odd_items)
    print max_odd_count

    denominator = [x[1] / 2 for x in even_letters]
    denominator += [max_odd_value / 2]
    print denominator

    numerator = factorial(r - l + 1)
    denominator = [factorial(x) for x in denominator]

    print numerator
    print denominator
    denominator = reduce(lambda x, y: x * y, denominator)

    answer = numerator / denominator
    answer *= max_odd_count
    answer %= 1000000007

    print answer
    return answer


class MyTest(unittest.TestCase):

    def testInitialize(self):
        # w  h  a  t  h  a  t  h  g  o  d  w  r  o  u  g  h  t  j  j  j
        # 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21

        text = 'whathathgodwroughtjjj'
        initialize(text)
        #pprint(lettercounts)
        self.assertEqual(1, range_lettercount('h', 1, 4))
        self.assertEqual(2, range_lettercount('h', 2, 5))
        self.assertEqual(0, range_lettercount('z', 1, 4))
        self.assertEqual(2, range_lettercount('t', 7, 18))
        self.assertEqual(1, range_lettercount('t', 8, 18))
        self.assertEqual(0, range_lettercount('t', 1, 1))
        self.assertEqual(0, range_lettercount('t', 1, 3))
        self.assertEqual(1, range_lettercount('t', 1, 4))
        self.assertEqual(1, range_lettercount('t', 4, 5))

    def test_factorial(self):
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(720, factorial(6))

    def test_example(self):
        text = 'madamimadam'
        initialize(text)
        result = answerQuery(4, 7)
        self.assertEqual(2, result)

    def test_answerQuery(self):
        text = 'whathathgodwroughtjjj'
        initialize(text)
        print text[3:11]
        answerQuery(4, 11)