def fibonacci_sequence(num):
    # Check if num input is 0 or 1
    if num == 0:
        # return empty list
        return []
    elif num == 1:
        # return 0
        return [0]
    # Initialize the sequence with the first two numbers
    sequence = [0, 1]
    # Append new numbers to the sequence until it has num terms
    while len(sequence) < num:
        # Calculate the next number as the sum of the previous two numbers
        next_num = sequence[-1] + sequence[-2]
        # Append the next number to the sequence
        sequence.append(next_num)
    # Return the complete sequence
    return sequence

# Test the function
n = int(input("Enter the number of terms: "))
print("The Fibonacci sequence:", fibonacci_sequence(n))

