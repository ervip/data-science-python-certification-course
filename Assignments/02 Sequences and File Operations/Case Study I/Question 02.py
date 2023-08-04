"""
Write a code that accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
Hint: In the case of input data being supplied to the question, it should be assumed to be a console input.
"""

def sort_words_sequence(seq):
    """Sorts the word sequence alphabetically.

    Args:
        seq (str): Sequence of words

    Returns:
        str: sequence of words alphabetically sorted
    """    
    return ' '.join(sorted(seq.split()))


if __name__ == '__main__':
    user_input = input()
    print(sort_words_sequence(user_input))