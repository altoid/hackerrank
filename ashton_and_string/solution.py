#!/usr/bin/env python

import binary_search
from suffixtree import SuffixTree
import unittest

from pprint import pprint


def find_char_in_expansion_helper(stree, node, arc, acc, pos):
    label = stree.get_arc_label(arc)
    next_node = node.children[arc]
    if next_node.is_leaf():
        label = label[:-1]

    for i in xrange(len(label)):
        substring = acc + label[:i + 1]
        if 0 <= pos < len(substring):
            return pos, substring[pos]
        print substring
        pos -= len(substring)

    keys = sorted(next_node.children.keys(), key=lambda x: stree.text[x[0]])
    for arc in keys:
        pos, char = find_char_in_expansion_helper(stree, next_node, arc, acc + label, pos)
        if char is not None:
            return pos, char
    return pos, None


def find_char_in_expansion(stree, pos):
    keys = sorted(stree.root.children.keys(), key=lambda x: stree.text[x[0]])
    for arc in keys:
        pos, char = find_char_in_expansion_helper(stree, stree.root, arc, '', pos)
        if char is not None:
            return char


class MyTest(unittest.TestCase):
    def test_find_char_in_expansion(self):
        t = SuffixTree("mississippi")
        t.build_tree()
        self.assertEqual('i', find_char_in_expansion(t, 0))


if __name__ == '__main__':
    t = SuffixTree('mississippi')
    t.build_tree()
    t.show()
