#!/usr/bin/env python

import fileinput

if __name__ == '__main__':
    fi = fileinput.FileInput()

    nelements = fi.readline()
    elements = map(int, fi.readline().split(' '))

    print elements