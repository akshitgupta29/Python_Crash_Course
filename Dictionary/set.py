# Self learning for the SET.
#author: akshitgupta29

#This approach pulls all the values from the dictionary without checking for repeats. That might work fine with a small number of values, but in a poll with a large number of respondents, this would result in a very repetitive list. 

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for  value in favorite_languages.values():
    print (value)

print ("------")

#To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique
for value in set(favorite_languages.values()):
    print (value)

print ("------")

