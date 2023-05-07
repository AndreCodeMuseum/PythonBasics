# A program that splits a bill among a number of people


bill = float(input("Price: "))
client = int(input("Number of client:"))
print()


# Calculation
eachClient = bill / client


# output

print("Bill:",bill, "$")
print("This bill will be divided by:",client)
print("Each client will pay:", eachClient,"$")
