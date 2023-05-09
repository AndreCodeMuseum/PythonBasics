# read a number and tell if its possible to calculate its square root or not, if its possible then output the square root of the number

# Get the user input
number = int(input("Enter a number: "))

# Loop through all integers less than or equal to half the input number
for i in range(1, number // 2 + 1):
    # Check if the square of the integer is equal to the input number
    if i * i == number:
        print(f"{number} is a square number, with square root {i}")
        break
else:
    print(f"{number} is not a square number")


