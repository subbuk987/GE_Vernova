def harmonic_number(number):
    """
    Prints the Nth harmonic number.

    Parameters:
        number(int) : User input for the value N.
    """

    if number == 0:
        print("Number should not be 0!")
        return

    harmonic_value = 0

    for num in range(1,number+1):
        harmonic_value += 1 / num

    print(f"The harmonic number of {number} is {harmonic_value}")


if __name__ == "__main__":
    user_input = int(input("Enter a Number:"))
    harmonic_number(user_input)
