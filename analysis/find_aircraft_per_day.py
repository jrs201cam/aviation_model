"""Analysis to determine number of aircraft per day."""

# import function file
import aviation
from aviation import _engine as engine

# inputs
days_per_year = 365.25
passengers_per_year = 4.46e9
flights_per_day = 2.0
seats = 150.0

inputs = {
    "passengers_per_year": passengers_per_year,
    "days_per_year": days_per_year,
    "seats": seats,
    "flights_per_day": flights_per_day,
}

output = "aircraft_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
aircraft_per_day = systems_model.evaluate(inputs, output)

print(f"{aircraft_per_day=:.2e}")
