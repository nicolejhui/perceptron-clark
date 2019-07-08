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
        self.entropy = 1
        # split feature holds the name of the feature that was split on to create this node (i.e. odor)
        self.split_feature = None
        self.info_gain_dict = {}
        self.depth = None
        # self.best_indx = None
        # self.best_attribute = []

    def get_entropy(self):
        label, label_counts = np.unique(self.examples[:, 0], return_counts=True)
        # print(label, label_counts)
        label1_prob = label_counts[0] / self.examples.shape[0]
        label2_prob = label_counts[1] / self.examples.shape[0]
        # print(label1_prob, label2_prob)
        out = - (label1_prob * (np.log2(label1_prob)) + (label2_prob * (np.log2(label2_prob))))
        # print(out)
        return out

    def con_entropy(self, attribute_col):
        # create empty dictionary which will hold unique values as keys and the probability of y being a certain label
        # when example is that unique value
        conditional_array = {}
        # print('attribute column:', str(attribute_col))
        for example in self.examples:
            # print('example:', str(example))
            if example[attribute_col] not in conditional_array:
                conditional_array[example[attribute_col]] = [0, 0]
            if example[0] == '+':
                conditional_array[example[attribute_col]][0] += 1
            if example[0] == '-':
                conditional_array[example[attribute_col]][1] += 1
        # print('conditional array:', str(conditional_array))
        # initialize conditional_entropy svo we can add to it
        conditional_entropy = 0
        for unique_var, counts, in conditional_array.items():
            # print('unique variable:', str(unique_var))
            # print('counts:', str(counts))
            frequency = (counts[0] + counts[1]) / self.examples.shape[0]
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
        # create empty list to later hold all information gains for every attribute
        ig_list = []
        # create loop to find information gain for every attribute (every column) and add it to the list
        for i in range(self.examples.shape[1]):
            if i > 0:
                # print('i:', str(i))
                print('-------NEXT ATTRIBUTE----------')
                print('example data used:', str(self.examples))
                print('entropy:' + str(self.entropy))
                conditional_entropy = self.con_entropy(i)
                print('conditional entropy:' + str(conditional_entropy))
                information_gain = self.entropy - conditional_entropy
                print('information gain:' + str(information_gain))
                # print('information gain:' + str(information_gain))
                ig_list.append(information_gain)
                # print('list of IG values' + str(ig_list))
        print('info gain list:', ig_list)
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
        # print('info gain dictionary:', str(info_gain_dict))
        print('best attribute:', str(best_attribute_name))
        print('info gain of', str(best_attribute_name), ':', str(info_gain_dict[best_attribute_name]))
        return best_attribute_name, best_attribute_index, best_attribute_col, ig_list, info_gain_dict, conditional_entropy

    def split_node(self):
        print('-----------------------------------NEXT CALL OF split_node--------------------------------------')
        # get best split
        print(str('STOP CONDITION CHECK. ENTROPY IS: ' + str(self.entropy)))
        if abs(self.entropy) < 0.001:
            print('entropy is 0')
            return
            # child.split_node()
            # if self.best_attribute_name:

        best_attribute_name, best_idx, best_attribute, ig_list, info_gain_dict, conditional_entropy = self.find_best_attribute()

        if self.split_feature is not None:
            print('INFO GAIN: ' + str(self.info_gain_dict))
            if self.info_gain_dict[self.split_feature] < 0.001:
                print('info gain is 0')
                return
        # print('best_attribute column found in from previous function:', str(best_attribute))
        # split data based on the unique value of the best attribute
        # info_gain_dict = self.info_gain_dict
        # best_attribute_name = self.best_attribute_name
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
            print(child, child.name)
            # print('conditional entropy before entropy assignment:' + str(conditional_entropy))
            child.entropy = child.con_entropy(best_idx)
            child.info_gain_dict = info_gain_dict
            child.split_feature = best_attribute_name
            '''if abs(child.entropy) < 0.001:
                print('entropy is 0')
                return
            # child.split_node()
            # if self.best_attribute_name:
            if info_gain_dict[best_attribute_name] < 0.001:
                print('info gain is 0')
                return'''
            #child.split_node()
            #michael also commented out the line above
            # michael changed the line below hes probably wrong
            self.children[unique_val_of_best_attribute[unique_val]] = child
            # print(child, child.children)
            # print('Node name:', str(unique_val_of_best_attribute[unique_val]))
            # print('list of unique values for the best attribute to split on:', unique_val_of_best_attribute)
            # print('examples in dataset with that unique value of the attribute:')
            # print(self.children)
            # print('examples: ' + str(self.examples))

    '''def partition_children(self): 
        info_gain_dict = self.info_gain_dict
        best_attribute_name = self.best_attribute_name
        if abs(self.entropy) < 0.001:
            return
        if info_gain_dict[best_attribute_name] < 0.001:
            return
        # print('examples: ' + str(self.examples))
        print('best attribute:', str(best_attribute_name))
        print(info_gain_dict[best_attribute_name])
        print(info_gain_dict)
        for idx, child in self.children.items():
            child.split_node()
            child.partition_children()'''

    #def build_tree(self, child, examples, used_feature, used_feature_values):
    def build_tree(self):
        '''best_attribute_name, best_idx, best_attribute, ig_list, info_gain_dict, conditional_entropy = self.find_best_attribute()
        used_feature = best_idx
        used_feature_values = np.unique(best_attribute)'''
        self.split_node()
        #print('children: ' + self.children.items())
        for yeet, child in self.children.items():
            child.build_tree()



if __name__ == "__main__":
    all_examples = pd.read_csv('Data/example_data', header=None)
    all_examples = all_examples.values
    root_node = Node("root", all_examples)
    root_node.build_tree()
    #michael changed it





