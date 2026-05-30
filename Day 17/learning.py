class User:
    def __init__(self,user_id,user_name):
        self.id = user_id
        self.name = user_name
        self.following = 0
        self.followers = 0

    def follow(self,user):
        self.following += 1
        user.followers += 1

user_1 = User(1,"Rahul")
user_2 = User(2,"Name")

user_1.follow(user_2)
user_1.follow(user_1)
user_2.follow(user_1)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)