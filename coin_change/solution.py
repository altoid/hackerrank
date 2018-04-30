#!/usr/bin/env python

from pprint import pprint, pformat

def coin_change(amount, coins):
    """
    returns the answer and the total number of recursive calls
    to coin_change.
    """

    if not coins:
        return 0, 1

    if amount == 0:
        return 1, 1

    if amount < 0:
        return 0, 1

    total1, count1 = coin_change(amount, coins[:-1])
    total2, count2 = coin_change(amount - coins[-1], coins)

    return total1 + total2, count1 + count2


def solve(amount, coins):
    pprint("amount = %s" % amount)
    pprint("coins = %s" % coins)
    result = coin_change(amount, coins)
    print "solution:  %s" % result[0]
    print "total calls to coin_change:  %s" % result[1]


if __name__ == '__main__':
    solve(4, [1,2,3])
    solve(10, [2,3,5,6])
