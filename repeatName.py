# write a name and a number of times you want that name to be repeated

name = input("Name: ")
repeat = int(input("Repetition: "))

for i in range(repeat):
    if i == repeat - 1:
        print(name)
    else:
        print(name,end=" * ")
