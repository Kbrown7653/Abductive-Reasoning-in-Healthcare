import pandas as pd
import numpy as np
from scipy.spatial.distance import euclidean

def give_prognosis_entire_df(sorted_prob_df,test_no_prog):
    probability_df = sorted_prob_df
    # for vector ops the columns must be the same and in same order
    are_cols_same = list(test_no_prog.columns) == list(probability_df.columns)
    if are_cols_same:
        all_progs = []
        for i in range(test_no_prog.shape[0]):
            s = test_no_prog.iloc[i]
            distances = probability_df.apply(lambda row: euclidean(row, s), axis=1).sort_values()
            print(distances)

            # Calculate the absolute distance and check if all are less than 1 for each row
            mask = probability_df.apply(lambda row: (abs(row - s) < 1).all(), axis=1)

            # Filter rows based on the mask
            filtered_df = probability_df[mask]

            # Each index has a true deduction value
            # We return them based on their euclidean distance
            prognosis = list(filtered_df.index)

            prog_dict = {}
            for j in prognosis:
                prog_dict[j] = distances.loc[j]
            sorted_prog = []
            length = len(prog_dict.values())
            for k in range(length):
                min_key = min(prog_dict, key=prog_dict.get)
                sorted_prog.append(min_key)
                prog_dict.pop(min_key)
            all_progs.append(sorted_prog)
        return all_progs
    else:
        return "Invalid DataFrame's"


def element_in_set(list_predicted_set,actual_element):
    assert (len(list_predicted_set) == len(actual_element))
    correct = 0
    for i in range(len(actual_element)):
        prog_set = set(list_predicted_set[i])
        if actual_element[i] in prog_set:
            correct += 1
    return correct/len(actual_element)


# df comes in sorted but for redundancy we sort again
probability_df = pd.read_csv('Data/Training_Data_Vectors.csv',index_col=0)
sorted_prob_df = probability_df.sort_index(axis=1)

# testing_Df to test the quality of out model
test_df = pd.read_csv('Data/Testing.csv').sort_index(axis=1)
test_no_prog = test_df.copy().drop(columns='prognosis',axis=1)

progonsis_test_df_results = give_prognosis_entire_df(sorted_prob_df, test_no_prog)

actual = list(test_df['prognosis'])

print(f'Accuracy:\t{element_in_set(progonsis_test_df_results, actual)}\n\n Trials:\t{len(actual)}')
