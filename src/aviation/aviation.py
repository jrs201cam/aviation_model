def passengers_per_day(*, passengers_per_year, days_per_year=365.25):
    passengers_per_day = passengers_per_year / days_per_year
    return passengers_per_day


def aircraft_per_day(*, passengers_per_day, seats, flights_per_day):
    aircraft_per_day = passengers_per_day / (seats * flights_per_day)
    return aircraft_per_day
