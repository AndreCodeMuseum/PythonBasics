# We have a perfect number when the sum of every integer divisors is equal to the number (except the number itself)

number = int(input("Number: "))
print()


counter = 1 
addUp = 0


while counter <= number:
    divi = number / counter 

    counter+=1 

    if divi%1 == 0 and divi != number:
        
        if counter == divi - 1:
            print(divi)
        else:
            print(divi, end="  ")

        addUp += float(divi)
print()
if addUp == number:
    print(number, "Perfect number")
else:
    print(number, "not a perfect number")

