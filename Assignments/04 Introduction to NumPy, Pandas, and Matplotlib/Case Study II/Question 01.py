"""
Domain 
    Education

focus 
    Data analysis

Business challenge/requirement
    You are a data analyst with the University of Cal USA (Not a machine learning expert 
    yet as you still have not completed the ML with Python Course :-)). The University 
    has data on Math, Physics, and Data Structure scores of sophomore students. This 
    data is stored in different files. The University has hired a data science company to do 
    an analysis of scores and find if there is any correlation between scores with age, 
    ethnicity, etc. Before the data is given to the company you have to do data wrangling.

Key issues
    Ensure student's identity is not revealed to the agency and only relevant data is 
    shared

Considerations
    NONE

Data volume
    - In thousands, but only around 1800 records are shared in files MathScoreTerm1.csv 
    DSScoreTerm1.csv, PhysicsScoreTerm1.csv

Additional information
    - NA

Business benefits
    University can get more students enrollment by improving their international 
    ranking through personalized courses/curricula for students

Approach to Solve
    You have to use the fundamentals of Numpy and Pandas covered in module 4. 
        1. Read the three CSV files which contain the score of the same students in term1 of each Subject
        2. Remove the name and ethnicity column (to ensure confidentiality)
        3. Fill missing score data with zero
        4. Merge the three files
        5. Change Sex(M/F) Column to 1/2 for further analysis
        6. Store the data in a new file - ScoreFinal.csv

Enhancements for code
    You can try these enhancements in code
        1. Convert ethnicity to a numerical value
        2. Fill the missing score for a student to the average of the class
"""

import os
import numpy as np
import pandas as pd


def get_file_path(file_name):
    return os.path.join(os.path.dirname(__file__), 'resources', file_name)


ds_df = pd.read_csv(get_file_path('DSScoreTerm1.csv'))
math_df = pd.read_csv(get_file_path('MathScoreTerm1.csv'))
physics_df = pd.read_csv(get_file_path('PhysicsScoreTerm1.csv'))


ds_df.drop(['Name', 'Ethinicity'], axis=1, inplace=True)
math_df.drop(['Name', 'Ethinicity'], axis=1, inplace=True)
physics_df.drop(['Name', 'Ethinicity'], axis=1, inplace=True)

ds_df['Score'].fillna(0, inplace=True)
math_df['Score'].fillna(0, inplace=True)
physics_df['Score'].fillna(0, inplace=True)


df = pd.concat([ds_df, math_df, physics_df], axis=0, ignore_index=True)
df['Sex'].replace({'M': 1, 'F': 2}, inplace=True)

df.to_csv(get_file_path('ScoreFinal.csv'), index=False)