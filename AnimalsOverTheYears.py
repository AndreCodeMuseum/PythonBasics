# Let's suppose that in a farm every dog that starts to live there, after the first year its population grows 3x times each year. Write a program that forsees the dog population growth over the year. 
# Remember its population grows 3x times only after the first year, you need to have at least 2 dog.

dogCount = int(input("Number of dogs: "))

yearCount= int(input("Years: "))
plusCount = yearCount + 1
print()
if dogCount > 1:

    for i in range(1,plusCount):
        
        print(i,"º year: ", dogCount, "dogs")
        dogCount*=3
else:
    print("One dog can not procreate alone")
