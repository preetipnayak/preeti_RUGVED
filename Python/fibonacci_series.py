""" Write a program to print the Fibonacci sequence up to n values,
where n is provided by the user."""

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(__name__)
n=int(input("Enter the position: "))
print("The Fibonacci Series:\n")
for i in range(n+1):
       print(fib(i),end="   ")