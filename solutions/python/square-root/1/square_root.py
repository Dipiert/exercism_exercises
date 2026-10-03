def square_root(number: int) -> int:
    """
    Calculates the integer square root of a number using binary search
    """
    if number == 1:
        return number

    right = number
    left = 0
    while left != right - 1:
        mid = (left + right)//2
        if mid * mid <= number:
            left = mid
        else:
            right = mid

    return left
