"""Analysis to determine number of passengers per day."""

import camia_engine as engine

import aviation

# inputs
days_per_year = 365.25
passengers_per_year = 4.46e9

inputs = {
    "days_per_year": days_per_year,
    "passengers_per_year": passengers_per_year,
}

output = "passengers_per_day"

# model
systems_model = engine.SystemsModel(aviation.transforms)
passengers_per_day = systems_model.evaluate(inputs, output)

# print output
print(f"{passengers_per_day=:.2e}")
