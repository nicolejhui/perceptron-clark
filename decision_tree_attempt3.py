import math
import numpy as np
import pandas as pd

data = pd.read_csv('Data/mush_train.data', header=None)
data_rotated = pd.read_csv('Data/mush_train_cond_entr.data', header=None)



class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.split = None

# calculate entropy
# count up all of the the times of color? = x (ex: counting up all of r occurred in certain column of information)
# divide by total number of examples = X
# possibility = x/X
# entropy = - [sum(possibility of attribute *  log(the possibility))]

# find the counts of each unique value and create a dictionary


def entropy(data):
    for i in range(data.shape[1] - 1):
        attr_type, attr_count = np.unique(data.values[:, i + 1], return_counts=True)
        keys = attr_type
        values = attr_count
        all_attributes = dict(zip(keys, values))
        # print(all_attributes)
        for key, value in all_attributes.items():
            # print(value)
            prob = value / 41472
            # print(prob)
            entropy = - (np.sum(prob * np.log2(prob)))
            # print(entropy)
        # return (entropy)
        # return all_attributes


# calculate conditional entropy
# need to calculate conditional probability


def conditional_entropy(data):
    # print("all_attributes")
    for i in range(data.shape[1] - 1):
        attr_type, attr_count = np.unique(data.values[:, i + 1], return_counts=True)
        keys = attr_type
        values = attr_count
        # print(keys, values)
        all_attributes = dict(zip(keys, values))
        # print(all_attributes)
        for key, value in all_attributes.items():
            # print(value)
            prob_a = value/41472
            print(prob_a)
    # print("all_attribtutes_rotated")
        for j in range(data_rotated.shape[1] - 1):
            rot_attr_type, rot_attr_count = np.unique(data_rotated.values[:, j + 1], return_counts=True)
            rot_keys = rot_attr_type
            rot_values = rot_attr_count
            # print(rot_keys, rot_values)
            all_attributes_rotated = dict(zip(rot_keys, rot_values))
            # print(all_attributes_rotated)
            for rot_key, rot_value in all_attributes_rotated.items():
                # print(rot_value)
                prob_b = rot_value/41472
                # print(prob_b)
                # goal is to have all possible combinations of prob_a and prob_b
                # when i put loop for prob_b within prob_a it gives me all combinations but values of prob_a are now different thatn before
                # print(prob_a, prob_b)
    # conditional_prob = (prob_a * prob_b) / prob_a
    # idk where in the function to make this code so that it returns all of prob a and prob b
    # conditional_entropy = - ((np.sum (prob_a)) * (np.sum(conditional_prob * np.log2(conditional_prob))))
    # print(conditional_entropy)
    # return conditional_entropy

# find information gain
# find best information gain


def information_gain(data):
    for attribute in all_attributes:
        information_gain = entropy - conditional_entropy
        # return information_gain????


#def split(data):
    # use sometime of loop
    # for attribute_type in all_attribute
    #   best_attribute = None
    #   compare information gain of certain attribute and find highest
    #   best_attribute = attribute_type
    #   split on that attribute
    # repeat over and over until entropy == 0 or majority vote

if __name__ == "__main__":
    entropy(data)
    conditional_entropy(data)
    # all_attributes = entropy(data)
    # print(all_attributes)
    # this is only returning the last value in the loop in entropy function; need to find a way to return all values
