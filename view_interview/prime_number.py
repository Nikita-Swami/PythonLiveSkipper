#Write a Function That Checks if a Number Is Prime or Not in Python user input

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n*0.5) + 1):
        if n % i == 0:
            return False

    return True

num = int(input("Enter the number:"))

if is_prime(num):
    print(num, "is a prime number")

else:
    print(num, "is not a prime number")
