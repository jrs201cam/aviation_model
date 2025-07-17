# import function file
import aviation

# inputs
days_per_year = 365.0
passengers_per_year = 4.46E9
flights_per_day = 2.0
seats = 150.0

# model
passengers_per_day =  aviation.passengers_per_day(passengers_per_year = passengers_per_year, days_per_year = days_per_year)
aircraft_per_day = aviation.aircraft_per_day(passengers_per_day = passengers_per_day, seats = seats, flights_per_day = flights_per_day)

# print output
print(f"{aircraft_per_day=:.2e}")
