# The client will receive a 50% discount on a product with he buys 3 items of that same product

prodName = input("Product: ")
price = float(input("Price $: "))

# Process

discountProduct = price * 0.5
total = price * 2 + discountProduct


# Output
print()
print(prodName, "Sale - Take 3 for $: ", total)
print("The last product has a 50% discount; $: ", discountProduct)
