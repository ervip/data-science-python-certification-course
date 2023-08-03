"""
Write a program that will find factors of the given number and find whether the factor is even or odd.
Hint:Use Loop with if-else statements
"""

def odd_even_factors(number):
    """Finds the factors of the given number
    
    Args:
        number (int): Number for which factors needs to be found out
    
    Returns:
        Factors categorized as even, odd in dict
    """

    factors = dict(odd=[], even=[])
    for n in range(1, number+1):
        if number % n == 0:
            if n & 1:
                factors['odd'].append(n)
            else:
                factors['even'].append(n)
    return factors

if __name__ == '__main__':
    user_input = int(input())
    factors = odd_even_factors(user_input)
    for factor_type, factors_list in factors.items():
        print(factor_type, factors_list)