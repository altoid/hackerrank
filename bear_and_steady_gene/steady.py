# https://www.hackerrank.com/challenges/bear-and-steady-gene/problem

nucleotides = 'ACTG'

def occurrences(sequence):
    """

    :param sequence:
    :return:  a dictionary, keys are A, C, G, or T, values are
    arrays the same length as the sequence.  the value at index i
    is the number of occurrences of that nucleotide up to and including
    i.
    """
    result = {
        'A': [0],
        'C': [0],
        'G': [0],
        'T': [0],
    }

    counts = {
        'A': 0,
        'C': 0,
        'G': 0,
        'T': 0,
    }

    for c in sequence:
        counts[c] += 1
        for k in counts.keys():
            result[k].append(counts[k])

    # append final counts one more time.  this will make
    # array arithmetic easier.
    for k in counts.keys():
        result[k].append(counts[k])

    return result


def invariant_holds(odict, l, r):
    """
    return true if the number of each nucleotide outside the range
    [l, r] is <= k.

    we count between the nucleotides:

    0   1   2   3   4        n-1  n
    | A | C | T | G | ... | C | G |

    :param k:
    :param odict:
    :param l:
    :param r:
    :return:
    """

    try:
        k = len(odict['A']) / 4
        for key in odict.keys():
            left_part = odict[key][l] - odict[key][0]
            right_part = odict[key][-1] - odict[key][r]

            if left_part + right_part > k:
                return False
        return True
    except IndexError as e:
        print e
        print "k = %s, l = %s, r = %s" % (k, l, r)


def find_best_interval(sequence):
    l = 0
    r = 0
    odict = occurrences(sequence)
    n = len(sequence)
    best_interval = (0, n)
    if not sequence:
        return best_interval

    while True:
        if r < n:
            r += 1

        while not invariant_holds(odict, l, r):
            if r >= n:
                break
            r += 1

        # now wind l
        while invariant_holds(odict, l, r):
            l += 1
            if l >= r:
                return best_interval

        # reset l
        if not invariant_holds(odict, l, r):
            l -= 1

        if r - l < best_interval[1] - best_interval[0]:
            best_interval = (l, r)
#            print best_interval

        if r >= n:
            break

    return best_interval


def steadyGene(sequence):
    i = find_best_interval(sequence)
    return i[1] - i[0]