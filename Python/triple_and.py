""" Define a function named “triple_and” that takes three parameters and 
returns True only if all three are True; otherwise, return False. """

def triple_and(a,b,c):
    if (a and b and c):
        return True
    else:
        return False

def get_input(statement):
    while True:
        i=input(statement).strip().lower()
        if (i=="true"):
            return True
        elif (i=="false"):
            return False
        else:
            print("Invalid Input! Enter 'True' / 'False' !")

print(__name__)
print("Enter a, b and c values as 'True' / 'False' ")
a= get_input("Enter 'a' value: ")
b= get_input("Enter 'b' value: ")
c= get_input("Enter 'c' value: ")

result = triple_and(a,b,c)
print("The code returns: ", result)


