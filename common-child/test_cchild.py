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

        print cchild.lcs_matrix("152741672952471503371792942072639098222725508481161772288133751962851942375223353394506129417815870530121062866406684144239359451518889569301486425933608023609120781961723349276451917271575096690163784969395254776909848099043148891445096557243720472871148112424705443720548124653139549112357089245983254523923",
                         "1447454686520439655139339327639007902691753599402564816602256079585609256441829219861384772102850641603007334069166176129594277403363871831439556060256543345509603765158700167156343409843454430764529739025039846212813161830174278930092644055194540961021516011720107241548729099078923039080308443008330473")

    def test_lcs_matrix(self):
        self.assertEqual(3, cchild.lcs_matrix("SHINCHAN", "NOHARAAA"))

        self.assertEqual(0, cchild.lcs_matrix("AA", "BB"))
        self.assertEqual(0, cchild.lcs_matrix("AAAA", ""))
        self.assertEqual(3, cchild.lcs_matrix("YESTERDAY", "YXXDXXY"))

        self.assertEqual(2, cchild.lcs_matrix("YESTERDAY", "YXXYXXD"))
        self.assertEqual(2, cchild.lcs_matrix("HARRY", "SALLY"))

