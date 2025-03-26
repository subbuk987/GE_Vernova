def leap_year(year):
    """
    Checks if the year is a leap year of not.

    Parameters:
        year(str) : User Input of Year
    """

    if len(year) != 4:
        print("The should be at least 4 digits!")
        return

    year = int(year)

    if (year % 100) % 4 == 0:
        print("The Entered Year is a Leap Year")
    else:
        print("The Entered Year is not a Leap Year")


if __name__ == "__main__":
    user_year = input("Please enter the year:")
    leap_year(user_year)
