from typing import Callable


def validate_triangle(fn: Callable) -> Callable:
       
    def wrapper(sides: list[float], *args, **kwargs) -> bool:
        return all(sides) and 2 * max(sides) < sum(sides) and fn(sides, *args, **kwargs)
    
    return wrapper


@validate_triangle
def equilateral(sides: list[float]) -> bool:
    return len(set(sides)) == 1


@validate_triangle
def isosceles(sides: list[float]) -> bool:
    return len(set(sides)) <= 2


@validate_triangle
def scalene(sides: list[float]) -> bool:
    return len(set(sides)) == 3

