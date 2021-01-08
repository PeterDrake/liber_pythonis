def years_to_seconds(years):
    days = years * 365.24
    hours = days * 24
    minutes = hours * 60
    seconds = minutes * 60
    return seconds

print(years_to_seconds(5))
