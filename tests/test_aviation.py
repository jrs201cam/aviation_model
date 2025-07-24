import typing

import pytest
import pytest_camia
from camia_model.units import Quantity, day, year

from aviation.aviation import aircraft_per_day, passengers_per_day
from aviation.units import aircraft, journey, passenger


@pytest.mark.parametrize(
    ("passengers_per_year", "expected_passengers_per_day"),
    (
        (365_000_000.0 * passenger / year, 1_000_000.0 * passenger / day),
        (732_000_000.0 * passenger / year, 2_000_000.0 * passenger / day),
    ),
)
def test_passengers_per_day(
    passengers_per_year: typing.Annotated[Quantity, passenger / year],
    expected_passengers_per_day: typing.Annotated[Quantity, passenger / day],
) -> None:
    assert passengers_per_day(
        passengers_per_year=passengers_per_year,
    ) == pytest_camia.approx(expected_passengers_per_day, atol=10_000.0)


def test_aircraft_per_day() -> None:
    passengers_per_year = 5_000_000_000.0 * passenger / year
    seats_per_aircraft = 200.0 * passenger / aircraft
    flights_per_aircraft_per_day = 2.0 * journey / (aircraft * day)

    expected_required_global_fleet = 25_000.0 * aircraft

    result = aircraft_per_day(
        passengers_per_day=passengers_per_day(passengers_per_year=passengers_per_year),
        seats=seats_per_aircraft,
        flights_per_day=flights_per_aircraft_per_day,
    )

    tolerance = 10_000.0
    assert result == pytest_camia.approx(expected_required_global_fleet, atol=tolerance)
