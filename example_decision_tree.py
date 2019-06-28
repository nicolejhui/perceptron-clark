import numpy as np
import pandas as pd

data = pd.read_csv('Data/example_data', header=None)



class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.split = None


def entropy(data):
    attr_type, attr_count = np.unique(data.values[:, 0], return_counts=True)
    keys = attr_type
    values = attr_count
    # print(keys, values)
    # prob_a and prob_b are p(Y=y)
    prob_a = values[0] / data.shape[0]
    prob_b = values[1] / data.shape[0]
    # print(prob_plus, prob_minus)
    entropy = - (np.sum((prob_a * (np.log(prob_a))) + (prob_b * (np.log(prob_b)))))
    # print(entropy)
    return entropy, prob_a, prob_b

def conditional_entropy(feature, data):
    # find prob_c, which is p(X=x)
    prob_c_list = []
    for i in range(data.shape[1] - 1):
        attr_type, attr_count = np.unique(data.values[:, i + 1], return_counts=True)
        keys = attr_type
        values = attr_count
        prob_c = values[0] / data.shape[0]
        prob_c_list.append(prob_c)
        # print(prob_c)
    # print(prob_c_list)
        # print(keys, values)
    # turn into numpy array
    data = data.values
    conditional_array = {}
    # print(data)
    # makes dictionary that contains unique value and the counts of it when it is +/-
    for example in data:
        if example[feature] not in conditional_array:
            conditional_array[example[feature]] = [0, 0]
        if example[0] == '+':
            conditional_array[example[feature]][0] += 1
        if example[0] == '-':
            conditional_array[example[feature]][1] += 1
    # print(conditional_array)
    # make two lists
    prob_d_list = []
    for key, value in conditional_array.items():
        cond_feature_count = conditional_array[key]
        # print(cond_feature_count)
        # want cond_feature_Count to go through all indexes (use for loop)
        prob_d_sublist = []
        for key, value in conditional_array.items():
            # prob_d is p(Y=y|X=x)
            prob_d = cond_feature_count[key] / (conditional_array[example[feature]][0] + conditional_array[example[feature]][1])
            prob_d_sublist.append(prob_d)
        prob_d_list.append(prob_d_sublist)
        # print(prob_d_sublist)
    # print(prob_d_list)
            # print(conditional_entropy)
    prob_log_list = []
    for prob_d_sublist in prob_d_list:
        prob_log_sublist = []
        for prob_d in prob_d_sublist:
            prob_log = prob_d * np.log(prob_d)
            # print(prob_log)
            prob_log_sublist.append(prob_log)
        prob_log_list.append(prob_log_sublist)
    # print(prob_log_list)
    log_sum_list = []
    for prob_log_sublist in prob_log_list:
        log_sum = prob_log_sublist[0] + prob_log_sublist[1]
        # print(log_sum)
        log_sum_list.append(log_sum)
    # print(log_sum_list)
    conditional_entropy = (prob_c_list[1] * log_sum_list[1])
    # print(conditional_entropy)


if __name__ == "__main__":
    entropy = entropy(data)
    print(entropy)
    for column in data:
        conditional_entropy(column + 1, data)


