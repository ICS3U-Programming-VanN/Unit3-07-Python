#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: October 19, 2022
# This program asks the user for their age and
# determines whether or not they can date the grandchild


import constants


def main():
    # Checks for exceptions input
    try:

        # Asks user for their age (as string)
        user_age_string = input("Enter your age: ")

        # Converts user input into integer (stores as new variable)
        user_age = int(user_age_string)

    # In the event of an exception in the user input
    except Exception:
        print("Please enter a valid number!")

    # If there are not exceptions
    else:

        # IF the user is within the age range set
        if (
            user_age > constants.MINIMUM_AGE_THRESHOLD
            and user_age < constants.MAXIMUM_AGE_THRESHOLD
        ):
            print("\nYou are able to date my grandchild!")

        # IF the user is not within the age range set
        else:
            print("\nYou are not allowed to date my grandchild!")


if __name__ == "__main__":
    main()
