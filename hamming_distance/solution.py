#!/usr/bin/env python

import unittest
import fileinput


# maps 0-255 to the number of bits in each of these numbers
bitcounts = {}


MASKWIDTH = 16
MASK = 2 ** MASKWIDTH - 1

def countbits_kernighan(n):
    """
    :param n: unsigned number
    :return: number of bits set in n
    """

    c = 0
    while n:
        c += 1
        n &= (n - 1)
    return c


def countbits_godawful(n):
    c = 0

    m1 = 0xffff
    m2 = m1 << 16
    m3 = m2 << 16
    m4 = m3 << 16

    while n:
        v1 = n & m1
        v2 = (n & m2) >> 16
        v3 = (n & m3) >> 32
        v4 = (n & m4) >> 48

        c += bitcounts[v1]
        c += bitcounts[v2]
        c += bitcounts[v3]
        c += bitcounts[v4]

        n >>= 64

    return c


def countbits(n):
    return countbits_godawful(n)


def hamming_distance(n1, n2):
    return countbits(n1 ^ n2)


def lyse(s, l, r):
    """
    split the string into 3 parts:
    1. left - the part to the left of the middle
    2. middle - the chars from l to r inclusive
    3. right - the part to the right of the middle

    left and right may be empty.  the middle never will be.

    :param s:
    :param l:
    :param r:
    :return:
    """

    left = s[:(l - 1)]
    middle = s[(l - 1):r]
    right = s[r:]

    return left, middle, right


def change(s, l, r, c):
    """
    in string s, change characters l through r into c.
    indexing is 1-based.

    string will never be ''
    """

    replacement_c = '0' if c == 'a' else '1'

    first, _, right = lyse(s, l, r)
    middle = replacement_c * (r - l + 1)
    return first + middle + right


def reverse(s, l, r):
    first, middle, right = lyse(s, l, r)
    return first + middle[::-1] + right


def swap(s, l1, r1, l2, r2):
    left_prefix, left_part, _ = lyse(s, l1, r1)
    _, right_part, right_suffix = lyse(s, l2, r2)
    middle = s[r1:(l2 - 1)]
    return left_prefix + right_part + middle + left_part + right_suffix


if __name__ == '__main__':

    for i in xrange(2 ** MASKWIDTH):
        bitcounts[i] = countbits_kernighan(i)

    fi = fileinput.FileInput()

    # throw away first line
    fi.readline()

    s = fi.readline().strip().replace('a', '0').replace('b', '1')
    s_int = int(s, base=2)

    # throw away next line
    fi.readline()

    # map length to mask
    masks = {}

    # now read the commands
    cmdline = fi.readline().strip()
    while cmdline:
        args = cmdline.split()
        cmd = args[0]
        rest = args[1:]

        if cmd == 'C':
            l = int(rest[0])
            r = int(rest[1])
            c = rest[2]
            s = change(s, l, r, c)
            s_int = int(s, base=2)

        elif cmd == 'S':
            l1 = int(rest[0])
            r1 = int(rest[1])
            l2 = int(rest[2])
            r2 = int(rest[3])
            s = swap(s, l1, r1, l2, r2)
            s_int = int(s, base=2)

        elif cmd == 'R':
            l = int(rest[0])
            r = int(rest[1])
            s = reverse(s, l, r)
            s_int = int(s, base=2)

        elif cmd == 'W':
            l = int(rest[0])
            r = int(rest[1])
            _, middle, _ = lyse(s, l, r)
            print middle.replace('0', 'a').replace('1', 'b')

        elif cmd == 'H':
            l1 = int(rest[0])
            l2 = int(rest[1])
            length = int(rest[2])
            len_s = len(s)

            if length not in masks:
                masks[length] = (1 << length) - 1
            mask = masks[length]

            n1 = (s_int >> (len_s - (l1 + length - 1))) & mask
            n2 = (s_int >> (len_s - (l2 + length - 1))) & mask

            d = hamming_distance(n1, n2)
            print d

        cmdline = fi.readline().strip()


class MyTest(unittest.TestCase):

    def test_swap(self):
        self.assertEqual('abcdLEFTxRIGHTdcba', swap('abcdRIGHTxLEFTdcba', 5, 9, 11, 14))
        self.assertEqual('LEFTRIGHT', swap('RIGHTLEFT', 1, 5, 6, 9))
        self.assertEqual('ab', swap('ba', 1, 1, 2, 2))

    def test_reverse(self):
        s = 'abcdLLATIKCUFefgh'
        self.assertEqual('abcdFUCKITALLefgh', reverse(s, 5, 13))

        s = 'LLATIKCUF'
        self.assertEqual('FUCKITALL', reverse(s, 1, 9))

    def test_lyse(self):
        s = 'CHEESE'
        first, middle, right = lyse(s, 1, 6)
        self.assertEqual('', first)
        self.assertEqual('CHEESE', middle)
        self.assertEqual('', right)

        first, middle, right = lyse(s, 3, 4)
        self.assertEqual('CH', first)
        self.assertEqual('EE', middle)
        self.assertEqual('SE', right)

    def test_change(self):
        self.assertEqual('aaaabbbbaaaa', change('aaaaaaaaaaaa', 5, 8, 'b'))

        self.assertEqual('b', change('a', 1, 1, 'b'))
        self.assertEqual('baaaa', change('aaaaa', 1, 1, 'b'))
        self.assertEqual('aabaa', change('aaaaa', 3, 3, 'b'))
        self.assertEqual('bbbbb', change('aaaaa', 1, 5, 'b'))

    def test_countbits(self):
        self.assertEqual(0, countbits(0))
        self.assertEqual(1, countbits(1))
        self.assertEqual(1, countbits(2))
        self.assertEqual(1, countbits(4))
        self.assertEqual(1, countbits(8))
        self.assertEqual(1, countbits(16))
        self.assertEqual(1, countbits(2 ** 5))
        self.assertEqual(1, countbits(2 ** 9))
        self.assertEqual(1, countbits(2 ** 111))

        self.assertEqual(2, countbits(2 ** 5 + 1))
        self.assertEqual(2, countbits(2 ** 9 + 2))
        self.assertEqual(2, countbits(2 ** 111 + 4))

        self.assertEqual(5, countbits(2 ** 5 - 1))
        self.assertEqual(9, countbits(2 ** 9 - 1))
        self.assertEqual(111, countbits(2 ** 111 - 1))

        self.assertEqual(3, countbits(2 ** 111 + 2 ** 9 + 2 ** 5))

