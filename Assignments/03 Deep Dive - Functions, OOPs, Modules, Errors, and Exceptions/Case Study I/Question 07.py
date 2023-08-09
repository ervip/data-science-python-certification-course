"""
Write a program that can compute the factorial of a given number. 
Use recursion to find it. 
Hint: 
    Suppose the following input is supplied to the program: 8
    Then, the output should be: 40320
"""

def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)


if __name__ == '__main__':
    user_input = int(input("Number: "))
    print(fact(user_input))