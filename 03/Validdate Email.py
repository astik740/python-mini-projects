# all condition 
# a-z all alpha bate
# 09
# ._ use 1 time
# @ use 1 time

# . positiuion 2 nd ya 3rd


# 1 st import regiex module
# in regix when start we use ^ simbol and 
# + sine help to join another 
# ? define 0 or 1
#  in regix  we serch any special character then use {}
import re

# Define the regular expression pattern for email validation
email_condition = "^[a-z]+[._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"

# Prompt user for email input
user_email = input("Enter your email: ")

# Perform the regex search
if re.search(email_condition, user_email):
    print("Right email")
else:
    print("Wrong email")


