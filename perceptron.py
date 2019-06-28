import numpy as np
import pandas as pd
import math

data = pd.read_csv('Data/mystery.data', header=None)
data = data.values

training_set = data[0:800]
testing_set = data[801:1000]


def update_weight_bias(training_examples, previous_weight, learning_rate, previous_bias):
    helper_vector = np.zeros((4))
    for example in training_examples:

        y = example[4]
        x = example[0:4]
        helper_vector += (y * x) * ((y * (np.dot(previous_weight.T, x) + previous_bias)) < 0).astype('int')

    weight = previous_weight + learning_rate * helper_vector
    # print(weight)

    helper_scalar = 0
    for example in training_examples:

        y = example[4]
        x = example[0:4]
        helper_scalar += y * int((y * (np.dot(previous_weight.T, x) + previous_bias)) < 0)
        # print(helper_scalar)

    bias = previous_bias + learning_rate * helper_scalar
    # print(bias)
    return weight, bias


def train_model(training_example, steps, learning_rate):
    i = 0
    weight = np.ones((4))
    bias = 0
    for i in range(steps):
        weight, bias = update_weight_bias(training_example, weight, learning_rate, bias)
        # if i % 10 == 0:
            # print(str(i + 1) + ": ", end="")
            # print(weight, end="\t")
            # print(bias)
    # print(weight, bias)
    return weight, bias


def evaluate():
    correct_count = 0
    incorrect_count = 0
    for example in testing_set:
        #print(solution(example[0:4]))
        #print(example[4])
        if solution(example[0:4]) == example[4]:
            correct_count += 1
        if solution(example[0:4]) != example[4]:
            incorrect_count += 1
    print(correct_count, incorrect_count)
    accuracy = (correct_count / 200) * 100
    print(accuracy)


if __name__ == '__main__':
    weight, bias = train_model(training_set, 3000, .03)

    def solution(x):
        return np.sign(np.dot(weight.T, x) + bias)
    evaluate()
