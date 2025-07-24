"""Modelling the global fleet."""

import typing

import camia_model as model
from camia_model.units import Quantity, day, year

from aviation.units import aircraft, journey, passenger


@model.transform
def passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
) -> typing.Annotated[Quantity, passenger / day]:
    """The number of passengers per day globally.

    Args:
        passengers_per_year: The number of passengers flying per
            year globally.

    """
    return passengers_per_year.convert_to(passenger / day)


@model.transform
def aircraft_per_day(
    passengers_per_day: typing.Annotated[Quantity, passenger / day],
    seats: typing.Annotated[Quantity, passenger / aircraft],
    flights_per_day: typing.Annotated[Quantity, journey / (aircraft * day)],
) -> typing.Annotated[Quantity, aircraft]:
    """The size of the required global fleet i.e., the number of aircraft per day.

    Args:
        passengers_per_day: The number of passengers flying per
            day globally.
        seats: The number of seats on an aircraft.
        flights_per_day: The average number of flights per day
            globally.

    """
    aircraft_per_journey = 1.0 * aircraft / journey
    return passengers_per_day / (seats * flights_per_day * aircraft_per_journey)
