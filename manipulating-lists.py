# Built-in functions and lists
# There are number of functions in python that takes lists as parameters

nums = [1, 2, 3, 4, 5, 6]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

greet = "Hello Everyone!"
split_gtreet = greet.split() # split() breaks string into parts and produces list of strings
for w in split_gtreet:
    print(w)  # we can access a particular word or loop through all the words
print(split_gtreet)
print(len(split_gtreet))

line = 'A lot of                spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
things = line.split()
print(things)
thing = line.split(';')
print(thing)

# When you do not specify delimiter, multiple spaces are treated as one delimiter.
# You can specify what delimiter character to use in the spliting().