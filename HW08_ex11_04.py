#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
pledge_histogram = {}

def reverse_lookup_old(d, v):
	value_list = [k for k in d if d[k] == v]
	
	return value_list
    

def reverse_lookup_new(d, v):
    d = histogram_new(get_pledge_list())
 
    return reverse_lookup_old(d,v)


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################
def histogram_old(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c,0)
    return d

def histogram_new(s):
    return histogram_old(s)

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
def main():   # DO NOT CHANGE BELOW
    print reverse_lookup_new(pledge_histogram, "1") # This will return an empty list because it's looking for "1" (string), not 1 (number)
    print reverse_lookup_new(pledge_histogram, "9") # Same as above
    print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
