# Program to convert a decimal number to binary

# Read the decimal number from the user
decimal_number = int(input("Enter decimal number: "))

# Initialize an empty list to store the remainders
remainders = []

# Convert the decimal number to binary
while decimal_number > 0:
    remainder = decimal_number % 2  # Get the remainder when dividing by 2
    remainders.append(remainder)    # Append the remainder to the list
    decimal_number = decimal_number // 2  # Divide the number by 2

# Since we have stored remainders from bottom to top, we need to reverse the list
binary_number = ''.join(str(x) for x in remainders[::-1])  # Reverse the list and convert to string

# Print the result
print(f"The binary representation is: {binary_number}")
