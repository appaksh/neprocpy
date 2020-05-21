fruits = ["apple", "strawberry", "raspberry", "banana", "lemon"]
print("Number of items: ", len(fruits))
counter = 1
for fruit in fruits:
    print("fruit {}: {}".format(counter, fruit))
    counter += 1

print("")
fruitCount = len(fruits)
for index in range(5):
    print("fruit {}: {}".format((index+1), fruits[index]))

favoriteFruits = [1, 3, 4]
print("")

counter = 1
for favorite in favoriteFruits:
    print("favorite fruit {}: {}".format((counter), fruits[favorite-1]))
    counter += 1

# print("---------------------------------------- ")
#
# for num in range(5, 10):
#     print(num)
#
# print("--------------------------------------------- ")
#
# for loop in range(4, 40, 4):
#     print(loop)
