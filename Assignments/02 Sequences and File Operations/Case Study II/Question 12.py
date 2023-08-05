"""
Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
Example:
If the following n is given as input to the program: 5
Then, the output of the program should be: 3.55
"""

def solution(n):
    result = 0
    for i in range(1, n+1):
        result += i / (i + 1)
    return result


if __name__ == '__main__':
    n = int(input())
    print(f"{solution(n):.2f}")