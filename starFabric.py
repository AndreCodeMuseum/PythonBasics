# In this program the user will input a number of times that will print out "*" in a sequence

numberStars = int(input("Numbers of '*': "))

for i in range(numberStars):
    
    if i == numberStars - 1:
        print("*")
    else:

        print("*", end="_")

