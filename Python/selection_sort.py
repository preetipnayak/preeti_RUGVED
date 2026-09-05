# Write a Python function to perform selection sort on a given string.

def selection_sort(s1):
    s1= list(s1)

    for i in range(len(s1)):
        min_i = i

        for j in range(i+1,len(s1)):
            if (s1[j].lower() < s1[min_i].lower()):
                min_i = j

        s1[i],s1[min_i] = s1[min_i],s1[i]

    return s1

print(__name__)

s=input("Enter a string to sort: ")
print("The sorted string: ",''.join(selection_sort(s)))