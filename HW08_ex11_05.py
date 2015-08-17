#!/usr/bin/env python
# Exercise 5
# (1) Write a more concise version of invert_dict_old.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Update print_hist_new from HW08_ex_11_03.py to be able to print
# a sorted version of the dict (print key/value pairs from 0 through the
# largest key values, (and those in between))
# Ex. If d = {1:["this, that"], 3: ["the"]}, it prints:
#    '1: ["this", "that"]'
#    '2:'
#    '3: ["the"]'
##############################################################################

def invert_dict_old(d):
    inverse = dict()
    inverse = {d[key]:key if d[key] not in inverse else inverse[d[key]].append(key) for key in d}
    
    return inverse

def invert_dict_new(d):
    invert = invert_dict_old(d)
    key_list = invert.keys()
    range_limit = int(max(key_list))
    dict_new = {c:invert.get(c,'') for c in range(range_limit)}

    return dict_new


def print_hist_newest(d):
    for k in d:
        print str(k) + ": " + d[k]

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################
pledge_histogram = {}

def histogram_old(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c,0)
    return d

def histogram_new(s):
    new_hist = histogram_old(s)
    return new_hist

def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
    with open('pledge.txt',"r") as handler:
        pledge_list = handler.read().split()
    return pledge_list
##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():  # DO NOT CHANGE BELOW
    pledge_histogram = histogram_new(get_pledge_list())
    pledge_invert = invert_dict_new(pledge_histogram)
    print_hist_newest(pledge_invert)

if __name__ == '__main__':
    main()
