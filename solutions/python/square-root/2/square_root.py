def _heron(number: int) -> int:
    x_n = 1
    x_nplus1 = 0
    while True:
        proposed_x_nplus1 = 1/2 * (x_n + number/x_n)
        if x_nplus1 == proposed_x_nplus1:
            break
        
        x_nplus1 = proposed_x_nplus1
        x_n = x_nplus1
        
    return int(x_nplus1)


def square_root(number: int) -> int:
    return _heron(number)
