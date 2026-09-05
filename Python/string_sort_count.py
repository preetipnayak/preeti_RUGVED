""" Write a Python program to sort a string alphabetically and 
print the count of each character. """

s=input("Enter a string: ")
s1=s.replace(" ","")
s2=""

sorted_s=''.join(sorted(s1,key=str.lower))
print("The entererd string",s,"after sorting: ",sorted_s)

for i in s1.lower():
    if i not in s2:
        s2+=i

for i in s2:
    print(i.upper(),":",s1.lower().count(i))




