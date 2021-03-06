import steady as st
import unittest
import random
import pprint

pp = pprint.PrettyPrinter()

class TestSteady(unittest.TestCase):

    def test1(self):
        multiple = 3
        sequence = []
        for i in xrange(4 * multiple):
            sequence.append(random.choice(st.nucleotides))

        print ''.join(sequence)

        d = st.occurrences(sequence)
        pp.pprint(d)

    def test_invariant(self):
        sequence = 'GTACCCTTGCGT'
        d = st.occurrences(sequence)
        n = len(sequence)

        pp.pprint(sequence)
        pp.pprint(d)

#        print st.invariant_holds(d, 5, 7)
#        print st.invariant_holds(d, 0, 12)
        self.assertFalse(st.invariant_holds(d, 0, 0))
        self.assertFalse(st.invariant_holds(d, 0, 1))
        self.assertFalse(st.invariant_holds(d, 0, 3))
        self.assertTrue(st.invariant_holds(d, 0, 4))
        self.assertTrue(st.invariant_holds(d, 5, 7))
        self.assertTrue(st.invariant_holds(d, 9, 12))

    def test_algorithm_part1(self):
        # test finding the first interval
        sequence = 'GTACCCTTGCGT'
        d = st.occurrences(sequence)

        l = 0
        r = 0
        while not st.invariant_holds(d, l, r):
            r += 1

        self.assertEqual(4, r)
        self.assertTrue(st.invariant_holds(d, l, r))

        # now wind l
        while st.invariant_holds(d, l, r):
            l += 1

        self.assertEqual(2, l)
        self.assertTrue(st.invariant_holds(d, l - 1, r))

    def test_algorithm_part2(self):
        sequence = 'GTACCCTTGCGT'
        self.assertEqual(2, st.steadyGene(sequence))

    def test_missing_ntide(self):
        sequence = 'GGAGTAATAATG'  # no C
        d = st.occurrences(sequence)
        print sequence
        pp.pprint(d)
        print st.find_best_interval(sequence)

    def test_one_ntide(self):
        sequence = 'A' * 12
        d = st.occurrences(sequence)
        print sequence
        pp.pprint(d)
        print st.find_best_interval(sequence)
        self.assertEqual(9, st.steadyGene(sequence))

    def test_random(self):
        multiple = 3
        ntides = []
        for i in xrange(4 * multiple):
            ntides.append(random.choice(st.nucleotides))

        sequence = ''.join(ntides)

        d = st.occurrences(sequence)
        print sequence
        pp.pprint(d)
        print st.find_best_interval(sequence)

    def test_n_eq_1(self):
        sequence = 'ACGG'
        d = st.occurrences(sequence)
        print sequence
        pp.pprint(d)
        print st.find_best_interval(sequence)

    def test_bigger(self):
        multiple = 9
        ntides = []
        for i in xrange(4 * multiple):
            ntides.append(random.choice(st.nucleotides))

        sequence = ''.join(ntides)

        d = st.occurrences(sequence)
        print sequence
        pp.pprint(d)
        print st.find_best_interval(sequence)

    def test_gigantic(self):
        multiple = 125000
        ntides = []
        for i in xrange(4 * multiple):
            ntides.append(random.choice(st.nucleotides))

        print "built sequence, scanning it now"
        sequence = ''.join(ntides)

        d = st.occurrences(sequence)
#        print sequence
#        pp.pprint(d)
        print st.find_best_interval(sequence)

    def test_gigantic_one_ntide(self):
        sequence = 'A' * 500000
        self.assertEqual(375000, st.steadyGene(sequence))

    def test_gigantic_balanced(self):
        sequence = 'ACTG' * 125000
        print st.find_best_interval(sequence)

    def test_empty_string(self):
        sequence = ''
        print st.find_best_interval(sequence)

# interesting test cases
# GGAGTAATAATG  (no C)
# GTACCCTTGCGT  answer is 2
# n = 1

# AACCAACTCAAG  algorithm gives interval as (0, 5)