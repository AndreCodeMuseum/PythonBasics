# Create a restaurant scale that calculates the food in grams and the price of the food is calculated in kilograms


foodKiloPrice = float(input("Price per kilogram $:"))
clientFoodGrams = int(input("Client's food (grams):"))
print()

# Processing

gramsToKilo = clientFoodGrams / 1000
foodPrice = foodKiloPrice * gramsToKilo

# Output

print("Price $: ",foodPrice)

