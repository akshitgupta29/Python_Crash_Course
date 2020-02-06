# Self learning for the if else.
#author: akshitgupta29

# Testing for equality is case sensitive in Python.
car = 'audi'
print (car == 'audi') #False as the vales are considered differents.
# to avoid this, convert all the user input to any case of your choice and then do the comparison.

# Checking Multiple Conditions
# The keywords 'and' and 'or' can help you in these situations.

## Let's start the fun again !!!

if True:
    print ("Let's re-begin")


requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for topping in requested_toppings:
    if topping == 'mushrooms':
        print ('no mushroom')
    else:
        print (f"added {topping}")

print ('Done')

""" When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False."""

test_list = [1]
if test_list:
    print ('in the test list')
else:
    print ('no items found')
