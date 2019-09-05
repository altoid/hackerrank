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

    global lettercounts

    lettercounts = {}

    for l in alphabet:
        lettercounts[l] = [0] * (len(s) + 1)

    i = 1
    ln = len(s)
    for k in s:
        # every time we see a letter, add 1 to lettercounts[k][i:]
        for j in xrange(i, ln + 1):
            lettercounts[k][j] += 1
        i += 1


def combinations(p):
    # p is an array of integers
    numerator = sum(p)
    denominator_arr = map(factorial, p)
    denominator = reduce(lambda x, y: x * y, denominator_arr)
    return factorial(numerator) / denominator


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

    answer = combinations(denominator)
    if len(odd_letters) > 0:
        answer *= len(odd_letters)
    answer %= 1000000007

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
