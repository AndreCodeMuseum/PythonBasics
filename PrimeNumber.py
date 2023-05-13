# A progrma tha tell wether a number is a prime number or not

primeNumber = int(input("Number: "))


if primeNumber > 1:

    for i in range(2,primeNumber):
        
        if primeNumber%i == 0:
            print(primeNumber, "not prime number")
            break
        
    else:
        print(primeNumber, "is prime number")

else:
    print(primeNumber, "not a prime number")
