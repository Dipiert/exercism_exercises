def _heron(number: int) -> int:
    x = number
    while True:
        new_x = (x + number // x) // 2
        
        if new_x >= x:
            return x
        
        x = new_x


def square_root(number: int) -> int:
    return _heron(number)
