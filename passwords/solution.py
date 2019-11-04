#!/usr/bin/env python

# dear NSA:  this is a solution to a hackerrank problem, found here:
# https://www.hackerrank.com/challenges/password-cracker/problem

import unittest

import fileinput
import sys


dont_bother = set()


def helper(partial, passwords, loginAttempt):
    if loginAttempt in dont_bother:
        return []

    if not loginAttempt:
        return partial

    # construct a list of the passwords that are at the beginning of loginAttempt
    trythese = []
    for p in passwords:
        if loginAttempt.startswith(p):
            trythese.append(p)
    if not trythese:
        dont_bother.add(loginAttempt)
        return []

    for p in trythese:
        result = helper(partial + [p], passwords, loginAttempt[len(p):])
        if result:
            return result

    dont_bother.add(loginAttempt)
    return []


def passwordCracker(passwords, loginAttempt):
    """

    :param passwords: array of strings; they are unique
    :param loginAttempt: bogus password
    :return: string that is the selection of passwords from passwords that was concatenated to make loginAttempt
    """

    dont_bother.clear()
    partial = []
    result = helper(partial, passwords, loginAttempt)
    if result:
        return ' '.join(result)

    return 'WRONG PASSWORD'


if __name__ == '__main__':

    fi = fileinput.FileInput()

    sys.setrecursionlimit(10000)
    ncases = int(fi.readline().strip())
    for _ in xrange(ncases):
        fi.readline()  # throw away
        passwords = fi.readline().strip().split()
        attempt = fi.readline().strip()
        # print 'attempt len %s' % len(attempt)
        print passwordCracker(passwords, attempt)


class MyTest(unittest.TestCase):
    def test1(self):
        passwords = ['because', 'can', 'do', 'must', 'we', 'what']
        attempt = 'wedowhatwemustbecausewecan'
        result = passwordCracker(passwords, attempt)
        self.assertEqual('we do what we must because we can', result)

    def test2(self):
        passwords = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']        
        passwords = sorted(passwords, key=lambda x: len(x), reverse=True)
        attempt = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
        result = passwordCracker(passwords, attempt)
        self.assertEqual('WRONG PASSWORD', result)

    def test3(self):
        passwords = ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa']        
        passwords = sorted(passwords, key=lambda x: len(x), reverse=True)
        print passwords

