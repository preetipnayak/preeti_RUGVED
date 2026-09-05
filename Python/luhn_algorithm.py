""" Write a Python function to check whether a given credit card number 
is valid using Luhnʼs algorithm. 

The basic idea

Take the digits and:

1. Start from the last digit and move towards left.
2. Double every second digit (leaving the last digit).
3. If doubling gives a number greater than 9, subtract 9.
4. Add all the resulting digits (the ones doubled and the ones not).
5. If the final sum is divisible by 10, it passes the Luhn check. """

def luhn(n):

    n = str(n)

    sum = 0
    double = False

    for i in range(len(n)- 1, -1, -1):
        d = int(n[i])

        if double:
            d = d * 2
            if d > 9:
                d = d-9
        sum+=d
        double = not double

    if sum % 10 == 0:
        return True
    else:
        return False

n = input("Enter credit card number: ")

if luhn(n):
    print("Valid credit card number")
else:
    print("Invalid credit card number")