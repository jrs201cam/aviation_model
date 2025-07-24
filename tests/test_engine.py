import typing

import camia_engine as engine
import pytest
import pytest_camia
from camia_model.units import day, year

import aviation
from aviation.units import aircraft, journey, passenger


@pytest.fixture
def systems_model() -> engine.SystemsModel:
    return engine.SystemsModel(aviation.transforms)


@pytest.mark.parametrize(
    ("inputs", "output", "expected"),
    (
        (
            {"passengers_per_year": 5_000_000_000.0 * passenger / year},
            "passengers_per_year",
            5_000_000_000.0 * passenger / year,
        ),
        (
            {"aircraft_per_day": 25_000.0 * aircraft / day},
            "aircraft_per_day",
            25_000.0 * aircraft / day,
        ),
        (
            {
                "passengers_per_year": 5_000_000_000.0 * passenger / year,
            },
            "passengers_per_day",
            13_689_254.0 * passenger / day,
        ),
        (
            {
                "passengers_per_day": 13_689_254.0 * passenger / day,
                "seats": 200.0 * passenger / aircraft,
                "flights_per_day": 3.0 * journey / (aircraft * day),
            },
            "aircraft_per_day",
            22_815.0 * aircraft,
        ),
        (
            {
                "passengers_per_day": 16_438_356.16 * passenger / day,
                "seats": 200.0 * passenger / aircraft,
                "flights_per_day": 3.0 * journey / (aircraft * day),
            },
            "aircraft_per_day",
            27_397.0 * aircraft,
        ),
    ),
)
def test_systems_model_evaluate(
    systems_model: engine.SystemsModel,
    inputs: dict[str, typing.Any],
    output: str,
    expected: float,
) -> None:
    assert systems_model.evaluate(inputs, output) == pytest_camia.approx(expected, atol=1.0)
