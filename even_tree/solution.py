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

    # implemented as a dictionary that maps nodes to lists of Nodes.

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

    def addedge(self, a, b):
        '''
        add an edge from a to b
        '''
        if a not in self.adj_list:
            raise GraphException("origin %s not in graph" % a)

        if b not in self.adj_list:
            raise GraphException("terminus %s not in graph" % b)

        self.adj_list[a].append(b)

    def removeedge(self, a, b):
        # delete the edge going from node a to node b
        # it is not an error if b is not in the graph.  a must be present though.

        if a not in self.adj_list:
            raise GraphException("origin %s not in graph" % a)

        self.adj_list[a].remove(b)

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


class UGraph(DGraph):
    '''
    implements an undirected graph.
    '''

    def __init__(self):
        super(UGraph, self).__init__()

    def addedge(self, a, b):
        super(UGraph, self).addedge(a, b)
        super(UGraph, self).addedge(b, a)


##########    ##########    ##########    ##########    ##########

def subtree_size(gr, node):
    global edges_to_remove
    if not gr.adj_list[node]:
        # leaf
        # print "node %s: %s" % (node, 1)
        return 1

    sz = sum([subtree_size(gr, x) for x in gr.adj_list[node]]) + 1
    # print "node %s:  %s" % (node, sz)
    if sz % 2 == 0:
        edges_to_remove += 1
    return sz


def remove_back_links(gr, node):
    for n in gr.adj_list[node]:
        gr.removeedge(n, node)
        remove_back_links(gr, n)


def build_graph(nnodes, edges):
    # returns the root and the graph
    gr = UGraph()
    number_to_node = {}
    for a in xrange(nnodes):
        # node numbering is 1-based
        if a + 1 not in number_to_node:
            n = Node("%s" % (a + 1))
            number_to_node[a + 1] = n
        gr.addnode(number_to_node[a + 1])

    for p in edges:
        gr.addedge(number_to_node[p[0]], number_to_node[p[1]])

    return number_to_node[1], gr


if __name__ == '__main__':
    fi = fileinput.FileInput()
    nnodes, nedges = map(int, fi.readline().strip().split(' '))
    edges = []
    for _ in xrange(nedges):
        edges.append(map(int, fi.readline().strip().split(' ')))

    # build the graph
    root, gr = build_graph(nnodes, edges)

    # want this tree to be a directed graph, remove edges to parent nodes
    remove_back_links(gr, root)

#    gr.dump()

    # idea:  get the size of the subtree rooted at  each node.  if that  number is even then the link pointing to
    # that subtree can be removed.  the only exception is for the root; if the subtree size for the root is even then
    # there is no incoming edge to remove.

    edges_to_remove = 0

    sz = subtree_size(gr, root)
    if sz % 2 == 0:
        edges_to_remove -= 1
    print edges_to_remove

