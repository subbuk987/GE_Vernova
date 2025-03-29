def check_prime(num):
    """
    Checks if a number is prime or not.

    Parameters:
        num(int) : Number to be checked.
    """
    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def prime_factors(number):
    """
    Computes the prime factors of N using brute force.

    Parameters:
        number(int) : User input for the value N.
    """
    prime_factor_list = []

    for num in range(2, number + 1):
        if number % num == 0:
            if check_prime(num):
                prime_factor_list.append(num)

    print(f"The prime factors of {number} are {', '.join(map(str,prime_factor_list))}.")


if __name__ == "__main__":
    user_input = int(input("Enter the number:"))
    prime_factors(user_input)