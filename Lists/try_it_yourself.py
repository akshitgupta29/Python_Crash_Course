#author: akshitgupta29

#Soltuions to the try it yourself problems in the book
#NOTE: Some of the exercises done on my previous knowledge of the for loops.

#3.1 Names
names = ['Akshit', 'Abhinav', 'Ashutosh', 'Abhishek']
for name in names:
    print(name)

#3.2 
for name in names:
    print(f"Hello {name}")

# 3.3 
#done

# 3.4
guest_lists = ['a', 'b', 'c']
for name in guest_lists:
    print (f"You are invited to my party {name}")

# 3.5
print (f"{guest_lists[1]} cannot make it and hence replacing him")
guest_lists[1] = 'd'
print (guest_lists)

#3.6
print ("got another big table")
guest_lists.insert(0, 'e')
print (guest_lists)

guest_lists.insert(2, 'f')
print (guest_lists)

guest_lists.append('g')
print (guest_lists)

#3.7 
print ("change in plan, can invite only two people.")

removed_person = guest_lists.pop(1)
print (f"cannot invite {removed_person}")

removed_person = guest_lists.pop(1)
print (f"cannot invite {removed_person}")

removed_person = guest_lists.pop(1)
print (f"cannot invite {removed_person}")

removed_person = guest_lists.pop(1)
print (f"cannot invite {removed_person}")

print (guest_lists)
for name in guest_lists:
    print (f"congratulations {name}, you are still invited!")

# Deleting the remaining two as well.
del guest_lists[0]
del guest_lists[0]
print (guest_lists)

# 3.8
places_visited = ['Chennai', 'Delhi', 'Bengaluru', 'Hyd', 'Hisar']
print (places_visited)

print(sorted(places_visited))

print (f"back in the original form {places_visited}")

print (sorted(places_visited, reverse=True))

print (places_visited)
places_visited.reverse()
print (places_visited)

#Inplace functions cannot be used with the print function.
print (places_visited.sort())

