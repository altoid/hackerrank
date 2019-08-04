#!/usr/bin/env python

import re
from pprint import pprint
import unittest

def is_valid(n):
    if not (100000 <= n < 1000000):
        return False

    sn = str(n)

    if re.match(r'.*0.0', sn):
        return False

    if re.match(r'.*1.1', sn):
        return False

    if re.match(r'.*2.2', sn):
        return False

    if re.match(r'.*3.3', sn):
        return False

    if re.match(r'.*4.4', sn):
        return False

    if re.match(r'.*5.5', sn):
        return False

    if re.match(r'.*6.6', sn):
        return False

    if re.match(r'.*7.7', sn):
        return False

    if re.match(r'.*8.8', sn):
        return False

    if re.match(r'.*9.9', sn):
        return False

    return True


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
        self.assertFalse(is_valid(234151))
        self.assertFalse(is_valid(123432))
