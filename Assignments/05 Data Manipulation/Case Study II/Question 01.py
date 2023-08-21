"""
Domain 
    HR

focus
    Insights from data

Business challenge/requirement
    SFO Public Department - referred to as SFO has captured all the salary data of its 
    employees from the year 2011-2014. Now we are in the year 2015 and the 
    organization is facing a financial crisis. As the first step HR wants to rationalize 
    employee costs to save the payroll budget. You have to do data manipulation and 
    analysis on the salary data to answer specific questions for cost savings.

Key issues
    Cost can be saved by figuring out the key pockets of high salaries

Considerations
    NONE

Data volume
    - Approx 150K records across files

additional information
    - NA

Business benefits
    Save at least 10% of employee costs by identifying and letting them go

Approach to Solve
    You have to use the fundamentals of Pandas covered in module 6 and answer the 
    following 5 Questions
        1. Compute how much total salary cost has increased from the year 2011 to 2014
        2. Which Job Title in the Year 2014 has the highest mean salary?
        3. How much money could have been saved in the Year 2014 by stopping 
            OverTimePay?
        4. Which are the top 5 common jobs in the Year 2014 and how much do they cost 
            SFO?
        5. Who was the top earning employee across all the years?

Enhancements for code
    You can try these enhancements in code
        1. Which are the last 5 common jobs in the Year 2014 and how much do they cost 
        SFO?
        2. In year 201 OverTimePay was what percentage of TotalPayBenefits
        3. Which Job Title in the Year 2014 has the lowest mean salary?

"""

import os
import pandas as pd


df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'resources', 'Salaries.csv'))


# Answer 1
tdf = df.filter(['Year', 'TotalPay']).groupby('Year', as_index=False).sum()
diff = float(tdf[tdf['Year'] == 2014]['TotalPay']) - float(tdf[tdf['Year'] == 2011]['TotalPay'])
diff_in_percent = (diff / float(tdf[tdf['Year'] == 2011]['TotalPay'])) * 100
print("Increased From 2011 to 2014:", diff, diff_in_percent)



# Answer 2
tdf = df[df['Year'] == 2014].filter(['JobTitle', 'TotalPay']).groupby('JobTitle', as_index=False).mean().max()
print(tdf)


# Answer 3
total_pay_in_2014 = df[df['Year'] == 2014]['TotalPay'].sum()
ot_pay_in_2014 = df[df['Year'] == 2014]['OvertimePay'].sum()
print("Amount could be saved by stopping overtime pay in 2014:", total_pay_in_2014 - ot_pay_in_2014)


# Answer 4
tdf = df[df['Year'] == 2014].filter(['JobTitle', 'TotalPay'])
common_jobs = tdf['JobTitle'].value_counts().sort_values(ascending=False)
for job in common_jobs.keys()[:5]:
    print("JobTitle: {0:50} Cost to SFO: {1:20.2f}".format(job, tdf[tdf['JobTitle'] == job]['TotalPay'].sum()))



# Answer 5
tdf = df[df['TotalPay'] == df['TotalPay'].max()]
print("People having highest pay across all the years")
for index in range(len(tdf)):
    print(tdf.iloc[index]['EmployeeName'], tdf.iloc[index]['TotalPay'])