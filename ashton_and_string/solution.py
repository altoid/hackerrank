#!/usr/bin/env python

import binary_search
from suffixtree import SuffixTree
import unittest

from pprint import pprint

MAX_LEN = 101
triangle_numbers = [0] * MAX_LEN


def initialize():
    global triangle_numbers
    triangle_numbers[0] = 0
    for i in xrange(1, MAX_LEN):
        triangle_numbers[i] = i + triangle_numbers[i - 1]


def prefix_expansion_length(stree, node, arc, acc):
    """
    for a node and an arc out of that node, give me the length of the prefix expansion through that arc.

    i.e. in the suffix tree for 'mississippi',

    prefix_expansion_length(root, (8, 8))

    is 8

    because the prefix expansion along that path is

    p
    pi
    pp
    ppi

    ignoring any $ markers.

    :param node:
    :param arc:
    :return:
    """

    next_node = node.children[arc]
    l = stree.arc_length(arc)
    if next_node.is_leaf():
        l -= 1   # lop off the $

    result = l * (l + 1) / 2 + acc * l
    acc += l
    for c in next_node.children.keys():
        result += prefix_expansion_length(stree, next_node, c, acc)
    return result


def substring_expansion_length(stree):
    """
    return the sum of the lengths of every unique substring of the text.
    :return:
    """

    total = 0
    for c in stree.root.children.keys():
        total += prefix_expansion_length(stree, stree.root, c, 0)
    return total


class MyTest(unittest.TestCase):
    def test_empty_tree(self):
        # make sure that we can build, traverse, show, and search a suffix tree constructed with the empty string.

        empty = SuffixTree("")
        empty.show()
        all_suffixes = [x for x in empty.suffixes()]
        self.assertEqual(1, len(all_suffixes))
        self.assertEqual(0, substring_expansion_length(empty))

    def test_prefix_expansion_length_commodore(self):
        t = SuffixTree("commodore")
        t.build_tree()
        self.assertEqual(10, prefix_expansion_length(t, t.root, (5, 9), 0))
        self.assertEqual(45, prefix_expansion_length(t, t.root, (0, 9), 0))
        self.assertEqual(55, prefix_expansion_length(t, t.root, (1, 1), 0))
        self.assertEqual(48, prefix_expansion_length(t, t.root, (2, 2), 0))

    def test_prefix_expansion_length_mississippi(self):
        t = SuffixTree("mississippi")
        t.build_tree()

        self.assertEqual(66, prefix_expansion_length(t, t.root, (0, 11), 0))
        self.assertEqual(0, prefix_expansion_length(t, t.root, (11, 11), 0))
        self.assertEqual(8, prefix_expansion_length(t, t.root, (8, 8), 0))
        self.assertEqual(82, prefix_expansion_length(t, t.root, (1, 1), 0))
        self.assertEqual(107, prefix_expansion_length(t, t.root, (2, 2), 0))

    def test_substring_expansion_length_mississippi(self):
        t = SuffixTree("mississippi")
        t.build_tree()
        self.assertEqual(263, substring_expansion_length(t))


if __name__ == '__main__':
    initialize()
    pprint(triangle_numbers)

    t = SuffixTree('mississippi')
    t.build_tree()
    t.show()
