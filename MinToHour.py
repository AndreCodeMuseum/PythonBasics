# A program that reads the name of a movie and the length of it in minutes
# then display the name of the movie with the minutes converted in hours


movieName = input("Movie: ")
movieLength = int(input("Movie length in minutes: "))


# Calculation

hours = movieLength // 60
minutes = movieLength % 60


# Output

print("The movie is: ",hours, "hour(s)", "and", minutes, "min(s)")
