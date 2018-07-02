#!/usr/bin/env python

from pprint import pprint, pformat
import collections
import fileinput

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


class Edge(object):
    def __init__(self, origin, terminus, cost):
        self._origin = origin
        self._terminus = terminus
        self._cost = cost

    def __str__(self):
        return "(%s - %s - %s)" % (self._origin, self._cost, self._terminus)

    def __hash__(self):
        return hash((self.origin, self.terminus, self.cost))

    def __eq__(self, other):
        if not isinstance(other, Edge):
            raise NotImplemented

        return self.origin == other.origin and self.terminus == other.terminus and self.cost == other.cost

    @property
    def origin(self):
        return self._origin

    @property
    def terminus(self):
        return self._terminus

    @property
    def cost(self):
        return self._cost


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

        sorted_neighbors = sorted(self.adj_list[n], key=lambda n: n[0]._label)
        for k in sorted_neighbors:
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

    def edges(self):
        # since this is an undirected graph, we have to be careful about not putting back-and-forth edges into the
        # result set.  we'll put edges in where the origin is lexicographically less than the terminus

        for n in self.nodes():
            for arc in self.adj_list[n]:
                a1 = n
                a2 = arc[0]
                if a1 < a2:
                    yield Edge(a1, a2, arc[1])

##########    ##########    ##########    ##########    ##########


def _next_unvisited_neighbor(g, n, visited):
    adj_list = sorted([x[0] for x in g.adj_list[n]], key=lambda n: n._label)
    for k in adj_list:
        if k not in visited:
            return k


def dfs(g, n):
    # non-recursive implementation

    if not g.contains(n):
        raise GraphException("node %s not in graph" % n)
    
    stack = []
    visited = set()
    
    stack.append(n)
    visited.add(n)
    result = str(n)
    
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
            result += str(k)

    return result


def getpartitions(g):
    # for the given graph, return its disjoint subgraphs.  if the
    # graph isn't partitioned, just return the the graph.  if it is,
    # return one node from each subgraph.
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
        subgraph = UGraph()
        for n in visited:
            subgraph.addnode(n)
            subgraph.adj_list[n] = list(g.adj_list[n])
        result.append(subgraph)

    return result


#####################

def evaluate(subgraph, libcost, roadcost):
    nnodes = len(subgraph)
    nroads = nnodes - 1

    # rule of thumb:
    # if cost of lib <= cost of road, rebuild all libs and no roads
    # if cost of lib > cost of road, rebuild 1 lib & all roads

    if libcost > roadcost:
        return libcost + nroads * roadcost
    return nnodes * libcost


def roadsAndLibraries(ncities, libcost, roadcost, cities):
    # construct the graph
    gr = UGraph()
    node_dict = {}
    for i in xrange(1, ncities + 1):
        node_dict[i] = Node("%s" % i)
        gr.addnode(node_dict[i])
    for e in cities:
        gr.addedge(node_dict[e[0]], node_dict[e[1]], roadcost)

    subgraphs = getpartitions(gr)
    total = 0
    for g in subgraphs:
        cost = evaluate(g, libcost, roadcost)
        total += cost
    return total


if __name__ == '__main__':
    fi = fileinput.FileInput()
    line = fi.readline().strip()
    nqueries = int(line)
    for _ in xrange(nqueries):
        line = fi.readline().strip().split(' ')
        ncities, nroads, libcost, roadcost = map(lambda x: int(x), line)
        cities = []
        for _ in xrange(nroads):
            e = map(lambda x: int(x), fi.readline().strip().split(' '))
            cities.append(e)
            
        print roadsAndLibraries(ncities, libcost, roadcost, cities)


