import numpy as np
def calculate_radius( area):
    pi = 3.14159265

    return np.sqrt( area/pi)

#
#


if __name__ == "__main__":
    my_area = 2
    print(f'A circle of area {my_area}m^2 has a radiys of {calculate_radius(my_area)}m')
