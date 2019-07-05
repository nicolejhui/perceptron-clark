import numpy as np
import pandas as pd

all_examples = pd.read_csv('Data/example_data', header=None)
all_examples = all_examples.values
# print(data)
attributes_list = ["X1", "X2"]
# where each attribute correlates with a column


class Node:
    def __init__(self, name):
        # name of attribute of which you split on
        self.name = name
        # list which contains children nodes
        self.children = {}
        # list of the examples that the node holds
        self.examples = []


def get_entropy(data):
    label, label_counts = np.unique(data[:, 0], return_counts=True)
    # print(label, label_counts)
    label1_prob = label_counts[0] / data.shape[0]
    label2_prob = label_counts[1] / data.shape[0]
    # print(label1_prob, label2_prob)
    out = - (np.sum((label1_prob * (np.log2(label1_prob)) + (label2_prob * (np.log2(label2_prob))))))
    # print(out)
    return out


def con_entropy(feature_col):
    # create empty dictionary which will hold unique values as keys and the probability of y being a certain label
    # when example is that unique value
    conditional_array = {}
    for example in all_examples:
        if example[feature_col] not in conditional_array:
            conditional_array[example[feature_col]] = [0, 0]
        if example[0] == '+':
            conditional_array[example[feature_col]][0] += 1
        if example[0] == '-':
            conditional_array[example[feature_col]][1] += 1
    # print(conditional_array)
    # initialize conditional_entropy so we can add to it
    conditional_entropy = 0
    for unique_var, counts, in conditional_array.items():
        frequency = (counts[0] + counts[1]) / all_examples.shape[0]
        # print('freq: ' + str(frequency))
        # print(unique_var, counts)
        label1_joint_prob = counts[0] / (counts[0] + counts[1])
        # print(label1_joint_prob)
        label2_joint_prob = counts[1] / (counts[0] + counts[1])
        # print(label2_joint_prob)
        if label1_joint_prob == 0:
            label1_log_prob = 0
            # print('first if statement triggered')
        else:
            label1_log_prob = label1_joint_prob * np.log2(label1_joint_prob)
        if label2_joint_prob == 0:
            label2_log_prob = 0
            # print('second if statement triggered')
        else:
            label2_log_prob = label2_joint_prob * np.log2(label2_joint_prob)
#        print(label1_log_prob)
#        print(label2_log_prob)
#        print('freq:' + str(frequency))
#        print('sum: ' + str((label1_log_prob + label2_log_prob)))
#        print('cond e: ' + str(conditional_entropy))
        conditional_entropy += frequency * (label1_log_prob + label2_log_prob)
#        print('con entropy:' + str(conditional_entropy))
    conditional_entropy = -1 * conditional_entropy
    # print('conditional entropy:', str(conditional_entropy))
    return conditional_entropy


def find_best_attribute(column):
    # define entropy
    entropy = get_entropy(all_examples)
    # create empty list to later hold all information gains for every attribute
    ig_list = []
    # create loop to find information gain for every attribute (every column) and add it to the list
    for i in range(num_col):
        if i > 0:
            conditional_entropy = con_entropy(i)
            information_gain = entropy - conditional_entropy
            # print('information gain:' + str(information_gain))
            ig_list.append(information_gain)
            # print('list of IG values' + str(ig_list))
        info_gain_dict = dict(zip(attributes_list, ig_list))
        # print(info_gain_dict)
    best_attribute = max(info_gain_dict, key=info_gain_dict.get)
    # print('best attribute to split on:', str(best_attribute))
    best_attribute_index = attributes_list.index(best_attribute) + 1
    best_attribute = all_examples[:, best_attribute_index]
    # print('index of best attribute in dataset:', best_attribute_index)
    # print('best attribute data:' + str(best_attribute))
    return best_attribute_index, best_attribute, ig_list, info_gain_dict


def split_data_and_create_node(node):
    child_node_dict = {}
    root_node = Node("root")
    root_node.examples = all_examples
    # get best split
    best_idx, best_attribute, ig_list, info_gain_dict = find_best_attribute(num_col)
    print('best_attribute column found in from previous function:', str(best_attribute))
    # split data based on the unique value of the best attribute
    unique_val_of_best_attribute = []
    for unique_val in np.unique(best_attribute):
        print('unique value:', unique_val)
        unique_val_of_best_attribute.append(unique_val)
        split = np.empty((0, 3), int)
        for example in all_examples:
            if example[best_idx] == unique_val:
                # print(row)
                split = np.append(split, np.array([example]), axis=0)
        temp_node = Node(unique_val_of_best_attribute[unique_val])
        temp_node.examples = split
        child_node_dict.update({str(unique_val_of_best_attribute[unique_val]): temp_node})
        root_node.children = child_node_dict
        print('Node name:', str(unique_val_of_best_attribute[unique_val]))
        print('list of unique values for the best attribute to split on:', unique_val_of_best_attribute)
        print('examples in dataset with that unique value of the attribute:')
        print(temp_node.examples)
        print(root_node.children)

    ''''# remove used valued from list of IG values and IG dictionary to later use updated list/dict when function is called again
    for ig in ig_list:
        print('list of IG values:',  str(ig_list))
        ig_list.remove(max(ig_list))
        print('updated IG list:', str(ig_list))
        # update info_gain_dict
        updated_ig_list = ig_list
        print('info gain dict:', str(info_gain_dict))
        best_dict_attr = max(info_gain_dict, key=info_gain_dict.get)
        del info_gain_dict[best_dict_attr]
        updated_ig_dict = info_gain_dict
        print('updated ig dict:', str(updated_ig_dict))
        # call split_data_and_create_node function again but this time using such updated lists/dict'''
    return root_node, child_node_dict,


def partition_children():
    child_node_dict = split_data_and_create_node(node)

if __name__ == "__main__":
    entropy = get_entropy(all_examples)
    print('entropy:' + str(entropy))
    num_col = all_examples.shape[1]
    # keep doing this until information gain = 0
    # have to do it once more
    split_data_and_create_node(Node("root"))
    # need to build tree







