import random


def coin_flip(number_of_toss):
    """
    Prints percentages of Tails and Heads in a given number of tosses.

    Parameters:
        number_of_toss(int) : Number of coin flips.

    """

    if number_of_toss <= 0:
        return -1

    number_of_heads = 0
    number_of_tails = 0

    for toss in range(number_of_toss):
        if random.random() < 0.5:
            number_of_tails += 1
        else:
            number_of_heads += 1

    tails_percentage = (number_of_tails / number_of_toss) * 100
    print(f"{tails_percentage}% of tails")
    print(f"{100 - tails_percentage}% of heads")


if __name__ == "__main__":
    number_of_tosses = int(input("Please enter the number of tosses:"))
    response = coin_flip(number_of_tosses)
    if response == -1:
        print("Please enter a positive value!")
