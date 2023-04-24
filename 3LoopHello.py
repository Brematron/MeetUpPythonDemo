import sys

names = sys.argv[1].split(',')

for x in names:
    print('hello ' + x)
    if x == "bremnertron":
        print("wow you a totaly cool guy")
        break