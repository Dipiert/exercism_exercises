from dataclasses import dataclass

@dataclass
class Color:
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

COLORS = { c.name: c for c in (black, brown, red, orange, yellow, green, blue, violet, grey, white) }

def reduce_using_prefix(value):
    prefixes = ("giga", "mega", "kilo")
    i = 1
    thousand = 1000
    prefix = ""
    while value >= thousand:
        value /= thousand
        prefix = prefixes[-i]        
        i = i + 1
    return value, prefix

def resistor_label(colors):
    if len(colors) == 1:
        return f"{COLORS[colors[0]].resistance} ohms"
    
    *values, multiplier, tolerance = colors

    multiplier = 10 ** int(COLORS[multiplier].resistance)  
    
    values = int("".join(COLORS[v].resistance for v in values))
        
    value, prefix = reduce_using_prefix(values * multiplier )
    
    value = int(value) if int(value) == value else value
    
    return f"{value} {prefix}ohms ±{COLORS[tolerance].tolerance}%"

