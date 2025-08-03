def two_sides_are_equal(sides):
    return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]

def all_sides_are_different(sides):
    return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]

def all_sides_are_equal(sides):
    return sides[0] == sides[1] == sides[2]

def validate_triangle(fn):
    
    def wrapper(sides, *args, **kwargs):
        if (
            all(s > 0 for s in sides) and 
            sides[0] + sides[1] >= sides[2] and
            sides[0] + sides[2] >= sides[1] and
            sides[1] + sides[2] >= sides[0]
        ):
            return fn(sides, *args, **kwargs)
        return False
    return wrapper
        
@validate_triangle
def equilateral(sides):
    return all_sides_are_equal(sides)

@validate_triangle
def isosceles(sides):
    return two_sides_are_equal(sides)

@validate_triangle
def scalene(sides):
    return all_sides_are_different(sides)
