import math

def main():
    # List of Can Names, Radius (centimeters), Height (centimeters), and Cost per Can (U.S. Dollars)
    cans = [['#1 Picnic', 6.83, 10.16, 0.28],
            ['#1 Tall', 7.78, 11.91, 0.43],
            ['#2', 8.73, 11.59, 0.45],
            ['#2.5', 10.32, 11.91, 0.61],
            ['#3 Cylinder', 10.79, 17.78, 0.86],
            ['#5', 13.02, 14.29, 0.83],
            ['#6Z', 5.40, 8.89, 0.22],
            ['#8Z short', 6.83, 7.62, 0.26],
            ['#10', 15.72, 17.78, 1.53],
            ['#211', 6.83, 12.38, 0.34],
            ['#300', 7.62, 11.27, 0.38],
            ['#303', 8.10, 11.11, 0.42]]

    # Goes through each can and gets their volume and surface area.
    computed_cans = []
    for can in cans:
        can_name = can[0]
        can_volume = compute_volume(can[1], can[2])
        can_surface_area = compute_surface_area(can[1], can[2])
        can_storage_efficiency = compute_storage_efficiency(can_volume, can_surface_area)
        can_cost_efficiency = compute_cost_efficiency(can_volume, can[3])
        computed_can = [can_name, can_storage_efficiency, can_cost_efficiency]
        computed_cans.append(computed_can)

    # Prints all the cans and their info
    for can in computed_cans:
        print(f'{can[0]} {can[1]:.2f} {can[2]:.2f}')


    # Determines and prints which can has the best storage efficiency.
    best_storage_efficiency = 0
    best_storage_efficiency_can_name = ''
    for can in computed_cans:
        if can[1] > best_storage_efficiency:
            best_storage_efficiency = can[1]
            best_storage_efficiency_can_name = can[0]
    print(f'The can with the best storage efficiency is the {best_storage_efficiency_can_name} can with an efficiency of {best_storage_efficiency:.3f} cm^3/cm^2')

    # Determines and prints which can is the most cost efficient.
    first_can = cans[0]
    best_cost_efficiency = first_can[2]
    best_cost_efficiency_can_name = first_can[0]
    for can in computed_cans:
        if can[2] > best_cost_efficiency:
            best_cost_efficiency = can[2]
            best_cost_efficiency_can_name = can[0]
    print(f'The most cost effective can is the {best_cost_efficiency_can_name} can with {best_cost_efficiency:.2f} cm^3/$')

# Computes the volume of a can.
def compute_volume(radius, height):
    pi = math.pi
    volume = pi * (radius ** 2) * height
    return volume

# Computes the surface area of a can.
def compute_surface_area(radius, height):
    pi = math.pi
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

# Computes storage efficiency of a can.
def compute_storage_efficiency(volume, surface_area):
    storage_efficiency = volume / surface_area
    return storage_efficiency

# Computes cost efficiency of a can.
def compute_cost_efficiency(volume, cost):
    cost_efficiency = volume / cost
    return cost_efficiency

main()