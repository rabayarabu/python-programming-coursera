def repeatedString(s, n):
    # Calculate the number of 'a' in the original string 's'
    count_in_single_string = s.count('a')
    
    # Calculate how many times the whole string 's' is repeated
    repetitions = n // len(s)
    
    # Calculate the remaining characters at the end of the infinite string
    remaining_chars = n % len(s)
    
    # Calculate the total count of 'a' in the infinite string
    total_count = count_in_single_string * repetitions
    
    # Count 'a' in the remaining characters
    total_count += s[:remaining_chars].count('a')
    
    return total_count

# Example usage:
s = "aba"
n = 10
result = repeatedString(s, n)
print(result)  # Output: 7
