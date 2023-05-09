# Create a parking meter that give 30 minutes for 1.00$, 60 minutes for 1.75$, 120 minutes for 3.00$. And gives the change the client

money = float(input("Value $: "))
print()
# Process

if money < 1.0:

    NeedMore = 1.0 - money
    print("Not enough money")
    print("You need more: ", NeedMore)

elif money >= 1.0 and money < 1.75:
    changeMoney = money - 1.0
    print("Time: 30 minutes")
    print("Your change $:", changeMoney)

elif money >= 1.75 and money < 3.00:
    changeMoney = money - 1.75
    print("Time: 60 minutes")
    print("Your change $: ", changeMoney)

else:
    changeMoney = money - 3.00
    print("Time: 120 mintues")
    print("Your change $: ", changeMoney)
