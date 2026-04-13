"""

program that will calculate your weekly earning based off hours worked and 
how much made in one hour

"""


print('this program will' \
' calculate your weekly earning based off of how many hours' \
' you work and dollars per hour')

hours = int(input('how many hours u work per week?: '))

rate_per_hour = int(input('how much u make per hour?: '))

weekly_earning = (hours * rate_per_hour)

print(weekly_earning)