# Program that reads a speed limit in a highway and the driver's speed, then if the driver is above the limit but his speed is less than 20% of the speed limit he you receive a small fine, however if his speed is above 20% of the highway limit he must receive a major fine

highwayLimit = int(input("Highway speed limit: "))
driverSpeed = int(input("Drive's speed: "))
print()
# Calculation

aboveTwenty = highwayLimit * 1.2


if driverSpeed <= highwayLimit:
    print("Under the highway limits")

elif driverSpeed > highwayLimit and driverSpeed <= aboveTwenty:
    print("Above the highway limits : Small fine")

else:
    print("Above 20% of the highway limits: Major fine")


