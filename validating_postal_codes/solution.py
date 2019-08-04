#!/usr/bin/env python

import re
from pprint import pprint
import unittest

def is_valid(n):
    sn = str(n)

    if not re.match(r'[1-9][0-9]{5}', sn):
        return False

    if re.match(r'.*([0-9]).\1', sn):
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
