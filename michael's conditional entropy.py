import math
import numpy as np
import pandas as pd

data = pd.read_csv('Data/example_data', header=None)
# The feature parameter takes an int which corresponds to the index value of the relevant feature in each row of the
# dataset. By "relevant feature", I mean the feature which we want to find conditional entropy with respect to-- which
# is represented by X in the conditional entropy formula.

# The examples parameter takes an array of examples which are relevant at the current node.
# For instance, if 'color' and 'size' have already been split on in parent nodes, the example subset might only contain
# examples with the feature values 'red' and 'small'.


def get_conditional_entropy(feature, examples):
    # Outcomes is a dict, with the keys being specific values that a feature takes (i.e. red) and
    # the values being lists containing the counts of features with that value that are poisonous or edible.
    # For example, {'r':[2,2],'b':[0:4]} could correspond to there being 4 red mushrooms, 2 edible and 2 poisonous,
    # and 4 blue mushrooms, 0 edible and 4 poisonous.
    outcomes = {}
    # total_examples counts how many examples there are in the whole set of examples.
    total_examples = 0
    # The following loop counts how many examples with a given feature are poisonous.
    for example in examples:
        feature_value = example[feature]
        if feature_value not in outcomes:
            outcomes[feature_value] = [0, 0]
        if example[0] == 'e':
            outcomes[feature_value][0] += 1
        if example[0] == 'p':
            outcomes[feature_value][1] += 1
        total_examples += 1
        print(outcomes)

    conditional_entropy = 0
    for outcome, counts in outcomes.items():
        # feature_rel_freq corresponds to the P(X=x) part of the conditional entropy formula;
        # It is calculated by dividing the number of examples with a given feature values by the total # of examples
        feature_rel_freq = ((counts[0] + counts[1]) / total_examples)
        # poison_cond_prob corresponds to the P(Y=y|X=x) part of the conditional entropy formula;
        # It is calculated by dividing the number of poisonous examples with a given feature by the total number of
        # examples with that feature
        poison_cond_prob = (counts[1] / (counts[0] + counts[1]))
        edible_cond_prob = 1 - poison_cond_prob
        if poison_cond_prob == 0 or edible_cond_prob == 0:
            pass
        else:
            conditional_entropy += feature_rel_freq * (
                poison_cond_prob * math.log2(poison_cond_prob) + edible_cond_prob * math.log2(edible_cond_prob))
    conditional_entropy = -1 * conditional_entropy
    return [conditional_entropy, outcomes]

# The function returns a list containing both the conditional entropy and the outcomes dict.
# Idk if you'll need the outcomes dict in your code, but I ended up needing it for something else later.
