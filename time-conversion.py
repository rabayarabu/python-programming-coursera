def timeConversion(s):
    # Extract hour, minute, and second components
    hh, mm, ss = map(int, s[:-2].split(":"))
    am_pm = s[-2:]

    # Handle AM
    if am_pm == "AM":
        if hh == 12:
            hh = 0
    # Handle PM
    else:
        if hh != 12:
            hh += 12

    # Convert components back to string in 24-hour format
    military_time = "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)
    return military_time

# Sample Input
s = "07:05:45PM"

# Convert to military time
result = timeConversion(s)
print(result)  # Output: "19:05:45"


# what is s[:-2]

# In the code s[:-2], s is a string, and [:-2] is a slicing operation in Python.

# s[:-2] means that you want to create a new string that consists of all characters 
# in the string s from the beginning (index 0) up to, but not including, the last two 
# characters. In other words, it removes the last two characters from the string s.

# For example, if s is "07:05:45PM", then s[:-2] will produce the string "07:05:45", 
# which is the part of the original string without "PM" at the end.