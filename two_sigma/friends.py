#!/usr/bin/env python

import fileinput
import unittest


# the task is to count the friend circles, not generate them.
#
# assume the friends matrix is symmetric:  if x and y are friends, then y and x are friends.
# in each row i we start at j = 1.  if we find a - then friend j is already in a set.
# otherwise it's in a new set.  mark all the Ys as - down to the diagonal.


def friendCircles(friends):
    circles = 0
    nfriends = len(friends)

    for i in xrange(nfriends):
        if friends[i][i] == 'Y':
            circles += 1
            wash(i, friends)

    return circles


def wash(i, friends):
    nfriends = len(friends)
    if friends[i][i] == 'Y':
        friends[i][i] = '-'
    for j in xrange(i + 1, nfriends):
        if friends[i][j] == 'Y':
            friends[i][j] = '-'
            wash(j, friends)
            for k in xrange(i, j + 1):
                if friends[k][j] == 'Y':
                    friends[k][j] = '-'
                    wash(k, friends)


if __name__ == '__main__':
    arr = []
    fi = fileinput.FileInput()
    while True:
        line = fi.readline().strip()
        if not line:
            break

        if fi.isfirstline():
            continue

        arr.append(list(line))

    print arr


class MyTest(unittest.TestCase):
    def test1(self):
        arr = [['Y', 'Y', 'N', 'N'], ['Y', 'Y', 'Y', 'N'], ['N', 'Y', 'Y', 'N'], ['N', 'N', 'N', 'Y']]

        print arr[0][3]

        self.assertEqual(2, friendCircles(arr))

    def test2(self):
        arr = [['Y', 'N', 'Y', 'N'], ['N', 'Y', 'Y', 'N'], ['Y', 'Y', 'N', 'N'], ['N', 'N', 'N', 'Y']]

        self.assertEqual(2, friendCircles(arr))
