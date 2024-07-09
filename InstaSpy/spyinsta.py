import instaloader
import os



ig = instaloader.Instaloader()

# Login or load session
ig.login("UserName for your account", "Your Password ") # it's better to use .env file 

def highlits(name):
    profile = instaloader.Profile.from_username(ig.context, name)
    userid = profile.userid
    for highlight in ig.get_highlights(userid):
        os.mkdir(highlight.title)
        os.chdir(highlight.title)
        for item in highlight.get_items():
            ig.download_storyitem(item, name)
        os.chdir("..")
def reels(name):
    profile = instaloader.Profile.from_username(ig.context, name)
    userid = profile.userid
    for reel in ig.get_reels(userid):
        os.mkdir("reeels-" + reel.owner_username)
        os.chdir(reel.owner_username)
        for item in reel.get_items():
            ig.download_storyitem(item, name)
        os.chdir("..")

def stories(name):
    profile = instaloader.Profile.from_username(ig.context, name)
    userid = profile.userid
    for story in ig.get_stories(userid):
        os.mkdir("stories-" + story.owner_username)
        os.chdir("stories-" + story.owner_username)
        for item in story.get_items():
            ig.download_storyitem(item, name)
        os.chdir("..")


def start(name):
    ig.download_profile(name, profile_pic_only=False)
    os.chdir(name)
    highlits(name)
    reels(name)
