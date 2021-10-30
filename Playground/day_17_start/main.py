class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        # This is a default value and doesn't need to be added an argument.
        self.followers = 0


user_1 = User("001", "angela")
user_2 = User("002", "jack")


print(user_1.username)
