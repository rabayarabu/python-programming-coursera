largest = None
smallest = None

while True:
    user_input = input("Enter an integer or 'done' to finish: ")

    if user_input == 'done':
        break

    try:
        number = int(user_input)

        if largest is None or number > largest:
            largest = number

        if smallest is None or number < smallest:
            smallest = number

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if largest is not None:
    print("Maximum is", largest)

if smallest is not None:
    print("Minimum is", smallest)


# 5.2 Write a program that repeatedly prompts a user for integer numbers until
#  the user enters 'done'. Once 'done' is entered, print out the largest and smallest 
# of the numbers. If the user enters anything other than a valid number catch it with 
# a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 
# 10, and 4 and match the output below.