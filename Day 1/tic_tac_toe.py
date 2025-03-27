import os
import random
import time

winner = None
chance = 2
board = [None] * 9


def show_board_instructions():
    """
    Displays the Tic-Tac-Toe board format for the user.

    This function prints the positions (1-9) that the user
    should use to make their move.
    """
    print("Please Remember the Board Format!!")
    print("–––––––––––––")
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print("–––––––––––––")


def print_board():
    """
    Prints the current state of the Tic-Tac-Toe board.

    The board uses 'X' for the user, 'O' for the computer,
    and empty spaces for unoccupied positions.
    """
    lb = [" " if x is None else x for x in board]
    print("–––––––––––––")
    print(f"| {lb[0]} | {lb[1]} | {lb[2]} |")
    print(f"| {lb[3]} | {lb[4]} | {lb[5]} |")
    print(f"| {lb[6]} | {lb[7]} | {lb[8]} |")
    print("–––––––––––––")


def clear_output():
    """
    Clears the terminal output.

    This function uses 'cls' for Windows and 'clear' for macOS/Linux.
    """
    os.system("cls" if os.name == "nt" else "clear")


def check_board():
    """
    Checks the board to determine if there is a winner.

    Updates the global 'winner' variable if a winning combination
    is found or if the game ends in a draw.
    """
    global winner
    match_indices = [[0, 1, 2],
                     [3, 4, 5],
                     [6, 7, 8],
                     [0, 3, 6],
                     [1, 4, 7],
                     [2, 5, 8],
                     [0, 4, 8],
                     [2, 4, 6]]

    for indices in match_indices:
        if board[indices[0]] == board[indices[1]] == board[indices[2]] and board[indices[0]] is not None:
            winner = "user" if board[indices[0]] == "X" else "computer"
            return

    if None not in board:
        winner = "draw"


def tic_tac_toe():
    """
    Runs the Tic-Tac-Toe game.

    The game alternates between the user and the computer, allowing them to make moves
    on the board until a winner is determined or the game ends in a draw.
    """
    global chance
    global winner
    show_board_instructions()
    time.sleep(2)
    seen = set()

    while not winner:
        clear_output()
        print_board()

        if chance == 2:
            try:
                user_choice = int(input("Dear user, Enter Your Choice (1-9): "))
                if user_choice not in range(1, 10) or user_choice in seen:
                    print("Invalid move! Try again.")
                    continue

                board[user_choice - 1] = "X"
                seen.add(user_choice)
                chance = 1
            except ValueError:
                print("Please enter a valid number (1-9).")
                continue
        else:
            while True:
                computer_choice = random.randint(1, 9)
                if computer_choice not in seen:
                    board[computer_choice - 1] = "O"
                    seen.add(computer_choice)
                    chance = 2
                    break

        check_board()

    clear_output()
    print_board()
    if winner == "draw":
        print("It's a Draw!!!")
    else:
        print(f"{winner.capitalize()} Wins!!!")


if __name__ == "__main__":
    tic_tac_toe()
