# def calculateCupcakeCost(howManyCupsSold, cupsSpoilt, eachCupCost):
#     totalMoney = ((howManyCupsSold - cupsSpoilt) * eachCupCost) + (cupsSpoilt * eachCupCost * 0.15)
#     print(totalMoney)
#
#
# calculateCupcakeCost(250, 10, 12)
# calculateCupcakeCost(25, 3, 14)
# calculateCupcakeCost(150, 15, 21)
# print('The End...')
#
# cost = 30.3
# name = "orange"
# anotherName = "carrot"
# quantity = 15
# amISmart = 'false'
# isItTrue = True
#
# # "apple cost is $20.3, I have 5 of them"
# print(cost)
#
# print(name, "is a fruit")
# print(anotherName, "is a vegetable")
# print(name, "cost is $", cost, ", I have ", quantity, "of them")
# print("{} cost is ${}, I have {} of them".format(name, cost, quantity))
# print("%s cost is $%s, I have %s of them" % (name, cost, quantity))
#
# myFirstIteration = ["apple", "banana", "cherry"]
# myIter = (iter(myFirstIteration))
#
# count = 0
# while count < len(myFirstIteration):
#     print(next(myIter))
#     count = count + 1
#
#
# def print_each(myBeginningIteration):
#     myNewIteration = iter(myBeginningIteration)
#     while True:
#         try:
#             myFinalIteration = next(myNewIteration)
#         except StopIteration:
#             break  # Iterator exhausted: stop the loop
#         else:
#             print(myFinalIteration)
#
#
# language = "python"
# integerAmountOfStudents = 3
# print("The {l} class has {i} students. ".format(l=language, i=integerAmountOfStudents))
#
# place = "Round rock"
# allTime = 5
# transport = "car"
# print("{p} is {a} min away by {t}. ".format(p=place, a=allTime, t=transport))
#
# print("1. List: ")
# myList = ["Agustya", "Aakash", "Akshara"]
# print(len(myList))
# print(myList)
# print("")
# myList.append("Avani")
# print(len(myList))
# print(myList)
#
# print("2. Tuples: ")
# myTuple = ("Agustya", "Aakash", "Akshara")
# print(myTuple)
# print(len(myTuple))
#
# print("3. Set: ")
# mySet = {"Agustya", "Aakash", "Akshara"}
# print(len(mySet))
# print(mySet)
# print("")
# mySet.add("Avani")
# print(len(mySet))
# print(mySet)
#
# print("4. Dictionary: ")
# myDictionary = {
#     "Name": "Surendra",
#     "language": "Java, Python",
#     "years": 5
# }
# print(myDictionary)
# print("")
# print(myDictionary)
# myDictionary["favoriteColor"] = "yellow"


# age = int(input("What is your age? "))
# if age > 10:
#     print("Your age is a double digit!!! ")
# else:
#     print("You are young!!! ")


# age = int(input('What is your age? '))
# if age > 18:
#     print("I am an adult. ")
# elif age > 12:
#     print("I am a teenager. ")
# else:
#     print("I am a kid. ")
#
# def printMyTechs():
#     myTechList = ["raspberry pi ", "arduino ", "beaglebone "]
#     print(" ")
#     for myTechComputers in myTechList:
#         print(myTechComputers)
#
#
#  printMyTechs()
# printMyTechs()
# printMyTechs()
# printMyTechs()
#
# for myNums in range(1, 10 + 80 + 1):
#     print(myNums)
# else:
#     print("Finally finished! ")
#
# friends = ["Agystya ", "Chaitra ", "Kaushik ", "Anuj ", "Tejas "]
# indexCounter = 1
#
# for friend in friends:
#     print("friends: {cr}. {fr} ".format(cr=indexCounter, fr=friends))
#     print("friend: {cr}. {fr} ".format(cr=indexCounter, fr=friend))
#     print(" ")
#     indexCounter = indexCounter + 1
# else:
#     print("total elements printed are: ", indexCounter - 1)
#
# n1 = 1
# n2 = 1
# print(n1)
# print(n2)
#
# for x in range(70):
#     n3 = (n1 + n2)
#     print(n3)
#     n1 = n2
#     n2 = n3
