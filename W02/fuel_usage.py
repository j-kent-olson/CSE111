
def main():
    # User input
    start = float(input('What is the odometers starting value in miles? '))
    end = float(input('What is the odometers ending value in miles? '))
    gallons = float(input('How many gallons of gas were used? '))

    # Runs convertion functions
    mpg = miles_per_gallon(start, end, gallons)
    lp100k = lp100k_from_mpg(mpg)

    print(f'Your vehicle gets {mpg:.1f} mpg and {lp100k:.2f} lp100k')

# Calculates miles per gallon
def miles_per_gallon(start, end, gallons):
    mpg = (end - start) / gallons
    return mpg

# Converts MPG to liters per 100 kilometers
def lp100k_from_mpg(mpg):
    lp100k = 235.215 / mpg
    return lp100k

main()