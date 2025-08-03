def is_even(number):
    return number % 2 == 0


def steps(number):
    steps = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while number != 1:
        number = number // 2 if is_even(number) else number * 3 + 1
        steps += 1
    return steps
