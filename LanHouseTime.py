# A program that reads the price for 15 minutes of computer usage in a lan house and the period that a user was logged in a computer.
# Then diplay how much the user needs to pay

pricePerFifteen = float(input("15 min $: "))
userUsage = int(input("User logged for (min):"))
print()

# Process

if userUsage <= 15:
    price = pricePerFifteen * 1
    print("price $: ", price)

if userUsage > 15 and userUsage <=30:
    price = pricePerFifteen * 2
    print("price $: ", price)

if userUsage > 30 and userUsage <=45:
    price = pricePerFifteen * 3
    print("price $: ", price)

if userUsage > 45 and userUsage <=60:
    price = pricePerFifteen * 4
    print("price $: ", price)

if userUsage > 60 and userUsage <=75:
    price = pricePerFifteen * 5
    print("price $: ", price)

if userUsage > 75 and userUsage <=90:
    price = pricePerFifteen * 6
    print("price $: ", price)

if userUsage > 90 and userUsage <=105:
    price = pricePerFifteen * 6
    print("price $: ", price)

if userUsage > 105 and userUsage <=120:
    price = pricePerFifteen * 6
    print("price $: ", price)

if userUsage > 120:
    price = pricePerFifteen * 10
    print("After 2 hours it is a fixed price for the rest of the day: $", price)








   
