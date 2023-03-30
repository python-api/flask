from src import database


class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(150))
    content = database.Column(database.Text)

    def __repr__(self):
        return f'<Post "{self.title}">'