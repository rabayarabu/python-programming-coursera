def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Calculate the positions where apples and oranges land
    apple_positions = [a + d for d in apples]
    orange_positions = [b + d for d in oranges]

    # Count the number of apples and oranges that land on Sam's house
    apples_on_house = sum(1 for pos in apple_positions if s <= pos <= t)
    oranges_on_house = sum(1 for pos in orange_positions if s <= pos <= t)

    # Print the results
    print(apples_on_house)
    print(oranges_on_house)

# Sample Input
s, t = 7, 11
a, b = 5, 15
apples = [-2, 2, 1]
oranges = [5, -6]

# Call the function with the sample input
countApplesAndOranges(s, t, a, b, apples, oranges)
