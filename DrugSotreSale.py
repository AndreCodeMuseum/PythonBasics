# Create a program that if the client buys 2 of the same product he will get a discounto the total price of his purchase. The discount is by discarding the cents

productName = input("Product: ")
productPrice = float(input("Price: "))
print()

# Calculation
totalPurchase = int(productPrice) * 2

# Output
print(productName, "sale")
print()
print("Take 2 by $:", float(totalPurchase)) 

