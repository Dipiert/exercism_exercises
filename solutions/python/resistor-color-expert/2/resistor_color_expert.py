"""Utilities for converting resistor color bands into human-readable labels."""

from dataclasses import dataclass

@dataclass
class Color:
    """Represents a resistor color band and its associated numeric value.

    Attributes:
        name: The canonical color name.
        resistance: The digit value represented by the color.
        tolerance: The color's tolerance percentage, if applicable.
    """

    name : str
    resistance: str
    tolerance: float = None 

black = Color("black", "0")
brown = Color("brown", "1", 1)
red = Color("red", "2", 2)
orange = Color("orange", "3")
yellow = Color("yellow", "4")
green = Color("green", "5", 0.5)
blue = Color("blue", "6", 0.25)
violet = Color("violet", "7", 0.1)
grey = Color("grey", "8", 0.05)
white = Color("white", "9")

COLORS = { color.name: color for color in (black, brown, red, orange, yellow, green, blue, violet, grey, white) }

def reduce_using_prefix(value):
    """Reduce a resistance value to the largest matching SI prefix.

    Args:
        value: The resistance value in ohms.

    Returns:
        A tuple containing the scaled numeric value and its prefix.
    """
    prefixes = ("giga", "mega", "kilo")
    index = 1
    thousand = 1000
    prefix = ""
    while value >= thousand:
        value /= thousand
        prefix = prefixes[-index]        
        index += 1
    return value, prefix

def resistor_label(colors):
    """Return the formatted label for a resistor color band sequence.

    Args:
        colors: A list of resistor color names, including the multiplier
            and tolerance bands.

    Returns:
        A human-readable resistance string such as "33 ohms ±2%" or
        "2 kiloohms ±0.5%".
    """
    if len(colors) == 1:
        return f"{COLORS[colors[0]].resistance} ohms"
    
    *values, multiplier, tolerance = colors

    multiplier = 10 ** int(COLORS[multiplier].resistance)  
    
    values = int("".join(COLORS[value].resistance for value in values))
        
    value, prefix = reduce_using_prefix(values * multiplier )
    
    value = int(value) if int(value) == value else value
    
    return f"{value} {prefix}ohms ±{COLORS[tolerance].tolerance}%"
