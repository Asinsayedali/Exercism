"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.

    Seat letters are generated from A to D.
    After D it should start again with A.

    Example: A, B, C, D

    """
    seats = ["A", "B", "C", "D"]
    j = 0
    i = 0
    while j <number:
        yield seats[i]
        i += 1
        j += 1
        if (i == 4):
            i = 0


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

    seats = ["A", "B", "C", "D"]
    j = 0
    i = 0
    row = 1
    while j < number:
        # Skip row 13
        if row == 13:
            row += 1
            continue

        yield str(row) + seats[i]

        i += 1
        j += 1

        # Reset seat letter index for each new row
        if i == 4:
            row += 1
            i = 0


def assign_seats(passengers):
    """Assign seats to passengers.

    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.

    Example output: {"Adele": "1A", "Björk": "1B"}

    """

    list_of_seat = []
    i = 0
    count = len(passengers)
    seats = generate_seats(count)

    while i<count:
        list_of_seat.append(next(seats))
        i += 1
    data_generated = dict(zip(passengers,list_of_seat))
    return data_generated



def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.

    """

    i=0
    count = len(seat_numbers)
    while i < count:
        ticket_id = seat_numbers[i] + flight_id
        extra_digits = 12 - len(ticket_id)
        ticket_id = ticket_id + '0' * extra_digits
        yield  ticket_id
        i+=1
