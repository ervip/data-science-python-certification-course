import numpy as np
import pandas as pd
from pandas.core.common import flatten


# 6.1 From the raw data below create a Pandas Series
pds = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(pds.map(str.lower, na_action='ignore'))
print(pds.map(str.upper, na_action='ignore'))
print(len(pds))


# 6.2  From the raw data below create a Pandas Series
pds = pd.Series([' Atul', 'John ', ' jack ', 'Sam'])
print(pds.map(str.strip, na_action='ignore'))
print(pds.map(str.lstrip, na_action='ignore'))
print(pds.map(str.rstrip, na_action='ignore'))


# 6.3 Create a series from the raw data below
pds = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(list(flatten(pds.map(lambda x: x.split('_'), na_action='ignore'))))


# 6.4 Create a series and replace either X or dog with XX-XX
pds = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
print(pds.map(lambda x: str(x).replace('X', 'XX-XX')).replace('dog', 'XX-XX'))


# 6.5 Create a series and remove the dollars from the numeric values
pds = pd.Series(['12', '-$10', '$10,000'])
print(pds.map(lambda x: x.replace('$', '')))


# 6.6  Create a series and reverse all lower case words
pds = pd.Series(['India 1998', 'big country', np.nan])
print(pds.map(lambda x: x[::-1] if x is not np.nan and str(x).islower() else x))


# 6.7 Create pandas series and print true if the value is alphanumeric in series or false if the value is not alphanumeric in series.
pds = pd.Series(['1', '2', '1a', '2b', '2003c'])
print(pds.map(lambda x: str(x).isalnum()))


# 6.8 Create pandas series and print true if the value is containing ‘A’
pds = pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'])
print(pds.map(lambda x: 'A' in str(x)))


# 6.9 Create pandas series and print in three columns value 0 or 1 is a or b or c exists in values
pds = pd.Series(['a', 'a|b', np.nan, 'a|c'])
print(pds.map(str).map(lambda x: x != 'nan' and ('a' in x or 'b' in x or 'c' in x)))


# 6.10 Create pandas dataframe having keys and ltable and rtable as below -
df1 = pd.DataFrame({'key': ['One', 'Two'], 'ltable': [1, 2]})
df2 = pd.DataFrame({'key': ['One', 'Two'], 'rtable': [4, 5]})
print(df1.merge(df2, on='key'))