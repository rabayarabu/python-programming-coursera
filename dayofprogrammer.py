def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return "26.09.1918"
    elif (year < 1918 and year % 4 ==0) or (year > 1918 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0))):
        # Check if it's a leap year in Julian or Gregorian calendar
        day = 256 - 244
        return f"{day}.09.{year}"
    else:
        # It's not a leap year
        day = 256 - 243
        return f"{day}.09.{year}"

# Sample inputs
print(dayOfProgrammer(2017))  # Output: "13.09.2017"
print(dayOfProgrammer(2016))  # Output: "12.09.2016"
print(dayOfProgrammer(1800))  # Output: "12.09.1800"

#hackerrank problem solving. got 15 points! well done my girl! 