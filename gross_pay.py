# 3.1 Write a program to prompt the user for hours and rate per hour 
# using input to compute gross pay. Pay the hourly rate for the hours 
# up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
# Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
# You should use input to read a string and float() to convert the string to a number.
# Do not worry about error checking the user input - assume the user types numbers properly.


# Prompt the user for input
hours = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")

# Convert the input to floating-point numbers

try:
    hours = float(hours)
    rate = float(rate)
except:
    print("error")
    quit()

# Calculate gross pay
if hours <= 40:
    gross_pay = hours * rate
else:
    # Calculate regular pay for the first 40 hours
    regular_pay = 40 * rate

    # Calculate overtime pay for hours worked above 40
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)

    # Calculate total gross pay
    gross_pay = regular_pay + overtime_pay

# Display the gross pay
print("Gross pay:", gross_pay)