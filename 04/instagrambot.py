# 1 st step install insta bot then import
from instabot import Bot
from time import sleep
import os
import shutil

# Clean up previous login session (fixes login error)
if os.path.exists("config"):
    shutil.rmtree("config")

# Create bot variable then call Bot function
my_bot = Bot()

# Login
my_bot.login(username="proto_n101", password="Astik@321")

# Follow a user
my_bot.follow("indianfootball")
print("✅ Successfully followed 'indianfootball'.")

# Follow multiple users
my_bot.follow_users(["indiancricketteam", "mahi7781", "sachintendulkarsachintendulkar", "klrahul"])

# Send message
my_bot.send_message("hellow !", "astikmandal101")

# Like a user
my_bot.like_user("astikmandal101", amount=8)

# Comment
user_id = my_bot.get_user_id_from_username("stevedias796")
media_ids = my_bot.get_last_user_medias(user_id)  # returns a list
if media_ids:
    my_bot.comment(media_ids[0], "This is very nice. I like it!")

# Get list of followers of anyone
followers_list = my_bot.get_user_followers("astikmandal101")
following_list = my_bot.get_user_following("astikmandal101")

for count, each_follower in enumerate(followers_list):
    if count > 4:
        continue
    sleep(5)
    print(my_bot.get_username_from_user_id(each_follower))

for count1, each_follow in enumerate(following_list):
    if count1 > 4:
        continue
    sleep(5)
    print(my_bot.get_username_from_user_id(each_follow))

# Logout
my_bot.logout()
