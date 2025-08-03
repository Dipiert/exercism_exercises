from typing import Callable

def validate_triangle(fn: Callable) -> Callable:
       
    def wrapper(sides: list[float], *args, **kwargs) -> bool:
        if all(s > 0 for s in sides):
            a, b, c = sorted(sides)
            return not a + b < c and fn(sides, *args, **kwargs)
        return False    
    
    return wrapper


@validate_triangle
def equilateral(sides: list[float]) -> bool:
    return len(set(sides)) == 1


@validate_triangle
def isosceles(sides: list[float]) -> bool:
    return equilateral(sides) or len(set(sides)) == 2


@validate_triangle
def scalene(sides: list[float]) -> bool:
    return len(set(sides)) == 3
