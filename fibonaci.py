# Fibonacci series asks users for input

first = 0
second = 1
nextNum = first + second
fib = input("How many numbers do you want? ")

for x in range(int(fib)):
    nextNum = first + second
    first = second
    second = nextNum
    print(nextNum)

print("{f} fibinacci numbers have been printed. ".format(f=fib))
