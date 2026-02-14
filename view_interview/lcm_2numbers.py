def calculate_lcm(num1, num2):
    # selecting the greater number
    if num1 > num2:
        max_num = num1
    else:
        max_num = num2
    while (True):
        if max_num % num1 == 0 and max_num % num2 == 0:
            lcm = max_num
            break
        max_num += 1
    return lcm


# taking input from users
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
# printing the result for the users
print("The L.C.M. of ", num1, " and ", num2, " is ", calculate_lcm(num1, num2))