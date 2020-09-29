thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = "apple"
print(type(thistuple))

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

print("---------------------------------------------------------------------------------------------------------------")
print("")
print("Tuple: ")
bikeTuple = ("bike: MTT Y2K superBike ", "0-60 mph: 2.5 ", "speed: 227 ")
print(bikeTuple)
print("")
bikeTuple = ("bike: Kawasaki Ninja H2R ", "0-60 mph: 2.5 ", "speed: 249 ")
print(bikeTuple)
print("")
bikeTuple = ("bike: Dodge Tomahawk  ", "0-60 mph: 2.5 ", "speed: 483 ")
print(bikeTuple)

print("")
print("List: ")
bikeList = ["bike: MTT Y2K superBike ", "0-60 mph: 2.5 ", "speed: 227 "]
print(bikeList)
print("")
bikeTuple = ["bike: Kawasaki Ninja H2R ", "0-60 mph: 2.5 ", "speed: 249 "]
print(bikeList)
print("")
bikeList = ["bike: Dodge Tomahawk  ", "0-60 mph: 2.5 ", "speed: 483 "]
print(bikeList)

print("")
print("Dictionary: ")
bikeDict = {
    "Bike ": "MTT Y2K superBike ",
    "0-60 mph ": 2.5,
    "speed ": 227
}
print(bikeDict)

print("")
bikeDict = {
    "Bike ": "Kawasaki Ninja H2 ",
    "0-60 mph ": 2.5,
    "speed ": 249
}
print(bikeDict)

print("")
bikeDict = {
    "Bike ": "Dodge Tomahawk ",
    "0-60 mph ": 2.5,
    "speed": 483
}
print(bikeDict)

print("")
print("Set: ")
bikeSet = {"bike: MTT Y2K superBike ", "0-60 mph: 2.5 ", "speed: 227 "}
print(bikeSet)
print("")
bikeSet = {"bike: Kawasaki Ninja H2R ", "0-60 mph: 2.5 ", "speed: 249 "}
print(bikeSet)
print("")
bikeSet = {"bike: Dodge Tomahawk  ", "0-60 mph: 2.5 ", "speed: 483 "}
print(bikeSet)

print("speed: ", bikeDict.get("speed"))
print("------------------------------------------------------------------------")

numCount = 2
while numCount < 5:
    print(numCount)
    if numCount == 5:
        break
    numCount += 1

# NumCount = (int) means the numCount will start at (int)
# while numCount < (int): means that it will amount the numbers in numCount
# if numCount == (int): means that it will go on till (int - 1)
# break      (look down)
# numCount += 1 these two lines (89 and 90) combined stops the process so this will not go on forever and will also...
# lines like this so we will not get an syntax
