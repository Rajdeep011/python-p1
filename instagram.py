from instabot import Bot
bot = Bot()
bot.login(username="rajdeep.kushwahh", password="Mayuri@14")
bot.follow('wscubetechindia')

bot.upload_photo("C:/Users/Mahakaal/OneDrive/Desktop/pthon.jpg", caption="i love python")
bot.unfollow('wscubetechindia')
bot.send_message("i love python", ["intense_eyes", "wscubetechindia"])
followers = bot.get_user_followers("rajdeep.kushwahh")
for follower in followers:
    print(bot.get_user_info(follower))

following = bot.get_user_following("rajdeep.kushwahh")    
for Following in following:
    print(bot.get_user_info(Following))
    
    