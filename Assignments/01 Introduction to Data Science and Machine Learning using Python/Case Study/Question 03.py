"""
Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input. Divide each digit with 2 and verify is it even or not.
"""

def is_all_digits_even(number):
    """Checks whether the number has all even digits

    Args:
        number (int): Number to check for

    Returns:
        bool: True if all digits are even
    """
    
    while number > 0:
        if (number % 10) & 1:
            return False
        number //= 10
    return True


if __name__ == '__main__':
    user_input = input("START and END separated by space: ")
    start, end = map(int, user_input.split())
    for n in range(start, end + 1):
        if is_all_digits_even(n):
            print(n, end=",")