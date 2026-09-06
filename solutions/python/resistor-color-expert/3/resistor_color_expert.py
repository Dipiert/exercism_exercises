"""Utilities for converting resistor color bands into human-readable labels."""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Color:
    """Represents a resistor color band and its associated numeric value.

    Attributes:
        name: The canonical color name.
        resistance: The digit value represented by the color.
        tolerance: The color's tolerance percentage, if applicable.
    """

    name : str
    resistance: int
    tolerance: int | float | None = None 


COLORS = {
    color.name: color
    for color in (
        Color("black", 0),
        Color("brown", 1, 1),
        Color("red", 2, 2),
        Color("orange", 3),
        Color("yellow", 4),
        Color("green", 5, 0.5),
        Color("blue", 6, 0.25),
        Color("violet", 7, 0.1),
        Color("grey", 8, 0.05),
        Color("white", 9),
    )
}

def reduce_using_prefix(value: int) -> tuple[float, str]:
    """Reduce a resistance value to the largest matching SI prefix.

    Args:
        value: The resistance value in ohms.

    Returns:
        A tuple containing the scaled numeric value and its prefix.
    """
    PREFIXES = ("", "kilo", "mega", "giga")
    prefix_index = 0     
    while (
        value >= 1000
        and prefix_index < len(PREFIXES) - 1
    ):
        value /= 1000
        prefix_index += 1

    return value, PREFIXES[prefix_index]

def resistor_label(colors: list[str]):
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
    
    *value_bands, multiplier_band, tolerance_band = colors
    multiplier = 10 ** int(COLORS[multiplier_band].resistance)    
    significant_value = int(
        "".join(
            str(COLORS[color].resistance)
            for color in value_bands
        )
    )        
    value, prefix = reduce_using_prefix(significant_value * multiplier)    
    value = int(value) if int(value) == value else value    
    return f"{value} {prefix}ohms ±{COLORS[tolerance_band].tolerance}%"
