#!/usr/bin/env python

import unittest


def chainLength(w, wordset, state):
    if w not in wordset:
        return 0

    if w not in state:
        if len(w) == 1:
            state[w] = 1

        else:
            max_substring_chain_length = 0
            for i in xrange(len(w)):
                substring = w[:i] + w[i + 1:]
                max_substring_chain_length = max(max_substring_chain_length, chainLength(substring, wordset, state))
            state[w] = max_substring_chain_length + 1

    return state[w]


def longestChain(words):
    wordset = set(words)
    state = {}
    max_chain_length = 0
    for w in words:
        max_chain_length = max(max_chain_length, chainLength(w, wordset, state))

    return max_chain_length


if __name__ == '__main__':
    s = 'aoeuidhtns'
    print s
    for i in xrange(len(s)):
        t = s[:i] + s[i + 1:]
        print t


class MyTest(unittest.TestCase):
    def test1(self):
        arr = ['a', 'b', 'ba', 'bca', 'bda', 'bdca']
        self.assertEqual(4, longestChain(arr))
