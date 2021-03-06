#!/usr/bin/env python

import fileinput

from pprint import pprint, pformat


class GraphException(Exception):
    pass


class Node(object):

    def __init__(self, label):
        self._label = label

    def __str__(self):
        return '%s' % self._label

    def __repr__(self):
        return "Node('%s')" % (self._label)

    def __eq__(self, other):
        if not isinstance(other, Node):
            raise NotImplemented

        return self._label == other._label

    def __hash__(self):
        return hash(self._label)

    def __cmp__(self, other):
        if not isinstance(other, Node):
            raise NotImplemented

        return cmp(self._label, other._label)

    def show_ids(self, tag):
        print '=' * 11, tag, '=' * 11
        print repr(self)
        print id(self)
        print id(self._label)
        
    @property
    def label(self):
        return self._label


class DGraph(object):
    '''
    directed graph.
    '''
    # implemented as a dictionary that maps nodes to lists of
    # tuples:  (Node, cost) which indicate the cost of the path.

    def __init__(self):
        self.adj_list = {}

    def __nonzero__(self):
        # returns true if the graph has > 0 nodes
        return len(self.adj_list) > 0

    def __len__(self):
        # returns the number of nodes in the graph.
        return len(self.adj_list)

    def addnode(self, n):
        if n in self.adj_list:
            raise GraphException("node %s is already in the graph" % n)
        self.adj_list[n] = list()

    def addnodes(self, *nodes):
        for n in nodes:
            self.addnode(n)

    def contains(self, n):
        return n in self.adj_list

    def addedge(self, a, b, cost=1):
        '''
        add an edge from a to be with default cost 1
        '''
        if a not in self.adj_list:
            raise GraphException("origin %s not in graph" % a)

        if b not in self.adj_list:
            raise GraphException("terminus %s not in graph" % b)

        edge = (b, cost)
        self.adj_list[a].append(edge)

    def dump(self):
        pprint(self.adj_list)

    '''
    return the nodes in the graph, as a list
    '''
    def nodes(self):
        for k in self.adj_list.keys():
            yield k

    def neighbors(self, n):
        if not self.contains(n):
            raise GraphException("node %s not in graph" % n)

        for k in self.adj_list[n]:
            yield k[0]

    def edges(self):
        for n in self.nodes():
            for arc in self.adj_list[n]:
                yield Edge(n, arc[0], arc[1])


class UGraph(DGraph):
    '''
    implements an undirected graph.
    '''

    def __init__(self):
        super(UGraph, self).__init__()

    def addedge(self, a, b, cost=1):
        super(UGraph, self).addedge(a, b, cost)
        super(UGraph, self).addedge(b, a, cost)


##########    ##########    ##########    ##########    ##########


def _next_unvisited_neighbor(g, n, visited):
    for k in g.adj_list[n]:
        if k[0] not in visited:
            return k[0]


def getpartitions(g):
    # for the given graph, return a list giving the number of nodes in each partition.
    #
    # todo - this will only work for undirected graphs.  if the graph
    # todo - is directed, we can't traverse the subgraphs
    # todo - whose member nodes we are returning.

    result = []

    # idea: pick a node and do DFS on the graph.  if there are any
    # nodes we still haven't visited, do it again.
    unvisited = set([n for n in g.nodes()])
    while len(unvisited) > 0:
        stack = []
        visited = set()

        n = unvisited.pop()
        stack.append(n)
        visited.add(n)

        # look at node on top of stack
        # if it has an unvisited neighbor,
        # mark it visited and put it at top of stack
        # otherwise pull it off

        while len(stack) > 0:
            top = stack[-1]
            # get next unvisited neighbor
            k = _next_unvisited_neighbor(g, top, visited)
            if k is None:
                stack.pop()
            else:
                stack.append(k)
                visited.add(k)
                unvisited.remove(k)

        # visited now has all the nodes in the subgraph.  make a new graph out of them.
        result.append(len(visited))

    return result


#####################
def compute(partitions):

    # hack, er, optimization.  discovered this:
    # sort the partitions list.  when there are > 1 singleton nodes,
    #
    # 1 1 1 1 ... 1 2 3 5 6 blah
    #
    # we can clip off all but one 1 and compute the answer on the resulting list
    # and then add n * (n - 1) / 2
    # and n * sum(list without ones)
    # where n is the number of 1s in the list.

    # we don't have to sort

    without_ones = filter(lambda x: x != 1, partitions)
    lpartitions = len(partitions)
    l_no_ones = len(without_ones)
    n_ones = lpartitions - l_no_ones
    total = n_ones * (n_ones - 1) / 2
    total += n_ones * sum(without_ones)

    for i in xrange(l_no_ones):
        for j in xrange(i + 1, l_no_ones):
            total += (without_ones[i] * without_ones[j])

    return total


def journeyToMoon(nastronauts, pairs):
    gr = UGraph()
    anumber_to_node = {}
    for a in xrange(nastronauts):
        if a not in anumber_to_node:
            n = Node("%s" % a)
            anumber_to_node[a] = n
        gr.addnode(anumber_to_node[a])

    for p in pairs:
        gr.addedge(anumber_to_node[p[0]], anumber_to_node[p[1]])

    partitions = getpartitions(gr)

    return compute(partitions)


if __name__ == '__main__':
    fi = fileinput.FileInput()
    nastronauts, npairs = map(int, fi.readline().strip().split(' '))
    pairs = []
    for _ in xrange(npairs):
        pairs.append(map(int, fi.readline().strip().split(' ')))
    result = journeyToMoon(nastronauts, pairs)
    print result



