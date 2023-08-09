"""
Domain
    E-Commerce

focus
    Optimization

Business challenge/requirement
    GoodsKart—the largest eCommerce company in Indonesia with revenue of $2B+ 
    acquired another eCommerce company FairDeal. FairDeal has its own IT system to 
    maintain records of customers, sales, etc. For ease of maintenance and cost savings 
    GoodsKart is integrating customer databases of both organizations hence customer 
    data of FairDeal has to be converted in GoodsKart Customer Format.

Key issues
    GoodsKart customer data has more fields than in FairDeal customer data. Hence 
    FairDeal data needs to be split and stored in GoodsKart Customer Object-Oriented
    Data Structure

Considerations
    The system should convert the data at run time

Data volume
    - NA

Additional information
    - NA

Business benefits
    GoodsKart can eventually sunset the IT systems of FairDeal and reduce IT cost by 20-
    30% 

Approach to Solve
    You have to use the fundamentals of Python taught in module 2
        1. Read FairDealCustomerData.csv
        2. Name field contains full name - use a regular expression to separate title, first 
        name, last name
        3. Store the data in Customer Class
        4. Create Custom Exception - CustomerNotAllowedException
        5. Pass a customer to function "createOrder" and throw 
        CustomerNotAllowedException in case of blacklisted value is 1

Enhancements for code
    You can try these enhancements in code
        1. Change function createOrder to take product name and product code as input
        2. Create Class Order
        Return object of type Order in case customer is eligible

"""


# Unable to understand the requirements !!