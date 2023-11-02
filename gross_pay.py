# Prompt the user for input
hours = input("Enter hours worked: ")
rate = input("Enter hourly rate: ")

# Convert the input to floating-point numbers
hours = float(hours)
rate = float(rate)

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