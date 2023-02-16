# Use the list data type
# Use the tuple data type
# Use the dictionary data type___

#Defining a list (mutable)
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#list by position
print(myFruitList[0])

print(myFruitList[1])

print(myFruitList[2])

#Changing the values in a list (mutable)
myFruitList[2] = "orange"

print(myFruitList)

#Defining a tuple (immutable)
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

#Accessing a tuple by position
#Like a list, the items of a tuple can also be accessed by position

print(myFinalAnswerTuple[0])

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])

#Defining a dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)

print(type(myFavoriteFruitDictionary))

#Accessing a dictionary by name
#use the name of the individuals to get their favorite fruit, instead of numbers.

print(myFavoriteFruitDictionary["Akua"])

print(myFavoriteFruitDictionary["Saanvi"])

print(myFavoriteFruitDictionary["Paulo"])
