import sqlalchemy as sa
from flaskr.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    username = sa.Column(sa.String(20), nullable=False, unique=True)
    password = sa.Column(sa.String(180), nullable=False)
    nombre = sa.Column(sa.String(40), nullable=False)
    apellido = sa.Column(sa.String(40), nullable=False)
    cedula = sa.Column(sa.String(20), nullable=False, unique=True)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
