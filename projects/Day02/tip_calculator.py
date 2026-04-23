print('This program will calculate tip for you')

# Okay so using input function will treat anything passed as 'string'
# my first one was like float(total) but that didn't really work well.
# so i just did total = float(input(...)) 
    # that worked a lot better
total = float(input('How much was the bill?: '))

tip_percent = float(input('How much are we tipping today? (Ex: 0.15 0.18): '))

people = float(input('How many people are paying? (Type 1 if just yourself): '))

tip_amount = total * tip_percent

final_total = total + tip_amount

print(f'Total comes out to {final_total}$ Each person pays {final_total/people}$')

