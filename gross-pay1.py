def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * (rate * 1.5)
        pay = regular_pay + overtime_pay
    return pay

# Get input from the user
hours_input = input("Enter hours worked: ")
rate_input = input("Enter hourly rate: ")

# Convert input to float
hours = float(hours_input)
rate = float(rate_input)

# Calculate and print the gross pay
gross_pay = computepay(hours, rate)
print("Gross pay:", gross_pay)