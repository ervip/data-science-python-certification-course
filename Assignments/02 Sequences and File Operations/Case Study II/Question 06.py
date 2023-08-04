"""
Please write a program that accepts a string from the console and print it in reverse order.
Example: If the following string is given as input to the program: 
	rise to vote sir
Then, the output of the program should be:
	ris etov ot esir
"""

def solution(user_string):
    print(user_string[::-1])


if __name__ == '__main__':
    solution(input())