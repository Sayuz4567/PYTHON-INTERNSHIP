# Write a Program to create a list of n integer values and do the following

# Add an item in to the list

lst = list([1, 2, 3, 4, 5, 6])
lst.append(7)
print(lst,"\n")

# Delete an item from list

del lst[2]
print(lst)
del lst[0:2]
print(lst,"\n")

# Store the largest number from the list to a variable

A = list([15, 67, 34, 89, 1])
largest = max(A)
print("The Largest number is: ",largest,"\n")

# Store the Smallest number from the list to a variable

Smallest = min(A)
print("The Largest number is: ",Smallest,"\n")

# Create a tuple and print the reverse of the created tuple

x = (1, 2, 3, 4, 5)
rev = reversed(x)
print("The reverse of the tupple is: ",tuple(rev),"\n")

# or
# rev1 = x[::-1]
# print(rev1)


# Create a tuple and convert tuple into list

tu = ('my', 'name', 'is', 'Sayuz')
print(tu)
convert = list(tu)
print("The converted tuple into list is: ",convert,"\n")

OUTPUT:


[Running] python -u "c:\Users\SAYUZ\Desktop\Python-Internship\Day4.py"
[1, 2, 3, 4, 5, 6, 7] 

[1, 2, 4, 5, 6, 7]
[4, 5, 6, 7] 

The Largest number is:  89 

The Largest number is:  1 

The reverse of the tupple is:  (5, 4, 3, 2, 1) 

('my', 'name', 'is', 'Sayuz')
The converted tuple into list is:  ['my', 'name', 'is', 'Sayuz'] 


[Done] exited with code=0 in 0.278 seconds

