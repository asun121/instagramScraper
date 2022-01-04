import instaloader # type: ignore

username = input("username: ")

loader = instaloader.Instaloader()
loader.interactive_login(username)

profile = instaloader.Profile.from_username(loader.context, username)

followers = []
for follower in profile.get_followers():
    followers.append(follower)

followees = []
for followee in profile.get_followees():
    followees.append(followee)

# noFollowBack = []
for followee in followees:
    if followee not in followers:
        # noFollowBack.append(followee)
        print(followee)