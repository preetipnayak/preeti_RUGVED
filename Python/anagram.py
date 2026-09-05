# Create a function that checks whether a given string is an anagram.
# Ex: Silent and Listen 

def anagram(s1,s2):
    if sorted(s1.lower())==sorted(s2.lower()):
        print(s1,s2,"are Anagrams")
    else:
        print(s1,s2,"are not Anagrams")

s1=input("Enter a word: ")
s2=input("Enter a word: ")

anagram(s1,s2)