import numpy as np
from openpyxl.styles.builtins import total


def mydice():
    total = 0
    while True:  # Start an infinite loop
        a = np.random.randint(1, 7)  # Generate a random number between 1 and 6
        print(f"Rolled: {a}")
        total += a

        answer = input("Type in True to continue and False to quit: ")
        if answer == "True":
            continue  # Continue the loop
        elif answer == "False":
            break  # Exit the loop
        else:
            print("Invalid input. Please type 'True' or 'False'.")
    return total
Numberofdice = int(input("How many dice do you want to roll at a time? "))

total_sum = 0
for i in range(Numberofdice):
    print(f"Rolling dice {i + 1}...")
    mydice()  # Call the mydice function to roll the dice interactively
    total_sum += mydice()
print(f"Total sum of all dice rolls: {total_sum}")
