#!/usr/bin/env python

# idea:  given the subrange, tally the letters in it.  each half of the palindrome would consist of half of all of
# the letters that appear more than once, plus (in the middle) one letter that appears an odd number of times.
# for every letter that appears an odd number of times there is a different palindrome, where the middle letter is
# that odd-appearing letter.
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
import math

# compute a 2d array of character counts.  arr[c][i] is the number of times character c appears in the substring
# that ends at index i, using 1-based indexing

lettercounts = {}
factorials = {}
combos = {}
inverses = {}
alphabet = 'abcdefghijklmnopqrstuvwxyz'
MODULUS = 1000000007


def factorial(n):
    if n not in factorials:
        factorials[n] = math.factorial(n) % MODULUS

    return factorials[n]


def range_lettercount(c, l, r):
    # give me the number of times letter c appears in the range l, r (inclusive).
    # l, r are 1-based
    return lettercounts[c][r] - lettercounts[c][l - 1]


def initialize(s):

    global factorials

    factorials[0] = 1
    for i in xrange(1, 50000):
        factorials[i] = i * factorials[i - 1]

    global lettercounts
    local_lettercounts = {}

    for l in alphabet:
        local_lettercounts[l] = [0] * (len(s) + 1)

    letter_indices = {}
    i = 1
    for k in s:
        if k not in letter_indices:
            letter_indices[k] = []
        letter_indices[k].append(i)
        i += 1

#    pprint(letter_indices)
    for k in alphabet:
        if k not in letter_indices:
            continue

        indices = letter_indices[k]
        counter = 1
        l = 0
        while l < len(indices) - 1:
            for j in xrange(indices[l], indices[l + 1]):
                local_lettercounts[k][j] = counter
            counter += 1
            l += 1
        for j in xrange(indices[l], len(s) + 1):
            local_lettercounts[k][j] = counter

    lettercounts = local_lettercounts
#    pprint(lettercounts)
    #print "done initializing"


def power(x, n):
    result = 1
    while n:
        if n & 1:
            result = result * x % MODULUS

        x = x * x % MODULUS
        n >>= 1

    return result


def inverse(x):
    """

    :param x:
    :return: the multiplicative inverse of x modulo MODULUS
    """
    if x not in inverses:
        result = power(x, MODULUS - 2)
        inverses[x] = result

    return inverses[x]


def combinations(numerator, denominator):
    # p is an array of integers

    t = tuple(sorted(denominator))
    if t not in combos:
        temp_arr = map(lambda x: inverse(factorial(x)), t)
        result = reduce(lambda x, y: x * y, temp_arr)
        result = factorial(numerator) * result
        result %= MODULUS
        combos[t] = result

    return combos[t]


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

    denominator = [x[1] / 2 for x in even_letters] + [x[1] / 2 for x in odd_letters]
    numerator = sum(denominator)

    answer = combinations(numerator, denominator)
    if len(odd_letters) > 1:
        answer *= len(odd_letters)
        answer %= MODULUS

    return answer


if __name__ == '__main__':
    with open('output24.txt') as handle:
        answers = handle.read()
        answers = answers.split('\n')
        answers = [int(x.strip()) for x in answers]

    with open('input24.txt') as handle:
        text = handle.readline().strip()
        #print text
        initialize(text)
        handle.readline() # count
        counter = 0
        for line in handle:
            bounds = line.strip().split(' ')
            bounds = map(int, bounds)
            #print "[%s, %s]" % (bounds[0], bounds[1])
            answer = answerQuery(bounds[0], bounds[1])
            if answer != answers[counter]:
                print "mismatch:  got %s, expected %s, bounds [%s, %s]" % (
                    answer, answers[counter], bounds[0], bounds[1]
                )
                print "text = |%s|" % text[(bounds[0] - 1):bounds[1]]
            counter += 1

    print "done"


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

    def test_example_1(self):
        text = 'madamimadam'
        initialize(text)
        result = answerQuery(4, 7)
        self.assertEqual(2, result)

    def test_example_2(self):
        text = 'week'
        initialize(text)
        self.assertEqual(2, answerQuery(1, 4))
        self.assertEqual(1, answerQuery(2, 3))

    def test_another(self):
        text = 'abbccabbcc'
        initialize(text)
        self.assertEqual(30, answerQuery(1, 10))

    def test_answerQuery(self):
        text = 'whathathgodwroughtjjj'
        initialize(text)
        answerQuery(4, 11)

    def test_combinations(self):
        self.assertEqual(2, combinations([1, 1]))
        self.assertEqual(30, combinations([1, 2, 2]))
        self.assertEqual(60, combinations([1, 2, 3]))
        self.assertEqual(10, combinations([2, 3]))
        self.assertEqual(5, combinations([1, 4]))

    def test_1(self):
        text = 'daadabbadcabacbcccbdcccdbcccbbaadcbabbdaaaabbbdabdbbdcadaaacaadadacddabbbbbdcccbaabbbacacddbbbcbbdbd'
        initialize(text)
        self.assertEqual(2, answerQuery(14, 17))
        self.assertEqual(2, answerQuery(76, 79))
        self.assertEqual(2, answerQuery(16, 19))
        self.assertEqual(2, answerQuery(25, 28))
        self.assertEqual(2, answerQuery(44, 47))
