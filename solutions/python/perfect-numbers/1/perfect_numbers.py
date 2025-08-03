def factors(number):
    return [ n for n in range(1, number) if not number % n ]
    
    
def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.") 
    
    result = sum(factors(number))
    if result == number:
        return "perfect"
    if result > number:
        return "abundant"
    if result < number:
        return "deficient"