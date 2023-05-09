# the program will calculate whats the ideal weight for men or women based on height

name = input("Name: ")
genre = input("Genre (man or woman): ")
height = float(input("Height: "))
print()

# Calculation
if genre == "man":
    idealWeight = 22 * (height ** 2)
    print("Your ideal weight is:", idealWeight)

elif genre == "woman":
    idealWeight = 21 * (height **2)
    print("Your ideal weight is:", idealWeight)

else:
    print("Please choose man or woman")
