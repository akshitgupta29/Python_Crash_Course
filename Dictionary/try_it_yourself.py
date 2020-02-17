#author: akshitgupta29

#Soltuions to the try it yourself problems in the book
#NOTE: Some of the exercises done on my previous knowledge of the Dictoniaries and the maps.

#6.3
glossary = {'for':'to iterate', 'if':'conditions', 'else':'for else'}
for key, value in glossary.items():
    print (f"{key}: {value}")
    print (f"{key}\n\t{value}")

#6.6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

to_takes = ['Akshit', 'Shrestha', 'Jen', 'Sarah']

# for to_take in to_takes:
#     if to_take.title() in favorite_languages.keys():
#         print (f"{to_take}, thanks!")
#     else:
#         print (f"{to_take}, please take the poll")

#Reason why this code will not work as expected, is that we are expecting as the value is different i.e in different case, hence the issues are there. So, we need to convert the whole text to the title case in the dictionary and then do the run competition.

#To convert the text into the title case.
favorite_languages = {k.title():v for k,v in favorite_languages.items()}

#Now writing the program as per the logic:

for to_take in to_takes:
    if to_take.title() in favorite_languages:
        print (f"{to_take}, Thanks!")
    else:
        print (f"{to_take}, kindly take the test!")
