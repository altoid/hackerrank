#!/usr/bin/env python

import unittest


def isBalanced(s):

    bracket_stack = []
    twins = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    for c in s:
        if c in '{[(':
            bracket_stack.append(c)
        elif c in ')]}':
            if len(bracket_stack) == 0:
                return 'NO'

            if bracket_stack[-1] != twins[c]:
                return 'NO'

            bracket_stack.pop()

    if len(bracket_stack) == 0:
        return 'YES'

    return 'NO'


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual('YES', isBalanced('{[()]}'))

    def test2(self):
        self.assertEqual('YES', isBalanced('{{[[(())]]}}'))

    def test3(self):
        self.assertEqual('NO', isBalanced('{[(])}'))

    def test4(self):
        self.assertEqual('YES', isBalanced('[](){()}'))

    def test5(self):
        self.assertEqual('YES', isBalanced('({}([][]))[]()'))

    def test6(self):
        self.assertEqual('NO', isBalanced('}][}}(}][))]'))

    def test_trivial(self):
        self.assertEqual('YES', isBalanced(''))
        self.assertEqual('YES', isBalanced('()'))
        self.assertEqual('YES', isBalanced('[]'))
        self.assertEqual('YES', isBalanced('{}'))
