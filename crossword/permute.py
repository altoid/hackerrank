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

        
