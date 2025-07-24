"""Analysis to determine number of aircraft per day."""

# import function file
import camia_engine as engine
from camia_model.units import day, year

import aviation
from aviation.units import aircraft, journey, passenger

# inputs
passengers_per_year = 4.46e9 * passenger / year
flights_per_day = 2.0 * journey / (aircraft * day)
seats = 150.0 * passenger / aircraft

inputs = {
    "passengers_per_year": passengers_per_year,
    "seats": seats,
    "flights_per_day": flights_per_day,
}

output = "aircraft_per_day"

systems_model = engine.SystemsModel(aviation.transforms)
aircraft_per_day = systems_model.evaluate(inputs, output)

print(f"{aircraft_per_day.value:.2e} {aircraft_per_day.unit}")
