
# function to calculate AT proportion in a sequence

from __future__ import division

def get (dna):
    length = len(dna)
    a = dna.count("A")
    t = dna.count("T")
    at_proportion = (a + t)/length
    return at_proportion


