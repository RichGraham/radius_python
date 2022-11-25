def calculate_radius( area):
    pi = 3.14159

    # Calculate the square root by a Taylor series in powers of x- 1 (a bad choice of method!)
    x = area / pi -1
    x_sq = x*x
    x_cubed = x*x*x
    x_4 = x*x*x*x
    x_5 = x*x*x*x*x

    return 1 + 1/2*x - 1/8*x_sq + 1/16*x_cubed - 5/128*x_4 + 7/256*x_5


if __name__ == "__main__":
    print(f'A circle of area of 2 has a radiys of {calculate_radius(2)}')
