#!/usr/bin/env python

# https://www.hackerrank.com/challenges/sherlock-and-permutations/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign

import fileinput

binary_coeff_cache = {}
factorial_cache = {}


def factorial(n):
    if n not in factorial_cache:
        if n < 2:
            result = 1
        else:
            result = n * factorial(n - 1)

        factorial_cache[n] = result
    return factorial_cache[n]


# doing this without factorials caused recursion to go too deep.
def binary_coefficient(n, k):
    assert 0 <= k <= n

    if (n, k) not in binary_coeff_cache:
        if n <= 1 or k == 0:
            result = 1
        else:
            num = factorial(n)
            d1 = factorial(k)
            d2 = factorial(n - k)

            result = num // (d1 * d2)

        binary_coeff_cache[(n, k)] = result

    return binary_coeff_cache[(n, k)]


def solve(n, m):
    for i in range(2000):
        _ = binary_coefficient(i, i // 2)

    result = binary_coefficient(n + m - 1, m - 1)
    return result % 1000000007


if __name__ == '__main__':
    with fileinput.input() as fi:
        fi.readline()  # throw away first line
        for line in fi:
            a, b = line.strip().split()
            a = int(a)
            b = int(b)
            print(a, b, solve(a, b))



