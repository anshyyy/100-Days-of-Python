class User:
    def __init__(self, uid, name):
        self.id = uid
        self.username = name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
 


user_1 = User("010", "Anshuman")
user_2 = User("001", "Jay")
user_1.follow(user_2)
print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)

