# Write a program that reads 3 sides and tell if it is to possible to make a triangle or not. If its possible tell what type of triangle its is (equilateral, isosceles or scalene)

sideA = int(input("Side A: "))
sideB = int(input("Side B: "))
sideC = int(input("Side C: "))
print()
sumA = sideB + sideC
sumB = sideA + sideC
sumC = sideA + sideB


if sumA > sideA and sumB > sideB and sumC > sideC:
    print("It can be a triangle!")

    if sideA == sideB and sideA == sideC and sideB == sideC:
        print("Equilateral Triangle")
    
    elif sideA != sideB and sideA != sideC and sideB != sideC:
        print("Scalene Triangle")

    else:
        print("Isosceles Triangle")
else:
    print("Not a triangle")

