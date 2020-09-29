bike1 = {
    "model": "MTT Y2K superBike ",
    "pickupSpeed": 2.5,
    "maxSpeed": 227
}
bike2 = {
    "model": "Kawasaki Ninja H2R ",
    "pickupSpeed": 2.5,
    "maxSpeed": 249
}
bike3 = {
    "model": "Dodge Tomahawk ",
    "pickupSpeed": 2.5,
    "maxSpeed": 483
}
bikes = [bike1, bike2, bike3]
for bike in bikes:
    print(bike.get("model"))

bikes = [bike1, bike2, bike3]
print(len(bikes))
index = 0
while index < len(bikes):
    print(bikes[index].get("model"))
    index = index + 1

print("")

lst = ['a', 'b', 'c']
print(lst[1:])

print("")

student1 = {
    "name": "Steve",
    "grade": 5,
    "rank": 1
}
student2 = {
    "name": "Alex",
    "grade": 5,
    "rank": 2
}
student3 = {
    "name": "Noob123",
    "grade": 5,
    "rank": 10
}

students = [student1, student2, student3]
print(len(students))
for student in students:
    print(student.get("name"))

students = [student1, student2, student3]
print(len(students))
count = 0
while count < len(students):
    print(students[count].get("name"))
    count = count + 1
