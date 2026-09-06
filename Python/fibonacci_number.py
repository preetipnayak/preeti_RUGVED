# Find the Fibonacci number for a given input using recursion.

def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(__name__)
n=int(input("Enter the position: "))
print("The Fibonacci Number:",fib(n))

