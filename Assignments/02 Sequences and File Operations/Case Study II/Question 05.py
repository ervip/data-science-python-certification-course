"""
Please write a program that accepts a string from the console and print the characters that have even indexes.
Example: 
If the following string is given as input to the program:
	H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be:
	Helloworld
"""

def solution(user_string):
    for char in user_string[::2]:
        print(char, end="")


if __name__ == '__main__':
    solution(input())