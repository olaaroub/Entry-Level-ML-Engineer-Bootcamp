import sys

#  collect reversed arguments in a variable to print later
args = [sys.argv[i].swapcase()[::-1] for i in range(len(sys.argv) - 1, 0, -1)]

print(" ".join(args))
