# Write a Python function to encrypt a string using Caesarʼs cipher.

def caesar(s,n):
    result=""
    for i in s:
        if i.isalpha():
            if i.islower():
                result+=chr((ord(i) - ord('a') +n) %26 + ord('a'))
            else:
                result+=chr((ord(i) - ord('A') +n) %26 + ord('A'))
        else:
            result+=i
    print("The encrypted string: ",result)

s=input("Enter a string: ")
n=int(input("Enter the shift: "))

caesar(s,n)
