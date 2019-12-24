# Self learning for the lists
#author: akshitgupta29

#Displays all the elements including the square bracket
bicycles = ['Akshit', 'Abhinav', 'Manju', 'Pardeep']
print (bicycles)

#Only first element without square bracket
print(bicycles[0])

#For accessing the last element, we use -1 as the index.
print (bicycles[-1])

## Adding the elements to the list
# 1. Appending at the last of the list: The simplest way to add a new element to a list is to append the item to the list. When you append an item to a list, the new element is added to the end of the list.

bicycles.append('Ashutosh')
print(bicycles)

bicycles.insert(2, 'ABC')
print(bicycles)

print (bicycles.index('Akshit'))
