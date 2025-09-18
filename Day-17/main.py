class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.followers_count = 0
        self.following_count = 0

        print("new User being created...")

    def follow(self, user):
        self.followers_count += 1
        user.following_count += 1

user_1 = User("001", "John", "john@abc.org")
# user_1.id = "001"
# user_1.username = "John"

print(user_1.id)
print(user_1.name)
print(user_1.email)
print(user_1.followers_count)

user_2 = User("002", "Jane", "jane@xyz.com")
user_2.follow(user_1)
print(user_2.followers_count)
print(user_2.following_count)

