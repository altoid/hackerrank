#!/usr/bin/env python

import re
from pprint import pprint
import unittest

def is_valid(n):
    sn = str(n)

    re1 = r'^[1-9][0-9]{5}$'
    re2 = r'(?=(0.0)|(1.1)|(2.2)|(3.3)|(4.4)|(5.5)|(6.6)|(7.7)|(8.8)|(9.9))'

#    print re.findall(re2, sn)

    return re.match(re1, sn) and len(re.findall(re2, sn)) < 2


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertFalse(is_valid(100000))
        self.assertFalse(is_valid(999999))
        self.assertTrue(is_valid(123456))
        self.assertTrue(is_valid(123451))
        self.assertFalse(is_valid(1000000))
        self.assertFalse(is_valid(1))

    def test2(self):
        self.assertFalse(is_valid(101000))
        self.assertFalse(is_valid(010100))
        self.assertFalse(is_valid(001010))
        self.assertFalse(is_valid(000101))
        self.assertTrue(is_valid(234151))
        self.assertTrue(is_valid(123432))

    def test3(self):
        self.assertFalse(is_valid(4542867))
