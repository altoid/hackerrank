#!/usr/bin/env python

import fileinput

# assume no 1-letter words

# words are sorted by length, then alphabetically

if __name__ == '__main__':
    fi = fileinput.FileInput()
    for _ in xrange(10):
        fi.readline().strip()
    
    # read the words
    words = fi.readline().strip().split(';')
    print words

