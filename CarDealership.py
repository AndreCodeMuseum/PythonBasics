# A program for a car dealership, It has to read the model of the vehicle and its priceand calculate how much the client need to pay for a 50% deposit and the installments after that in 12x

carModel = input("Vihecle: ")
price = float(input("Price $: "))
print()

# Calculation

depositFifty = (price * 1.5) - price

installmentsTwelve = depositFifty / 12


# Output

print("Car in sale: ", carModel)
print("50% deposit $:", depositFifty)
print("12x of $: ", installmentsTwelve)
