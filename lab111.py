#lab 111 13/5/26
#Defining a list

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)

#this is to add/remove more items
# myFruitList.append("pineapple")
# print(myFruitList)
#myFruitList.insert(2, "New Fruit")
#myFruitList.remove(2)

myFinalAnaswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnaswerTuple)
print(type(myFinalAnaswerTuple))

print(myFinalAnaswerTuple[0])
print(myFinalAnaswerTuple[1])
print(myFinalAnaswerTuple[2])

#accessing a dictionary by name
myFavoriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])