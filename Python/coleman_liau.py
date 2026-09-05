""" Write a Python program that prints the grade level of a given text 
using the Coleman–Liau formula.
The formula is:
                 Grade=0.0588L−0.296S−15.8
where:
      L = average number of letters per 100 words
      S = average number of sentences per 100 words """

def coleman_liau(text):

    l= 0
    w= len(text.split())
    s= 0

    for i in text:

        if i.isalpha():
            l+=1

        if i == '.' or i == '!' or i == '?':
            s+=1

    L= (l/w)*100
    S= (s/w)*100

    grade= (0.0588 * L) - (0.296 * S) - 15.8
    return grade


text = input("Enter the text: ")
coleman_liau(text)
print("Grade level:",coleman_liau(text))