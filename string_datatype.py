# Concatenate strings
# Use the string to get input
# Format strings for output

myString = "This is a string."

print(myString)


print(type(myString))

print(myString + " is of the data type " + str(type(myString)))

# Concatenate strings
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

#input strings
name = input("What is your name? ")
print(name)

#format string
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))