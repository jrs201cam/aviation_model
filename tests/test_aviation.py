import pytest

from aviation.aviation import aircraft_per_day, passengers_per_day


@pytest.mark.parametrize(
    ("passengers_per_year", "days_per_year", "expected_passengers_per_day"),
    (
        (365_000_000.0, 365.0, 1_000_000.0),
        (732_000_000.0, 366.0, 2_000_000.0),
    ),
)
def test_passengers_per_day(passengers_per_year, days_per_year, expected_passengers_per_day):
    assert (
        passengers_per_day(passengers_per_year=passengers_per_year, days_per_year=days_per_year)
        == expected_passengers_per_day
    )


def test_aircraft_per_day():
    days_per_year = 365.0
    passengers_per_year = 5_000_000_000.0
    seats_per_aircraft = 200.0
    flights_per_aircraft_per_day = 2.0

    expected_required_global_fleet = 25_000.0

    result = aircraft_per_day(
        passengers_per_day=passengers_per_day(
            passengers_per_year=passengers_per_year, days_per_year=days_per_year
        ),
        seats=seats_per_aircraft,
        flights_per_day=flights_per_aircraft_per_day,
    )

    tolerance = 10_000.0
    assert result == pytest.approx(expected_required_global_fleet, abs=tolerance)
