BAND_VALUES = {
    color: value for value, color in enumerate(
        (
            'black',
            'brown',
            'red',
            'orange',
            'yellow',
            'green',
            'blue',
            'violet',
            'grey',
            'white'
        )
    )
}

PREFIXES = (
    (1_000_000_000, "giga"),
    (1_000_000, "mega"),
    (1_000, "kilo"),
)


def label(colors: list[str]) -> str:
    """
    Given a list of colors representing the color bands on a resistor, return a string representing the resistance value of the resistor in ohms.
    It uses the appropriate SI prefix (kilo, mega, giga) if necessary.
    """
    first, second, multiplier = colors[:3]
    base = BAND_VALUES[first] * 10 + BAND_VALUES[second]
    resistance_value = base * (10 ** BAND_VALUES[multiplier])
        
    prefix = ""
    
    for prefix_value, prefix_name in PREFIXES:
        if resistance_value >= prefix_value:
            prefix = prefix_name
            resistance_value //= prefix_value
            break
        
    return f"{resistance_value} {prefix}ohms"