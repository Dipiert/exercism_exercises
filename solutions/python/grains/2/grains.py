def square(number):
    if number <= 0 or number >= 65:
        raise ValueError("Square number should be greater than 0 and lesser than 65")

    if number in (1, 2):
        return number

    return 2**(number-1)


def total():
    return 2**64-1
