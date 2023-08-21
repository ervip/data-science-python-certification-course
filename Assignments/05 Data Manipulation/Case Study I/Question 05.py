import os
import pandas as pd


CURRENT_PATH = os.path.dirname(__file__)


# 5.1 From the raw data below create a data frame
data = {
    'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
    'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
    'age': [42, 52, 36, 24, 73], 
    'preTestScore': [4, 24, 31, ".", "."],
    'postTestScore': ["25,000", "94,000", 57, 62, 70]
}
df = pd.DataFrame(data)


# 5.2 Save the dataframe into a CSV file as example.csv
df.to_csv(os.path.join(CURRENT_PATH, 'example.csv'), index=False)


# 5.3 Read the example.csv and print the data frame
_ = pd.read_csv(os.path.join(CURRENT_PATH, 'example.csv'))
print(_)


# 5.4 Read the example.csv without the column heading
_ = pd.read_csv(os.path.join(CURRENT_PATH, 'example.csv'), header=None)
print(_)


# 5.5 Read the example.csv and make the index columns 'First Name’ and 'Last Name'
_ = pd.read_csv(os.path.join(CURRENT_PATH, 'example.csv'), index_col=['first_name', 'last_name'])
print(_)


# 5.6 Print the data frame in a Boolean form as True or False. True for Null/ NaN values and false for non-null values
print(df.astype(bool).replace([True, False], [False, True]))


# 5.7 Read the dataframe by skipping the first 3 rows and print the data frame
_ = pd.read_csv(os.path.join(CURRENT_PATH, 'example.csv'), skiprows=3)
print(_)


# 5.8
"""
Load a CSV file while interpreting "," in strings around numbers as thousands
of separators. Check the raw data 'postTestScore' column has, as thousands 
separator. A comma should be ignored while reading the data. It is the default behavior, 
but you need to give an argument to the read_csv function which makes sure commas are ignored.
"""
_ = pd.read_csv(os.path.join(CURRENT_PATH, 'example.csv'), thousands=',')
print(_)