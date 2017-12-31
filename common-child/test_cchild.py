#!/usr/bin/env python

import unittest
import cchild

import pprint

pp = pprint.PrettyPrinter(width=50)

class TestP(unittest.TestCase):

    def test_gen(self):
        strings = ['HSHINCHANA','HNOHARAANA']
        
        hash1 = cchild.build_hash(strings[0])
        hash2 = cchild.build_hash(strings[1])
        
        pp.pprint(hash1)
        pp.pprint(hash2)
        
        # get the set of common characters
        
        set1 = set(hash1.keys())
        set2 = set(hash2.keys())
        
        inter = set1 & set2
        
        pp.pprint(inter)
        
        for c in inter:
            print c, hash1[c], hash2[c]
        
        common_chars = [c for c in inter]

        g1 = cchild.gen(common_chars, hash1)
        pp.pprint(g1)

# test for 'children' with repeating letters
# e.g. 'YESTERDAY', 'YXXXDXXXY'
# e.g. 'YESTERDAY', 'YXXXYXXXD'  should show no matches.

# other test cases
# HANA HANNA - HANA
# AA BB - no matches
# AXBXCXDXE  OEODOCOBOAO  - no matches
# ABCDE AAAAABBBBBCCCCDDDDDDEEEE - ABCDE
