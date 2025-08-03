"""Functions to automate Conda airlines ticketing system."""

from itertools import cycle

def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """

    for _, seat in zip(range(number), cycle("ABCD")):
        yield seat
            

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.

    A seat number consists of the row number and the seat letter.

    There is no row 13.
    Each row has 4 seats.

    Seats should be sorted from low to high.

    Example: 3C, 3D, 4A, 4B

    """

    row = 0
    seats = "ABCD"
    remaining = number
    
    for _ in range(number):
        row += 1
        if row == 13:
            row += 1

        for seat in seats:
            if remaining <= 0:
                return
            yield f"{row}{seat}"
            remaining -= 1

def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """
    return {p:s for p,s in zip(passengers, generate_seats(len(passengers)))}

def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """
    for sn in seat_numbers:
        yield f'{sn}{flight_id}'.ljust(12, '0')
