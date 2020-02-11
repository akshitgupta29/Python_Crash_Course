#author: akshitgupta29

#Soltuions to the try it yourself problems in the book
#NOTE: Some of the exercises done on my previous knowledge of the if, else and elif blocks.

#5.3, 5.4, 5.5
alien_color = 'green'
if 'red' == alien_color:
    print ('green found')
elif 'green'== alien_color:
    print ('yellow found')
else:
    print ('you are dead')

#5.7
favourite_food = ['aaple', 'kiwi', 'grapes']
if 'aaple' in favourite_food:
    print ("Apple found")
elif 'kiwi' in favourite_food:
    print ("Kiwi found") 

#5.8
usernames = ['admin', 'Akshit', 'Abhinav', 'Pradeep', 'Manju']

#To check if the users even exist in this list.
if usernames:
    #Iterating in the userlist
    for username in usernames:
        #If username is admin
        if username == 'admin':
            print(f"Hello {username}, would you like to see a status report?")
        else:
            print (f"Hello {username}, thank you for logging in again.")

#If no users are found
else:
        print ("we need to find some users")

#5.10
current_users = ['admin',  'Abhinav', 'Pradeep', 'Akshit','Manju']
new_users = ['admin', 'AKSHIT', 'Shrestha', 'Raunak', 'Surabhi']

for new_user in new_users:
    if new_user.lower() in [user.lower() for user in current_users]:
        print (f"username {new_user} is not available. Kindly choose another one.")
    else:
        print (f"username {new_user} is available.")

#5.11
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print (f"{number}st\n")    
    elif number == 2:
        print (f"{number}nd\n")
    elif number == 3:
        print (f"{number}rd\n")
    else:
        print (f"{number}th\n")






