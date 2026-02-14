#Write a Program to Reverse a String Using Slicing

def reverse_str(s):
    return s[::-1]

string_data = input("Enter a string")
rev = reverse_str(string_data)
print(rev)