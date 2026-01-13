class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        for i in self.posts:
            print(i)
a= SocialMediaProfile('meow')
a.add_post('Hello, world!')
a.add_post('Had a great day at the park!')
a.add_post('What\'s up, Natalie? How are you?')
a.display_timeline()