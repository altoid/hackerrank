#!/usr/bin/env python

# https://www.hackerrank.com/challenges/power-of-large-numbers/problem

a = 34534985349875439875439875349875
b = 93475349759384754395743975349573495

MODULUS = 1000000007


def power(x, n):
    result = 1
    while n:
        if n & 1:
            result = result * x % MODULUS

        x = x * x % MODULUS
        n >>= 1

    return result

# we are guaranteed that a is not divisible by MODULUS


a2 = a % MODULUS

# we know that a2 ** (MODULUS - 1) is congruent to 1 modulo MODULUS
_, n = divmod(b, MODULUS - 1)

# and b = m * (MODULUS - 1) + n
#
# so a ** b = a ** (m * (MODULUS - 1)) * a ** n
#           = 1 * a ** n
#           = a2 ** n


print(a2, n)

x = power(a2, n)
print(x)


