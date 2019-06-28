import numpy as np
import pandas as pd

data = pd.read_csv('Data/example_data', header=None)
data = data.values


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.split = None


def entropy(label):
    label, label_counts = np.unique(data[:, 0], return_counts=True)
    # print(label, label_counts)
    label1_prob = label_counts[0] / data.shape[0]
    label2_prob = label_counts[1] / data.shape[0]
    # print(label1_prob, label2_prob)
    entropy = - (np.sum((label1_prob * (np.log2(label1_prob)) + (label2_prob* (np.log2(label2_prob))))))
    # print(entropy)
    return entropy


def con_entropy(feature_col):
    labels = data[:, 0]
    # print(labels)
    data_points = data[:, 1:]
    # print(data_points)
    for i in range(data.shape[1] - 1):
        feature_type, feature_count = np.unique(data[:, i + 1], return_counts=True)
        # print(feature_count)
        feature_dict = dict(zip(feature_type, feature_count))
        # print(feature_dict)
    conditional_array = {}
    for example in data:
        if example[feature_col] not in conditional_array:
            conditional_array[example[feature_col]] = [0, 0]
        if example[0] == '+':
            conditional_array[example[feature_col]][0] += 1
        if example[0] == '-':
            conditional_array[example[feature_col]][1] += 1
    # print(conditional_array)
    # print(frequency) (ends up being [.5, .5])
    conditional_entropy = 0
    for unique_var, counts, in conditional_array.items():
        frequency = (counts[0] + counts[1]) / data.shape[0]
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
        # print(label1_log_prob)
        # print(label2_log_prob)
        # print('freq:' + str(frequency))
        # print('sum: ' + str((label1_log_prob + label2_log_prob)))
        # print('cond e: ' + str(conditional_entropy))
        conditional_entropy += frequency * (label1_log_prob + label2_log_prob)
        # print('con entropy:' + str(conditional_entropy))
    conditional_entropy = -1 * conditional_entropy
    # print(conditional_entropy)
    return conditional_entropy


def best_information_gain(column, entropy, conditional_entropy):
    information_gain = 0
    for i in range(num_col):
        if i > 0:
            # print(entropy)
            # print(conditional_entropy)
            previous_information_gain = information_gain
            print('previous info gain:' + str(previous_information_gain))
            information_gain = entropy - conditional_entropy
    # print(information_gain)



if __name__ == "__main__":
    entropy = entropy(data)
    # print(entropy)
    num_col = data.shape[1]
    for i in range(num_col):
        if i > 0:
            con_entropy(i)
            conditional_entropy = con_entropy(i)
            # print(conditional_entropy)
            best_information_gain(num_col, entropy, conditional_entropy)

