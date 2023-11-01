def sockMerchant(n, ar):
    sock_count = {}  # Dictionary to store the count of each sock color

    # Count the socks of each color
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

    total_pairs = 0

    # Count the number of pairs for each sock color
    for count in sock_count.values():
        total_pairs += count // 2

    return total_pairs

# Sample input
n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

# Call the function and print the result
print(sockMerchant(n, ar))  # Output: 3