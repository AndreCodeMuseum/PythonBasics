# Read a number and subtract one by one until it reaches the number 1

number = int(input("Number: "))
print()
# Process
print("Between", number, "and 1:")
for i in reversed(range(0, number)) :
    i+=1
    
    if i ==1:
        print(i)

    else: 
        print(i,end=",")
