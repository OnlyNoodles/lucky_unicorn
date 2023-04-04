"""Component 2 (How much) v4
Changing v3 into a function
Also needed to change user_balance to the more generic variable name 'response'
and to change the condition and position of the number comparison into the loop
to make the function recyclable
"""


def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a number between {} and {}\n".format(low, high)


    # Keep asking until a valid amount (1-10) is entered
    while True:
        try:
            # Ask for amount
            response = int(input(question))

            # Check for number within the required range
            if low <= response <= high:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine
user_balance = num_check("How much would you like to play with? $", 1, 10)
print(f"You are playing with ${user_balance}")
