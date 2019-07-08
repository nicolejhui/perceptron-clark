import numpy as np
import pandas as pd
import math

# print(data)
attributes_list = ["X1", "X2"]
# where each attribute correlates with a column

# root_node = Node("root")
# root_node.examples = all_examples


class Node:
    def __init__(self, name, examples):
        # name of attribute of which you split on
        self.name = name
        # list which contains children nodes
        self.children = {}
        # list of the examples that the node holds
        self.examples = examples
        self.entropy = 1

    def get_entropy(self):
        label, label_counts = np.unique(self.examples[:, 0], return_counts=True)
        # print(label, label_counts)
        label1_prob = label_counts[0] / self.examples.shape[0]
        label2_prob = label_counts[1] / self.examples.shape[0]
        # print(label1_prob, label2_prob)
        out = - (label1_prob * (np.log2(label1_prob)) + (label2_prob * (np.log2(label2_prob))))
        # print(out)
        return out

    def con_entropy(self, feature):
        # outcomes is a dict, with the keys being specific values that a feature takes (i.e. red) and
        # the values being lists containing the counts of features with that value that are poisonous or edible
        outcomes = {}
        total_examples = 0
        # Count how many examples with a given feature are poisonous.
        for example in self.examples:
            feature_value = example[feature]
            if feature_value not in outcomes:
                outcomes[feature_value] = [0, 0]
            if example[0] == '+':
                outcomes[feature_value][0] += 1
            if example[0] == '-':
                outcomes[feature_value][1] += 1
            total_examples += 1
        conditional_entropy = 0
        # Calculate conditional entropy for the feature
        for outcome, counts in outcomes.items():
            feature_rel_freq = ((counts[0] + counts[1]) / total_examples)
            poison_cond_prob = (counts[1] / (counts[0] + counts[1]))
            edible_cond_prob = 1 - poison_cond_prob
            if not poison_cond_prob == 0 and not edible_cond_prob == 0:
                conditional_entropy += feature_rel_freq * (
                        poison_cond_prob * math.log2(poison_cond_prob) + edible_cond_prob * math.log2(edible_cond_prob))
        conditional_entropy = -1 * conditional_entropy
        return conditional_entropy

    def find_best_attribute(self):
        # define entropy
        # create empty list to later hold all information gains for every attribute
        ig_list = []
        # create loop to find information gain for every attribute (every column) and add it to the list
        for i in range(self.examples.shape[1]):
            if i > 0:
                print(self.examples)
                print('entropy:' + str(self.entropy))
                conditional_entropy = self.con_entropy(i)
                print('conditional entropy:' + str(conditional_entropy))
                information_gain = self.entropy - conditional_entropy
                print('information gain:' + str(information_gain))
                # print('information gain:' + str(information_gain))
                ig_list.append(information_gain)
                # print('list of IG values' + str(ig_list))
        # print(ig_list)
        info_gain_dict = dict(zip(attributes_list, ig_list))
        # print(info_gain_dict)
        best_attribute_col = max(info_gain_dict, key=info_gain_dict.get)
        conditional_entropy = self.entropy - info_gain_dict[best_attribute_col]
        # print('best attribute to split on:', str(best_attribute))
        best_attribute_index = attributes_list.index(best_attribute_col) + 1
        best_attribute_col = self.examples[:, best_attribute_index]
        best_attribute_name = max(info_gain_dict, key=info_gain_dict.get)
        # print('index of best attribute in dataset:', best_attribute_index)
        # print('best attribute data:' + str(best_attribute))
        return best_attribute_name, best_attribute_index, best_attribute_col, ig_list, info_gain_dict, conditional_entropy

    def split_node(self):
        # get best split
        best_attribute_name, best_idx, best_attribute, ig_list, info_gain_dict, conditional_entropy = self.find_best_attribute()
        # print('best_attribute column found in from previous function:', str(best_attribute))
        # split data based on the unique value of the best attribute
        unique_val_of_best_attribute = []
        for unique_val in np.unique(best_attribute):
            # print('unique value:', unique_val)
            unique_val_of_best_attribute.append(unique_val)
            split = np.empty((0, 3), int)
            for example in self.examples:
                if example[best_idx] == unique_val:
                    # print(row)
                    split = np.append(split, np.array([example]), axis=0)
            child = Node(unique_val_of_best_attribute[unique_val], split)
            print('conditional entropy befoer entropy assignment:' + str(conditional_entropy))
            child.entropy = conditional_entropy
            self.children[unique_val_of_best_attribute[unique_val]] = child
            # print('Node name:', str(unique_val_of_best_attribute[unique_val]))
            # print('list of unique values for the best attribute to split on:', unique_val_of_best_attribute)
            # print('examples in dataset with that unique value of the attribute:')

    def partition_children(self):
        best_attribute_name, best_attribute_index, best_attribute, ig_list, info_gain_dict, conditional_entropy = self.find_best_attribute()
        if abs(info_gain_dict[best_attribute_name]) < 0.001:
            return
        if abs(self.entropy) < 0.001:
            return
        print('examples: ' + str(self.examples))
        print(info_gain_dict[best_attribute_name])
        print(info_gain_dict)
        for idx, child in self.children.items():
            child.split_node()
            child.partition_children()


if __name__ == "__main__":
    all_examples = pd.read_csv('Data/example_data', header=None)
    all_examples = all_examples.values
    root_node = Node("root", all_examples)
    root_node.split_node()
    root_node.partition_children()








