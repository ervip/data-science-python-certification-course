"""
Design a code that will find whether the given number is a Palindrome number or not.
"""

def is_palindrome(text):
    """Checks whether the string is palindrome or not

    Args:
        text (str): Text to check

    Returns:
        bool: True if palindrome else False
    """

    start, end = 0, len(text) - 1
    while start < end:
        if text[start] != text[end]:
            return False
        start += 1
        end -= 1
    return True


if __name__ == '__main__':
    user_input = input()
    print("Palindrome:", is_palindrome(user_input))