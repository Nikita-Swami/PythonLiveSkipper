# Function to return minimum and maximum values in list
def find_min_max(numbers):
    return min(numbers), max(numbers)


# Take user input
user_input = input("Enter numbers separated by spaces: ")

# Convert input string to a list of integers
num_list = list(map(int, user_input.split()))

# Calling the function
minimum, maximum = find_min_max(num_list)

# Display results
print("Minimum value:", minimum)
print("Maximum value:", maximum)