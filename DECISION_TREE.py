import numpy as np
import pandas as pd

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

    def get_entropy(self):
        label, label_counts = np.unique(self.examples[:, 0], return_counts=True)
        # print(label, label_counts)
        label1_prob = label_counts[0] / self.examples.shape[0]
        label2_prob = label_counts[1] / self.examples.shape[0]
        # print(label1_prob, label2_prob)
        out = - (np.sum((label1_prob * (np.log2(label1_prob)) + (label2_prob * (np.log2(label2_prob))))))
        # print(out)
        return out

    def con_entropy(self, feature_col):
        # create empty dictionary which will hold unique values as keys and the probability of y being a certain label
        # when example is that unique value
        conditional_array = {}
        for example in self.examples:
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

    def find_best_attribute(self):
        # define entropy
        entropy = self.get_entropy()
        # create empty list to later hold all information gains for every attribute
        ig_list = []
        # create loop to find information gain for every attribute (every column) and add it to the list
        for i in range(self.examples.shape[1]):
            if i > 0:
                conditional_entropy = self.con_entropy(i)
                information_gain = entropy - conditional_entropy
                # print('information gain:' + str(information_gain))
                ig_list.append(information_gain)
                # print('list of IG values' + str(ig_list))
            info_gain_dict = dict(zip(attributes_list, ig_list))
            # print(info_gain_dict)
        best_attribute = max(info_gain_dict, key=info_gain_dict.get)
        if info_gain_dict[best_attribute] < 0.001:
            raise ValueError('The information gain is zero.')
        # print('best attribute to split on:', str(best_attribute))
        best_attribute_index = attributes_list.index(best_attribute) + 1
        best_attribute = all_examples[:, best_attribute_index]
        # print('index of best attribute in dataset:', best_attribute_index)
        # print('best attribute data:' + str(best_attribute))
        return best_attribute_index, best_attribute, ig_list, info_gain_dict

    def split_node(self):
        # get best split
        best_idx, best_attribute, ig_list, info_gain_dict = self.find_best_attribute()
        # print('best_attribute column found in from previous function:', str(best_attribute))
        # split data based on the unique value of the best attribute
        unique_val_of_best_attribute = []
        for unique_val in np.unique(best_attribute):
            # print('unique value:', unique_val)
            unique_val_of_best_attribute.append(unique_val)
            split = np.empty((0, 3), int)
            for example in all_examples:
                if example[best_idx] == unique_val:
                    # print(row)
                    split = np.append(split, np.array([example]), axis=0)
            child = Node(unique_val_of_best_attribute[unique_val], split)
            self.children[unique_val_of_best_attribute[unique_val]] = child
            # print('Node name:', str(unique_val_of_best_attribute[unique_val]))
            # print('list of unique values for the best attribute to split on:', unique_val_of_best_attribute)
            # print('examples in dataset with that unique value of the attribute:')

    def partition_children(self):
        for idx, child in self.children.items():
            child.split_node()
            child.partition_children()


if __name__ == "__main__":
    all_examples = pd.read_csv('Data/example_data', header=None)
    all_examples = all_examples.values
    root_node = Node("root", all_examples)
    root_node.split_node()
    root_node.partition_children()








