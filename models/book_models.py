from exts import db


class BooksModel(db.Model):
    __tablename__ = "Books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    author = db.Column(db.String(20), nullable=False)
    publish_time = db.Column(db.DateTime, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            'name': self.name,
            'author': self.author,
            'publish_time': self.publish_time.isoformat()
        }
