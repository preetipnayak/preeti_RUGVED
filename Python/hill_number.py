# To check whether a given number is a hill number.
""" Hill Number first strictly increases then strictly decreases """

n= int(input("Enter a Number: "))
n1=[]
for i in str(n):
    n1.append(int(i))

increase=0
pos=0
for i in range(len(n1)-1):
    if (n1[i] < n1[i+1]):
        continue
    else:
        increase=1
        pos=i
        break

if (increase==0 or pos==len(n1)-1):
    print(n,"is not a Hill Number")

else:
    for i in range(len(n1)-1,pos,-1):
        if (n1[i] < n1[i-1]):
            continue
        else:
            print(n,"is not a Hill Number")
            break
    else:
        print(n,"is a Hill Number")


