# A program that reads a number and multiplicates it by 1 to 10 using the repetition structure

number = float(input("Number: "))
print()

# Process

for i in range(0,10):
    multi = (number*i) + number
    i+=1
    print(number,"x",i,"=",multi)


