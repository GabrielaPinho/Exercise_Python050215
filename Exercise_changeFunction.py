
# function to calculate AT proportion in a sequence

from __future__ import division

def get (dna):
    length = len(dna)
    a = dna.upper().count("A")
    t = dna.upper().count("T")
    at_proportion = (a + t)/length
# this is equal to "arrendondar", 3 will be the number of numbers after the comma
    return round(at_proportion, 3)
