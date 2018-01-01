#!/usr/bin/env python

import unittest
import isvalid

import pprint

pp = pprint.PrettyPrinter(width=50)

class TestIsValid(unittest.TestCase):

    def test_isvalid(self):
        # these are all valid
        self.assertTrue(isvalid.testValid("aabb"))
        self.assertTrue(isvalid.testValid("abcabc"))
        self.assertTrue(isvalid.testValid("abcabcd"))
        self.assertTrue(isvalid.testValid("abcdefgh"))
        self.assertTrue(isvalid.testValid("a"))
        self.assertTrue(isvalid.testValid("abcc"))

        # these are not valid
        self.assertFalse(isvalid.testValid("abababcd"))
        self.assertFalse(isvalid.testValid("abbcccdddd"))
