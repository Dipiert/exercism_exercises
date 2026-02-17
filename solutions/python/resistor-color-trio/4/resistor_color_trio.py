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

PREFIXES = ("kilo", "mega", "giga", "")


def label(colors: list[str]) -> str:
    """
    Given a list of colors representing the color bands on a resistor,
    return a string representing the resistance value of the resistor (ohms).
    It uses the appropriate SI prefix (kilo, mega, giga) if necessary.
    """
    first, second, multiplier, *_ = colors
    base = BAND_VALUES[first] * 10 + BAND_VALUES[second]
    resistor_value = base * (10 ** BAND_VALUES[multiplier])
    counter = 0
    
    while resistor_value >= 1000:
        resistor_value //= 1000
        counter += 1
        
    return f"{resistor_value} {PREFIXES[counter - 1]}ohms"
