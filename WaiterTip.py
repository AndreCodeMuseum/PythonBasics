# Create a program that reads the total of a restaurant bill and adds 10% to the waiter's tip


bill = float(input("Bill $: "))

#Calculating the 10% of the waiter
print()
waiterTip = (bill * 1.10) - bill
TotalBill = bill + waiterTip
print("Your bill is: ",bill,"$")

# Output with the waiter tip and the total
print("The waiter tip is: ",waiterTip,"$")
print()
print("The total is: ",TotalBill,"$")



