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

PREFIXES = ("kilo", "mega", "giga")


def label(colors: list[str]) -> str:
    """
    Given a list of colors representing the color bands on a resistor,
    return a string representing the resistance value of the resistor (ohms).
    It uses the appropriate SI prefix (kilo, mega, giga) if necessary.
    """
    first, second, multiplier = colors[:3]
    base = BAND_VALUES[first] * 10 + BAND_VALUES[second]
    resistance_value = base * (10 ** BAND_VALUES[multiplier])
    counter = 0
    
    while resistance_value >= 1000:
        resistance_value //= 1000
        counter += 1

    prefix = PREFIXES[counter - 1] if counter else ""
        
    return f"{resistance_value} {prefix}ohms"
