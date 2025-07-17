# import function file
import aviation

# inputs
days_per_year = 365.0
passengers_per_year = 4.46E9

# model
passengers_per_day =  aviation.passengers_per_day(passengers_per_year = passengers_per_year, days_per_year = days_per_year)

# print output
print(f"{passengers_per_day=:.2e}")