from app import db
from app.models import User, Post
j = User(username='john', email='john@example.com')
s = User(username='susan', email='susan@example.com')
db.session.add(j)
db.session.add(s)
db.session.commit()

users = User.query.all()
for u in users:
    print(u.id, u.username)

u = User.query.get(1)
print(u)

p = Post(body='my first post!', author=u)
db.session.add(p)
db.session.commit()

# get all posts written by a user
posts = u.posts.all()
print(posts)
# same, but with a user that has no posts
u = User.query.get(2)
posts = u.posts.all()
print(posts)
# print post author and body for all posts
posts = Post.query.all()
for p in posts:
    print(p.id, p.author.username, p.body)


# get all users in reverse alphabetical order
User.query.order_by(User.username.desc()).all()
