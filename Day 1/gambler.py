from random import randint


def gambler(stake, goal, number_of_experiments):
    """
    Simulates a gambling scenario where a user bets until they either reach their goal or lose all their stake.

    Parameters:
        stake (int): The initial amount of money the gambler starts with.
        goal (int): The target amount the gambler wants to reach.
        number_of_experiments (int): The number of times the experiment is repeated.
    """
    win_list = []
    bet_list = []
    wins = 0

    for _ in range(number_of_experiments):
        loop_stake = stake
        number_of_wins = 0
        number_of_bets = 0

        while loop_stake != 0 and loop_stake != goal:
            if randint(1, 2) == 1:
                loop_stake += 1
                number_of_wins += 1
            else:
                loop_stake -= 1

            number_of_bets += 1

        if loop_stake == goal:
            wins += 1

        win_list.append(number_of_wins)
        bet_list.append(number_of_bets)

        win_percentage = (number_of_wins / number_of_bets) * 100 if number_of_bets > 0 else 0
        print(f"Win percentage of {_ + 1} experiment is {win_percentage}%.")
        print(f"Loss percentage of {_ + 1} experiment is {100 - win_percentage}%.")

    print(f"The average number of wins across {number_of_experiments} is {sum(win_list) / len(win_list)}.")
    print(f"The average number of bets across {number_of_experiments} is {sum(bet_list) / len(bet_list)}.")
    print(f"The Number of times Goal Reached across {number_of_experiments} is: {wins}.")


if __name__ == "__main__":
    """
    Runs the gambling simulation based on user input.
    """
    user_stake = int(input("Enter the Stake amount:"))
    user_goal = int(input("Enter the Goal Amount:"))
    user_experiment_count = int(input("Enter the experiment count:"))
    gambler(user_stake, user_goal, user_experiment_count)
