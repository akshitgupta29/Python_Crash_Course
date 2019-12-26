# Self learning for the tuples
#author: akshitgupta29

#sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple.

#Defining a tuple:
# A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

dimensions =(200,50)
for dimension in dimensions:
    print (dimension)

#TypeError as basically, because we’re trying to alter a tuple, which can’t be done to that type of object, Python tells us we can’t assign a new value to an item in a tuple
#dimensions[0] = 250

#NOTE: Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma:#
    # my_t = (3,)

#we can reassign the variable representing the tuple, so as to we can have some fun within it.
dimensions = (400,500)
for dimension in dimensions:
    print(dimension)

#NOTE: Use them when you want to store a set of values that should not be changed throughout the life of a program.