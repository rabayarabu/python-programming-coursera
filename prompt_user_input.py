#2.3 Write a program to prompt the user for hours and rate per hour using input to 
#compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program 
#(the pay should be 96.25). You should use input to read a string and float() to 
#convert the string to a number.Do not worry about error checking or bad user data.

# Prompt the user for input
hours = input("Enter hours worked: ")
rate_per_hour = input("Enter rate per hour: ")

# Convert the input strings to floating-point numbers
hours_worked = float(hours)
hourly_rate = float(rate_per_hour)

# Calculate the gross pay
gross_pay = hours_worked * hourly_rate

# Display the result
print("Pay:",gross_pay)