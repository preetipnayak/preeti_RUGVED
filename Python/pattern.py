# Write a program to print the following patterns.

n = int(input("Enter: "))

for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

for i in range(n, 0, -1):
    print(" " * (n - i) + "* " * i)


























