def user_name():
    """
    Takes user input for Username  and greets the user.
    """

    user_input = input("Please enter your Username:")

    if len(user_input) < 4:
        print("The username should be greater than 3 characters!")
        return

    print(f"Hello {user_input}, How are you?")


if __name__ == "__main__":
    user_name()
