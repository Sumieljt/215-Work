#Using the input function 
name = input("What is your name? ")
print("Hi " + name)
color = input("What is your favorite color? ")
print(name  + " likes " + color)

#Using the input function for birth/year
year = input("What is your birth year? ")
age = 2020 - int(year)
print (age)

#Using input function for weight conversion
weight_lbs = input("What is your weight please? ")
pounds_kg = int(weight_lbs) * 0.454
print (pounds_kg)

#Using input function for motivation
motivation = input("How is your day going I care about how you feel? ")
motiv_good = True
motiv_bad = False
if motiv_good:
    print("I'm glad your enjoying your day! ")
elif motiv_bad:
    print("Thank you so much for joining me on my game. It was no nice meeting you. i hope you enjoyed")