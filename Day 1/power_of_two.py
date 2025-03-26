def power_of_two(power):
    """
    Takes an argument power and prints a table of the
    powers of 2 that are less than or equal to 2^N.

    Parameters:
        power(int) : user entered power.
    """

    if power > 30 or power < 0:
        print("Please enter a number in the range (0,30) !")
        return

    result = 1

    for i in range(power):
        result *= 2
        print(f"| 2^{i+1}   | {result}")


if __name__ == "__main__":
    input_power = int(input("Please enter the power:"))
    power_of_two(input_power)
