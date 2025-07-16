#inputs
days_per_year = 365.0
passenger_per_year = 4.46E9
flights_per_day = 2.0
seats = 150.0

#model
passengers_per_day =  passengers_per_year/days_per_year
aircraft_per_day = passengers_per_day/(seats*flights_per_day)

print(f"{passengers_per_day=:.2e}")
print(f"{aircraft_per_day=:.2e}")