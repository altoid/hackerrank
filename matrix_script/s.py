#!/usr/bin/env python

import unittest
from pprint import pprint
import re

if __name__ == '__main__':

    nm = raw_input().split()

    n = int(nm[0])

    m = int(nm[1])  # columns

    matrix = []

    for _ in xrange(n):
        matrix_item = raw_input()
        matrix.append(matrix_item)

    pprint(matrix)

    # no if statements allowed

    lines = [[row[i] for row in matrix] for i in xrange(m)]
    print lines

    l2 = [''.join(line) for line in lines]
    print l2

    l3 = ''.join(l2)
    print l3

    # replace [' ' ! @ # $ % &]* with a single space when these occur between two alphanumeric characters.


class MyTest(unittest.TestCase):
    def setUp(self):
        self.pattern = r'(.*[A-Za-z])[ \!\@\#\$\%\&]+([A-Za-z])'
        self.pattern2 = r'([A-Za-z])[ \!\@\#\$\%\&]+([A-Za-z])'

    def test1(self):
        test = "A !@#$%&B"
        result = re.sub(self.pattern,
                        r'\1 \2',
                        test)
        self.assertEqual("A B", result)

    def test1_5(self):
        test = "A !@#$%&!@#$%&B"
        result = re.sub(self.pattern,
                        r'\1 \2',
                        test)
        self.assertEqual("A B", result)

    def test2(self):
        test = "A !@#$%&B !@#$%&C !@#$%&"
        print
        result = re.sub(self.pattern,
                        r'\1 \2',
                        test)
        print result
        result = re.sub(self.pattern2,
                        r'\1 \2',
                        result)
        print result
        self.assertEqual("A B C !@#$%&", result)

    def test3(self):
        test = "A B !@#$%&C !@#$%&"
        result = re.sub(self.pattern,
                        r'\1 \2',
                        test)
        self.assertEqual("A B C !@#$%&", result)
