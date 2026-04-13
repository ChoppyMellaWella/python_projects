"""

program converts years to seconds

"""

years_lived = int(input('how old are you?: '))

def seconds_lived(years_lived):
    days_lived = years_lived * 365
    hours_lived = days_lived * 24
    minutes_lived = hours_lived * 60
    seconds_lived = minutes_lived * 60
    return seconds_lived

print(f"you've lived {seconds_lived(years_lived)} seconds")
