# Built-in functions and lists
# There are number of functions in python that takes lists as parameters

nums = [1, 2, 3, 4, 5, 6]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))

greet = "Hello Everyone!"
split_gtreet = greet.split()
for w in split_gtreet:
    print(w)
print(split_gtreet)
print(len(split_gtreet))