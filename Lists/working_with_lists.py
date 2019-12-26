# Self learning for the working of lists
#author: akshitgupta29

# Range function
# You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example, range(6) would return the numbers from 0 through 5.
for i in range(1,5):
    print (i)

for i in range(1,6):
    print (i)

numbers = list(range(1,6))
print (numbers)

#Print the even numbers
for i in range(2,11,2):
    print (i)

squares = []
for i in range (1,11):
    squares.append(i**2)
print (squares)

#Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print (f"The min is {min(digits)}")
print (f"the max is {max(digits)}")
print (f"The sum is {sum(digits)}")

#List Comprehensions
#A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element. 
squares = [value ** 2 for value in range(1,11)]
print (squares)