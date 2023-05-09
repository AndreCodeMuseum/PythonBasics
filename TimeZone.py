# Create a program that reads the time in Brazil and converts to the French time zone in the summer (+5 hours)

hourBrazil = float(input("Time in Brazil: "))
print()

# Calculation

if hourBrazil < 24.00:

    frenchTime = hourBrazil + 5

    if frenchTime > 24:
        afterMid = frenchTime - 24
        print("Now its: ", afterMid, "a.m. in France")
    elif frenchTime >= 12:
        print("Now its: ",frenchTime, "p.m. in France")
    else:
        print("Now its: ",frenchTime, "a.m. in France")

else:
    print("Insert the hours correctly (hours and minutes)")
