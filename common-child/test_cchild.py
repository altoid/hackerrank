#!/usr/bin/env python

import unittest
import cchild

import pprint

pp = pprint.PrettyPrinter(width=50)

class TestP(unittest.TestCase):

    def test_lcs(self):
        self.assertEqual(3, cchild.lcs("SHINCHAN", "NOHARAAA"))

        self.assertEqual(0, cchild.lcs("AA", "BB"))
        self.assertEqual(0, cchild.lcs("AAAA", ""))
        self.assertEqual(3, cchild.lcs("YESTERDAY", "YXXDXXY"))

        self.assertEqual(2, cchild.lcs("YESTERDAY", "YXXYXXD"))
        self.assertEqual(2, cchild.lcs("HARRY", "SALLY"))

    def test_lcs_matrix(self):
        self.assertEqual(3, cchild.lcs_matrix("SHINCHAN", "NOHARAAA"))

        self.assertEqual(0, cchild.lcs_matrix("AA", "BB"))
        self.assertEqual(0, cchild.lcs_matrix("AAAA", ""))
        self.assertEqual(3, cchild.lcs_matrix("YESTERDAY", "YXXDXXY"))

        self.assertEqual(2, cchild.lcs_matrix("YESTERDAY", "YXXYXXD"))
        self.assertEqual(2, cchild.lcs_matrix("HARRY", "SALLY"))

