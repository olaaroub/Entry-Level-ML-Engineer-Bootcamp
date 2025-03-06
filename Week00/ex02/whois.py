import sys

if (len(sys.argv) != 2  or not(sys.argv[1].isdigit())):
        print("Error: Invalid Arguments")
        exit(1)
num = int(sys.argv[1], 10)
if num == 0:
        print("I'm Zero")
elif num % 2 == 0:
        print("I'm Even")
else:
        print("I'm Odd")