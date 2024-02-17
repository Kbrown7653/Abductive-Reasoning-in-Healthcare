import numpy as np
import pandas as pd


# Checks range of a series
def check_range_0_1(series):
    series = series.copy()
    # Convert the column to numeric, non-convertible values become NaN
    numeric_series = pd.to_numeric(series, errors='coerce')
    # Drop NaN values that resulted from coercion
    numeric_series = numeric_series.dropna()
    return numeric_series.between(0, 1).all()


# Calculates Fuzzy Values of A Prognosis
def calculate_average_by_target(data, target_column, target_value):
    # Filter the DataFrame for rows where target_column equals target_value
    data = data.copy()
    matching_rows = data[data[target_column] == target_value]

    #drop target
    matching_rows = matching_rows.drop(columns=target_column,axis=1)

    # Calculate the mean for each column in the filtered DataFrame
    column_averages = matching_rows.mean()

    # Return the means as a Series (or you could convert it to a dictionary if preferred)
    return column_averages.sort_index()


def compile_averages_dataframe(data, target_column):

    target_values = data[target_column].unique()

    # Initialize a list to hold each target's averages Series, excluding the target column
    averages_list = []

    # Also, prepare a list for the row labels (target values)
    row_labels = []

    # Calculate averages for each target value, excluding the target column
    for value in target_values:
        averages_series = calculate_average_by_target(data, target_column, value)
        averages_list.append(averages_series)
        row_labels.append(value)

    # Convert the list of Series into a DataFrame
    averages_df = pd.DataFrame(averages_list, index=row_labels)

    return averages_df


df = pd.read_csv('Data/Training.csv')
copy = df.copy()
# Get numerics to perform range check
numeric_df = df.copy().select_dtypes(include=['number'])
filtered_columns = numeric_df.columns[numeric_df.apply(check_range_0_1)]

target_column = 'prognosis'

print(filtered_columns)

probability_df = compile_averages_dataframe(copy, target_column)
print(probability_df.shape)
print(len(set(probability_df.columns)-set(probability_df.index)))
probability_df.to_csv('Data/Training_Data_Vectors.csv')