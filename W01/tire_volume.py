# Calculates a user's tire volume
# If use would like to buy more tires, it stores the users name, phone number, and email in the txt file

import math
from datetime import datetime

# Imports current date from users computer
current_date = datetime.now()


# Gets tire measurements form the user
width = int(input('What is the tires WIDTH in millimeters: '))
aspect_ratio = int(input('What is the tires ASPECT RATIO: '))
diameter = int(input('What is the tires DIAMETER in inches: '))

# Requests to see if the user would like to buy more tires
buy = input('Would you like to buy more tires: [y/n] ')
phone = False
email = False
if buy == 'y':
    name = input('What is your name: ')
    phone = input('What is your phone number: ')
    email = input('What is you email: ')
    with open(r"W01\costomers.txt", "at") as file:
        print(f'{name}, {phone}, {email}', file=file)

# Calculates the tire volume
pi = math.pi
volume = (pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Adds data to volume.txt file
with open(r"W01\volumes.txt", "at") as file:
    print(f'{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}', file=file)

# Displays the tire volume in liters
print(f'The volume of the tire is {volume:.2f} liters.')