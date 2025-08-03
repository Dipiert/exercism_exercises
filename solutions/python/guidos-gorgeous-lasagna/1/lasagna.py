EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    '''
    :param elapsed_bake_time: int baking time already elapsed
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    '''
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_or_layers):
    '''
    :param number_or_layers: int, number of layers you want to add to the lasagna
    :return: int, how many minutes you'd spend making these layers
    '''
    return number_or_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''
    :param number_of_layers: int, number of layers added to the lasagna
    :param elapsed_bake_time: int, minutes the lasagna has been baking
    :return: int, total number of minutes you've been cooking
    '''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
