# An ATM machine that only cash out 10, 50 and 100$

cashOut = int(input("Cash out: "))
print()
# Process

if cashOut%10 == 0:
    
    cashHundred = cashOut % 100
    cashHundredBills = cashOut // 100
    
    cashFifty = cashHundred % 50
    cashFiftyBills = cashHundred // 50
    
    cashTen = cashFifty % 10
    cashTenBills = cashFifty // 10


    print("100$ bills: ", cashHundredBills)
    print("50$ bills: ", cashFiftyBills)
    print("10$ bilss: ", cashTenBills)
           


else: 
    print("Only values on base 10 can be cashed out.")

