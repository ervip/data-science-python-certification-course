"""
Domain
    Banking Marketing

focus
    Optimization

Business challenge/requirement
    Bank of Portugal runs a marketing campaign to offer loans to clients. The loan is 
    offered to only clients with particular professions. A list of successful campaigns
    (with client data) is given in the attached dataset. You have to come up with a 
    program that reads the file and builds a set of unique profession lists and gives input 
    profession of the client - the system tells whether the client is eligible to be 
    approached for a marketing campaign.

Key issues
    Caller can only make x number of cold calls in a day. Hence to increase her 
    effectiveness only eligible customers should be called

Considerations
    The current system does not differentiate clients based on age and profession

Data volume
    447 records in bank-data.csv

Additional information
    - NA

Business benefits
    The company can achieve between 15% to 20% higher conversion by targeting the 
    right clients

Approach to Solve
    You have to use the fundamentals of Python taught in module 2
        1. Read file bank-data.csv
        2. Build a set of unique jobs
        3. Read the input from the command line - profession
        4. Check if the profession is on the list
        5. Print whether the client is eligible

Enhancements for code
    You can try these enhancements in code
        1. Compute max and min age for loan eligibility based on data in CSV file
        2. Store max and min age in the dictionary
        3. Make the professional check case insensitive 
        4. Currently program ends after the check. Take the input in the while loop and 
        end only if the user types "END" for the profession
"""

import os

unique_jobs = {}

with open(os.path.join(os.path.dirname(__file__), 'resources', 'bank-data.csv'), 'r') as f:
    lines = [line.strip().split(",") for line in f.readlines()]
    
    # Header
    age_index, job_index, marital_index, eligible_index = 0, 1, 2, 3

    for row in lines[1:]:
        if row[eligible_index] not in ('yes', 'y'):
            continue

        profession = row[job_index].lower()
        age = int(row[age_index])

        if profession not in unique_jobs:
            unique_jobs[profession] = dict(min=age, max=age)
        else:
            if age < unique_jobs[profession]["min"]:
                unique_jobs[profession]["min"] = age
            elif age > unique_jobs[profession]["max"]:
                unique_jobs[profession]["max"] = age

while True:
    profession = input("Profession: ").strip().lower()
    
    if profession.lower() == 'END':
        break
    
    age = int(input("Age: "))
    eligible = profession in unique_jobs and unique_jobs[profession]["min"] <= age <= unique_jobs[profession]["max"]
    print("Eligible:", eligible)