"""Modelling the global fleet."""

from aviation._model import transform


@transform
def passengers_per_day(*, passengers_per_year: float, days_per_year: float = 365.25) -> float:
    """The number of passengers per day globally.

    Args:
        passengers_per_year: The number of passengers flying per
            year globally.
        days_per_year: The number of days in a year.

    """
    return passengers_per_year / days_per_year


@transform
def aircraft_per_day(*, passengers_per_day: float, seats: float, flights_per_day: float) -> float:
    """The size of the required global fleet i.e., the number of aircraft per day.

    Args:
        passengers_per_day: The number of passengers flying per
            day globally.
        seats: The number of seats on an aircraft.
        flights_per_day: The average number of flights per day
            globally.

    """
    return passengers_per_day / (seats * flights_per_day)
