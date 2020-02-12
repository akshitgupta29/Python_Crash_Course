#author: akshitgupta29

#Trying the exercise with the lambda expressions.
#NOTE: Some of the exercises done on my previous knowledge of the if, else and elif blocks.

current_users = ['admin',  'Abhinav', 'Pradeep', 'Akshit','Manju']
new_users = ['admin', 'AKSHIT', 'Shrestha', 'Raunak', 'Surabhi']



for new_user in new_users:
    check = lambda new_user: f"{new_user} cannot be formed" if new_user.lower() in [user.lower() for user in current_users] else f"{new_user} can be formed"
    print (check(new_user))
