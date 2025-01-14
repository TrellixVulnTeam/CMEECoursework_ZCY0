#!/usr/bin/env python3

"""Python Practicals: Align DNA sequences
convert from the original align_seqs.py from repository,
read csv files including the two example sequences originally given
and find the best alignment and score
"""

__appname__ = 'align_seqs.py'
__author__ = 'Wenhua Zhou (wz2812@ic.ac.uk)'
__version__ = '0.0.1'

# load two sequences from the csv in data directory
import csv

f = open('../Data/DNA_seq.csv','r')

# read csv
csvread = csv.reader(f)
temp = []
for row in csvread:
    temp.append(tuple(row))
seq1 = temp[0][0] # put two sequences into seq1 and seq2
seq2 = temp[0][1]   

f.close()

# Assign the longer sequence s1, and the shorter to s2
# l1 is length of the longest, l2 that of the shortest

l1 = len(seq1)
l2 = len(seq2)
if l1 >= l2:
    s1 = seq1
    s2 = seq2
else:
    s1 = seq2
    s2 = seq1
    l1, l2 = l2, l1 # swap the two lengths

# A function that computes a score by returning the number of matches starting
# from arbitrary startpoint (chosen by user)
def calculate_score(s1, s2, l1, l2, startpoint):
    """ function that computes the score """
    matched = "" # to hold string displaying alignements
    score = 0
    for i in range(l2):
        if (i + startpoint) < l1:
            if s1[i + startpoint] == s2[i]: # if the bases match
                matched = matched + "*"
                score = score + 1
            else:
                matched = matched + "-"

    # some formatted output
    print("." * startpoint + matched)           
    print("." * startpoint + s2)
    print(s1)
    print(score) 
    print(" ")

    return score

# Test the function with some example starting points:
# calculate_score(s1, s2, l1, l2, 0)
# calculate_score(s1, s2, l1, l2, 1)
# calculate_score(s1, s2, l1, l2, 5)

# now try to find the best match (highest score) for the two sequences
my_best_align = None
my_best_score = -1

for i in range(l1): # Note that you just take the last alignment with the highest score
    z = calculate_score(s1, s2, l1, l2, i)
    if z > my_best_score:
        my_best_align = "." * i + s2 # use dots to match the position of alignment with the longer sequence
        my_best_score = z 

# print the best alignment and longer sequence
print(my_best_align)
print(s1)
print("Best score:", my_best_score)
