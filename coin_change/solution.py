#!/usr/bin/env python

from pprint import pprint, pformat

def coin_change(amount, coins):
    if not coins:
        return 0

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    return (coin_change(amount, coins[:-1]) +
            coin_change(amount - coins[-1], coins))


def solve(amount, coins):
    pprint("amount = %s" % amount)
    pprint("coins = %s" % coins)
    result = coin_change(amount, coins)
    print "solution:  %s" % result


if __name__ == '__main__':
    solve(4, [1,2,3])
    solve(10, [2,3,5,6])
