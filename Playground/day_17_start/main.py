class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # This is a default value and doesn't need to be added an argument.
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

# This is user_1 following user_2, based on the follow method in the User Class.
user_1.follow(user_2)

print(user_1.followers)  # This is 0 because no one is follwing user_1
print(user_1.following)  # This is 1 because we set user_1 to follow user_2
