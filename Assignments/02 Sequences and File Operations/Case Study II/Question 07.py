"""
7.
Please write a program that counts and prints the numbers of each character in a string input by the console.
Example: If the following string is given as input to the program:
	abcdefgabc
Then, the output of the program should be:
	a,2
	c,2
	b,2
	e,1
	d,1
	g,1
	f,1
"""

def char_counter(user_str):
    """Counts the character occurrences in the given string

    Args:
        user_str (str): User input

    Returns:
        dict: character as key and it's count as value.
    """    
    
    counts = {}

    for char in user_str:
        counts[char] = counts.get(char, 0) + 1

    return counts


if __name__ == '__main__':
    counts = char_counter(input())
    for char, count in counts.items():
        print(char, count, sep=",")