import math
import numpy as np
import pandas as pd
import scipy as sp

#filename = "mush_train.data"
#file = open("mush_train.data", mode = 'r')

data = pd.read_csv('Data/mush_train.data', header=None)

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.split = None


# attributes = (cap_size, cap_surface, cap_color, bruises, order, gill_attachment, gill_spacing, gill_size, gill_color, stalk_shape,
#             stalk_surface, stalk_surface_above_root, stalk_surface_below_root, stalk_color_above_ring, stalk_color_below_ring,
#             veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat)
#
# to later use to pull best attribute out

#create class and node


#calculate entropy

#def entropy(attribute, examples):
#   for attribute type in all_attributes:
#       count up all of the the times of color? = x (ex: counting up all of r occured in vertain column of information)
#       divide by total number of examples = X
#   possibility = x/X
#   entropy = - [sum(possibility of attribute *  log(the possibilty))]

np.unique

# this code is from stack overflow bc I'm dumb and couldn't come up with it on my own
# def entropy(attribute):
#     for attribute in all_attributes:
#         n_attribute = len(all_attributes)
#         if n_attribute <= 1:
#             return 0
#         counts = np.bincount(attributes)
#         probs = counts[np.nonzero(counts)] / n_attribute
#         n_classes = len(probs)
#
#         if n_classes <= 1:
#             return 0
#         return - np.sum(probs * np.log(probs)) / np.log(n_classes)
#     entropy = - np.sum(probs * np.log(probs)) / np.log(n_classes)
#     print(entropy)
#
#
# calculate conditional_entropy
#
# def conditional_entropy(attribute):
#     n_attribute = len(all_attributes)
#     if n_attribute <= 1:
#         return 0
#     counts = np.bincount(attributes)
#     probs = counts[np.nonzero(counts)] / n_attribute
#     probs2 = counts[np.nonzero(counts)] / n_attribute
#     n_classes = len(probs)
#
# calculate information gain
#
# def information_gain(attribute):
#     entropy(attribute) - conditional_entropy(attribute)
#     take the biggest information gain
#     but how the fuck do I do that

# determining the split using the best IG
#
