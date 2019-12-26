# Self learning for the lists
#author: akshitgupta29

#Displays all the elements including the square bracket
bicycles = ['Akshit', 'Abhinav', 'Manju', 'Pardeep', 'ABC']
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

#use of delete keyword (del) for deleting any element from the list
del bicycles[2]
print (bicycles)

popped = bicycles.pop()
print (popped)

removed = 'ABC'
bicycles.remove(removed)
print (f"{removed} is not needed")

# Sorting of the lists
# 1. Permanently using the sort command i.e. list.sort(). The sort() method, shown at ➊, changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to the original order:

cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
cars.sort()
print (cars)
cars.sort(reverse=True)
print (cars)


# 2. Displaying temporarily through the sorted function. To maintain the original order of a list but present it in a sorted order, you can use the sorted() function. The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.

print ("temporarily Sorting")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)
print (sorted(cars))
print (cars)
print (sorted(cars, reverse=True))

#Printing a List in Reverse Order
#To reverse the original order of a list, you can use the reverse() method. 
print (cars)
cars.reverse()
print (cars)
#getting back the original value
cars.reverse()
print (cars)

#Finding the Length of a List
#You can quickly find the length of a list by using the len() function.
#NOTE: Python counts the items in a list starting with one, so you shouldn’t run into any off-by-one errors when determining the length of a list.
print (len(cars))

#Index errors
lista = []
#print (lista[-1]) #it will throw error.

#Slicing
#Note: You can include a third value in the brackets indicating a slice. If a third value is included, this tells Python how many items to skip between items in the specified range.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:-2]:
    print (player)

#Copying a list
#This [:] is necessary as otherwise it will not copy the values from the list to the new list.
new_players = players [:]

#This syntax actually tells Python to associate the new variable players with the list that is already associated with new_players, so now both variables point to the same list. As a result, when we add 'cannoli' to players, it will also appear in new_players
new_players = players

