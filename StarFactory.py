# a program that reads a number and uses this number to output "*" to the user. Each time a new repetition happens another "*" is added.

number = int(input("Number: "))


counter = 0
star = "*"

while counter < number:
    star = star
    print(star)
    counter+=1
    star+="*"
