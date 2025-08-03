def is_armstrong_number(number):
    number_as_str = str(number)
    return sum(int(num)**len(number_as_str) for num in number_as_str) == number
