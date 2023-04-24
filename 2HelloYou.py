import sys

# print(sys.argv)


# line = "hello %s!!" % sys.argv[1]
# print(line)


# print("hello " + sys.argv[1] + "!!")

# name = sys.argv[1]
# print(f"Hello {name}")


name = input("what is your name? ")
print("hello " + name)

year = input("what year were you born " + name + "? ")
age = 2023 - int(year)
print("you are " + str(age))



