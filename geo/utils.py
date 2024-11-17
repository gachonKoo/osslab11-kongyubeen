import math

def pythagoras(a, b):
    """
    Calculate the hypotenuse of a right triangle given sides a and b.
    """
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    """
    Calculate the area of a circle given its radius r.
    """
    area = math.pi * r**2
    return area
