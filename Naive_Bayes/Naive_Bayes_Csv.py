import pandas as pd
import numpy as np
from collections import defaultdict
from pprint import pprint

# test_df = pd.DataFrame(np.random.randint(1,5,40).reshape(10,4) , columns=["outlook","temperature","humidity","windy"])
test_df = pd.read_csv("training.csv", names=["outlook","temperature","humidity","windy","play"])

total_observation = test_df.shape[0]
print(test_df)


def get_priors_likelihood():
    """
    :return: priors - dict
                key - class
                val - dict
                    key - column name
                    val - dict
                        key - column value
                        val - probability of that value for given class.
            e.g {0: {'humidity': {1: 0.66666666666666663, 2: 0.33333333333333331},
                    'outlook': {1: 0.33333333333333331,
                                2: 0.5,
                                 4: 0.16666666666666666}}
            likelihood - dict
                key - class
                val - probability of that class
    """
    likelihood = dict(test_df["play"].value_counts())
    priors = defaultdict(dict)
    for key, val in likelihood.items():
        for column in test_df.columns:
            if column is not "play":
                priors[key][column] = dict(test_df.loc[test_df["play"] == key, column].value_counts()/val)

    for key, val in likelihood.items():
        likelihood[key] = float(val/total_observation)
    return priors, likelihood


def shall_we_play(*l):
    """
    :param l: 2,3,2,1 - outlook-2,temperature-2,humidity-4,windy-1
    Closely look at float(val_dict[name].get(l[idx], 1e-3))
    This is needed as there is a chance that 2 doesn't occur in windy in
    case of class 0, If that happens we may get fucked up by KeyError
    If we get 0 in that case, whole multiplication is 0,
    So we are setting a value close to 0, to indicate the fact that this value doesn't exist in given class.
    We CAN NOT do except KeyError as in that case we would not multiply anything, and that would lead to wrong answers.
    As all the values are < 1, thus by not multiplying we are multiplying by 1, that is utterly wrong
    :return: string - DO NOT PLAY
                      YAY PLAY
    """
    priors, likelihood = get_priors_likelihood()
    value = 1
    maximum = (0,0)
    for key, val_dict in priors.items():
        for idx, name in enumerate(test_df.columns[:-1]):
            print("For class {} Column {} Value {}".format(key, name, val_dict[name].get(l[idx], 1e-3)))
            value *= float(val_dict[name].get(l[idx], 1e-3))
        value *= float(likelihood[key])
        if value > maximum[1]:
            maximum = (key, value)
            print(maximum)
        value = 1
    if maximum[0] == 0:
        print("DO NOT PLAY")
    else:
        print("YAY PLAY")

pprint(get_priors_likelihood())
shall_we_play(3,3,4,4)
