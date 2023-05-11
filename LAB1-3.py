print("Hello, World")
print("Python has three numeric types: int, float, and complex")
myValue0=1
print(myValue0)
print(type(myValue0))
print(str(myValue0) + " is of the data type " + str(type(myValue0)))

myValue1=3.14
print(myValue1)
print(type(myValue1))
print(str(myValue1) + " is of the data type " + str(type(myValue1)))

myValue2=5j
print(myValue2)
print(type(myValue2))
print(str(myValue2) + " is of the data type " + str(type(myValue2)))

myValue3=True
print(myValue3)
print(type(myValue3))
print(str(myValue3) + " is of the data type " + str(type(myValue3)))

myValue4=False
print(myValue4)
print(type(myValue4))
print(str(myValue4) + " is of the data type " + str(type(myValue4)))

myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)

color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"
print(myFruitList)
