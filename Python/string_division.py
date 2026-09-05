""" Write a Python program to divide a given string into equal parts of n
characters (where n is provided by the user) that repeat the same sequence. 
Example: string = “abcdabcdabcdabcd”, n = 4 
         output: “abcd”, “abcd”, “abcd”, “abcd”. 
If the division is not possible or the sequence is not the same,
print an appropriate error. """

s=input("Enter a string: ")
n=int(input("Enter the size of equal parts: "))
l=[]
flag=1

if (len(s)%n==0):
    for i in range(0,len(s),n):
        l.append(s[i:i+n])

    c=l[0]
    for i in range(1,len(l)):
        if c==l[i]:
            continue
        else:
            flag=0
            
else:
    print("Division is not possible!!!")

if (flag==1):
    for i in l:
        print(i)
else:
    print("The sequence is not the same!!!")



















