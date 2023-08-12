import os
import pandas as pd


df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'resources', 'SalaryGender.csv'))

"""
1. Extract data from the given SalaryGender CSV file and store the data from each 
column in a separate NumPy array
"""

arrays = [column_content.to_numpy() for column_name, column_content in df.items()]


"""
2. Find:
    1. The number of men with a PhD
    2. The number of women with a PhD

Consideration: 1 as men, 0 as women
"""

men, women = df[df['PhD'] == 1]['Gender'].value_counts()
print(men, women)


"""
3. Use SalaryGender CSV file. Store the “Age” and “Ph.D.” columns in one DataFrame 
and delete the data of all people who don't have a PhD
"""

df3 = df[['Age', 'PhD']]
df3 = df3[~(df['PhD'] == 0)]
print(df3)


"""
4. Calculate the total number of people who have a Ph.D. degree from the 
SalaryGender CSV file.
"""

print(len(df[df['PhD'] == 1]))