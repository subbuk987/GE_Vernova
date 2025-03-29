from random import randint

try_count = 0


def generate_coupon(coupon, digits):
    """
    Generates a random number until it matches the given coupon.

    Parameters:
        coupon (int): The target coupon number.
        digits (int): The number of digits in the coupon.
    """
    global try_count
    found_coupon = False
    end_range = 10 ** digits - 1

    while not found_coupon:
        random_coupon = randint(0, end_range)
        try_count += 1
        if random_coupon == coupon:
            found_coupon = True


def coupon_numbers(coupon_list, digits):
    """
    Generates random numbers for each coupon in the list.

    Parameters:
        coupon_list (list): A list of coupon numbers.
        digits (int): The number of digits in each coupon.
    """
    global try_count
    for coupon in coupon_list:
        generate_coupon(coupon, digits + 1)

    print(f"The total number of random numbers needed to generate {len(coupon_list)} coupons are {try_count}")


if __name__ == "__main__":
    """
    Runs the coupon number generation process based on user input.
    """
    n_digits = int(input("Enter the length of coupons:"))
    if 2 < n_digits < 13:
        user_coupons = set(map(int, input(f"Enter your {n_digits}-digit coupon numbers separated by space:").split()))
        print(f"You have entered {len(user_coupons)} unique coupons!!")
        coupon_numbers(list(user_coupons), n_digits)
    else:
        print("Please enter coupons with length in between 3 and 12!")
