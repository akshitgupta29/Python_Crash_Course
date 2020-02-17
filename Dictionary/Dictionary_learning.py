# Self learning for the Dictionary.
#author: akshitgupta29

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print (f"Original position {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print (f"new position is {alien_0['x_position']}")

print(alien_0['x_position'])
''' This will throw error and we will have to simply comment it'''
#print(alien_0['points'])

# get() function is used to have a default value in case the given key is not present in the given dictionary.
point = alien_0.get('points', "no value found")
print(point)

point = alien_0.get('x_position', "no value found")
print(point)

point = alien_0.get('points')
print(point)

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#for loop can be used to iterate the dictionary.
#dict.items() will return a key, value pair that can be used directly that can be used to iterate in the key, value. 
#title function is used to make the name in the title case. 
for name, language in favorite_languages.items():
    print (f"{name.title()}'s favourie language is {language.title()}")

#to iterate only over the keys, use the dict.keys() function
for key in favorite_languages.keys():
    print (f"Name is {key.title()}")

print ("------")

#By default only the keys are iterated over the dictionary, hence the value will have the same result.
for key in favorite_languages:
    print (f"Name is {key.title()}")

print ("------")

#Starting python 3.7 dictonaries are always returned as per the entry sequence.
'''But we can use functions like sorted() to get the values in the sorted values'''
for key in sorted(favorite_languages):
    print (key)

print ("------")

#Looping Through All Values in a Dictionary
# We can use the values functions to loop through all the values.

for value in favorite_languages.values():
    print (value)

print ("------")

#This approach pulls all the values from the dictionary without checking for repeats. That might work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list. This approach is called as using the set theory.

'''Nesting in the dictionaries'''

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print (alien)








