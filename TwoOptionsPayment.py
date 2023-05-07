# A program that reads the price of a product and gives to the client two option of payment
# One in cash and the and installment purchase in 3x, Payment in cash gives 10% discount

product = float(input("Product: "))
print()

# Calculation

tenDesc = product - ((product*1.10) - product )
installmentPayment = product / 3


# output

print("In cash (10% discount):", tenDesc, "$")
print("Or in 3x of:", installmentPayment, "$")
