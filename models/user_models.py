from exts import db
from werkzeug.security import generate_password_hash, check_password_hash


class UsersModel(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            'username': self.username
        }

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


