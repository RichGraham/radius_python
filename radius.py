import math

def calculate_radius( area):
    pi = math.pi

    # Calculate the square root by a Taylor series in powers of x- 1 (a bad choice of method!)
    x = area / pi -1
    x_2 = x * x
    x_3 = x_2 * x
    x_4 = x_2 * x_2
    x_5 = x_3 * x_4

    return 1 + 1/2*x - 1/8*x_2 + 1/16*x_3 - 5/128*x_4 + 7/256*x_5


if __name__ == "__main__":
    print(f'A circle of area of 2 has a radius of {calculate_radius(2)}')
