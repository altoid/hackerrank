#!/usr/bin/env python

# look at first digit
# if second digit(s) are successor keep going
# if not
# look at first two digits
#
import unittest
import fileinput


def parse(s, n):
    # parse s as a number sequence using the first n characters as the initial value
    # return first number in sequence if beautiful, None otherwise

    initial = int(s[:n])
    rest = s[n:]
    successor = str(initial + 1)
    while rest.startswith(successor):
        rest = rest[len(successor):]
        successor = str(int(successor) + 1)
    if len(rest) == 0:
        return initial


def initial_value(s):
    # return first number in sequence if beautiful, None otherwise

    if not s:
        return None

    for i in xrange(1, (len(s) / 2) + 1):
        result = parse(s, i)
        if result:
            return result


if __name__ == '__main__':
    fi = fileinput.FileInput()

    nelements = fi.readline()
    for line in fi:
        l = line.strip()
        result = initial_value(l)
        if result:
            print "YES %s" % result
        else:
            print "NO"


class MyTest(unittest.TestCase):
    def testParse(self):
        self.assertIsNone(parse('1235', 1))
        self.assertEqual(11111, parse('1111111112', 5))

    def testNone(self):
        self.assertIsNone(initial_value(""))
        self.assertIsNone(initial_value(None))
        self.assertIsNone(initial_value('1235'))
        self.assertIsNone(initial_value('1'))
        self.assertIsNone(initial_value('11'))
        self.assertIsNone(initial_value('010203'))
        self.assertIsNone(initial_value('10203'))
        self.assertIsNone(initial_value('111111111211113111145'))

    def testPositive(self):
        self.assertEqual(1, initial_value('1234'))
        self.assertEqual(1001, initial_value('100110021003'))
        self.assertEqual(11111, initial_value('11111111121111311114'))
        self.assertEqual(97, initial_value('979899100101102'))

