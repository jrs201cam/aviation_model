"""Analysis to determine number of passengers per day."""

import camia_engine as engine
from camia_model.units import year

import aviation
from aviation.units import passenger

# inputs
passengers_per_year = 4.46e9 * passenger / year

inputs = {
    "passengers_per_year": passengers_per_year,
}

output = "passengers_per_day"

# model
systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)

# print output
print(f"{passengers_per_day.value:.2e} {passengers_per_day.unit}")
