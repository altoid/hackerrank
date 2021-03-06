#!/usr/bin/env python

import fileinput

BOARDSIZE = 10
ACROSS = 0
DOWN = 1

# assume no 1-letter words

class Run(object):
    def __init__(self, r, c, length, dir):
        self.row = r
        self.col = c
        self.length = length
        self.dir = dir

    def __str__(self):
        return "[row %s, col %s, len %s, dir %s]" % (
            self.row, self.col, self.length, 'DOWN' if self.dir else 'ACROSS')

    def __repr__(self):
        return str(self)

    def __len__(self):
        return self.length


def next_permutation(mylist, cmp_function):
    # return the permutation that lexicographically follows
    # <mylist>, or None if there is no such permutation
    #
    # algorithm:
    # - scan RL to first item x that is smaller than
    #   the one to its right
    # - swap it with the smallest item to the right
    #   of x that is larger than x (y)
    # - sort the list [x+1:]

    l = len(mylist)
    if l < 2:
        return

    current = l - 2
    following = l - 1
    while current >= 0:
        if cmp_function(mylist[current], mylist[following]) < 0:
            #print "ack - current = %s, following = %s, list = %s" % (current, following, mylist)
            # find the smallest item to the right of
            # mylist[current] that is bigger
            # than mylist[current]
            k = following
            m = mylist[k]
            mi = k
            while k < l:
                # mylist[current] < mylist[k] < m:
                if cmp_function(mylist[current], mylist[k]) < 0 and cmp_function(mylist[k], m) < 0:
                    m = mylist[k]
                    mi = k
                k += 1

            mylist_copy = list(mylist)
            mylist_copy[current], mylist_copy[mi] = mylist_copy[mi], mylist_copy[current]
            return mylist_copy[:following] + sorted(mylist_copy[following:])
        
        current -= 1
        following -= 1
    

def permute(mylist, cmp_function=cmp):
    x = sorted(mylist, cmp_function)

    while x is not None:
        yield x
        x = next_permutation(x, cmp_function)


# words are sorted by length, then alphabetically
def my_compare(a, b):
    if len(a) == len(b):
        return cmp(a, b)

    if len(a) < len(b):
        return -1

    return 1


def word_fits(word, run):
    global board
    if len(word) != len(run):
        return False

    chars = list(word)
    if run.dir == ACROSS:
        for i in xrange(len(chars)):
            cell = board[run.row][run.col + i]
            if cell == '-':
                board[run.row][run.col + i] = chars[i]
            elif cell != chars[i]:
                return False
        return True

    for i in xrange(len(chars)):
        cell = board[run.row + i][run.col]
        if cell == '-':
            board[run.row + i][run.col] = chars[i]
        elif cell != chars[i]:
            return False
    return True


def clear_board():
    global board
    for r in xrange(BOARDSIZE):
        for c in xrange(BOARDSIZE):
            if board[r][c] != '+':
                board[r][c] = '-'


def test_solution(soln, all_runs):
    for i in xrange(len(all_runs)):
        if not word_fits(soln[i], all_runs[i]):
            return False

    return True


def crosswordPuzzle(crossword, raw_words):
    global board
    board = []
    for r in crossword:
        board.append(list(r))

    words = raw_words.strip().split(';')
    # scan the board: across
    across_runs = []
    for row in xrange(BOARDSIZE):
        # '' -> '-'
        # '' -> '+'
        # '-' -> '-'
        # '-' -> '+'
        # '+' -> '-'
        # '+' -> '+'
        
        lastchar = None
        currentrun = None
        for col in xrange(BOARDSIZE):
            c = board[row][col]
            if not lastchar:
                if c == '-':
                    currentrun = Run(row, col, 1, ACROSS)

            elif lastchar == '-':
                if c != '-':
                    if currentrun.length > 1:
                        across_runs.append(currentrun)
                    currentrun = None
                elif c == '-':
                    currentrun.length += 1

            elif lastchar != '-':
                if c == '-':
                    currentrun = Run(row, col, 1, ACROSS)

            lastchar = c
            
        if currentrun and currentrun.length > 1:
            across_runs.append(currentrun)
            
    # scan the board: down
    down_runs = []
    for col in xrange(BOARDSIZE):
        # '' -> '-'
        # '' -> '+'
        # '-' -> '-'
        # '-' -> '+'
        # '+' -> '-'
        # '+' -> '+'
        
        lastchar = None
        currentrun = None
        for row in xrange(BOARDSIZE):
            c = board[row][col]
            if not lastchar:
                if c == '-':
                    currentrun = Run(row, col, 1, DOWN)

            elif lastchar == '-':
                if c != '-':
                    if currentrun.length > 1:
                        down_runs.append(currentrun)
                    currentrun = None
                elif c == '-':
                    currentrun.length += 1

            elif lastchar != '-':
                if c == '-':
                    currentrun = Run(row, col, 1, DOWN)

            lastchar = c
            
        if currentrun and currentrun.length > 1:
            down_runs.append(currentrun)

    # print "across_runs: %s" % across_runs
    # print "down_runs: %s" % down_runs

    all_runs = across_runs + down_runs
    all_lengths = map(lambda x: x.length, all_runs)
    # print "all_runs: %s" % all_runs
    # print "all_lengths: %s" % all_lengths

    # sort the words, first by length, then lexicographically
    
    # print words
    # print "#" * 44
    for x in permute(words, my_compare):
        lens = map(len, x)
        if lens == all_lengths:
            if test_solution(x, all_runs):
                result = map(lambda y: ''.join(y), board)
                return result

            clear_board()

    
if __name__ == '__main__':
    fi = fileinput.FileInput()
    crossword = []
    for _ in xrange(BOARDSIZE):
        crossword.append(fi.readline().strip())

    # read the words
    raw_words = fi.readline()

    result = crosswordPuzzle(crossword, raw_words)
    for r in result:
        print r

