# Create a program that reads and stores the name and the price of a bill. It diplays it one by one and the total.

bills = []
totalPrice = 0

while True:
    billName = input("Bill (or type end to list and calculate your bills):")

    if billName == "end":
        break
    
    billPrice = float(input("$: "))

    # Adding billName and price to the list
    bills.append((billName,billPrice))

    # Add up the price to the total
    totalPrice += billPrice
print()
# list of bill output

print("BillName\tBillPrice")
for bill in bills:
    print(f"{bill[0]}\t{bill[1]}")

# total price output

print(f"\nTotal price: {totalPrice:.2f}")
print(f"bill (s): {len(bills)}")
