from dataclasses import dataclass, field


@dataclass
class User:
    name: str
    friends: list = field(default_factory=list)
    posts: list = field(default_factory=list)

    def add_friend(self, friend):
        self.friends.append(friend)

    def add_post(self, post):
        self.posts.append(post)

    def list_posts(self):
        return self.posts
    

user = User(name="Mehmed")


user.add_friend("SAMsam")
user.add_friend("nigga")

user.add_post("PDP univer")
user.add_post("Family guy")

print(f'foydalanuvchi',user.name)
print(f'dustlar', user.friends)
print(f'postlar', user.posts)
print(user.list_posts)
