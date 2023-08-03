"""
Write a program that accepts a sentence and calculates the number of letters and digits.
Suppose if the entered string is:Python0325 
Then the output will be:
LETTERS: 6
DIGITS: 4
"""

def dl_counter(sentence):
    """Counts the letters and digits in the given sentence.
    Note: All the special characters including space will be counted in 'others' key.

    Args:
        sentence (str): Sentence for which you need to count digits and letters

    Returns:
        dict: Counts categorized as digits, letters, others in a dict
    """

    counts = dict(digits=0, letters=0, others=0)
    for char in sentence:
        if char.isdigit():
            counts['digits'] += 1
        elif char.isalpha():
            counts['letters'] += 1
        else:
            counts['others'] += 1
    return counts


if __name__ == '__main__':
    user_input = input()
    counts = dl_counter(user_input)
    print("LETTERS:", counts['letters'])
    print("DIGITS:", counts['digits'])