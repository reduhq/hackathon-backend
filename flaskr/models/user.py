import sqlalchemy as sa
from datetime import datetime
from flaskr.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(db.Model):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    email = sa.Column(sa.String(100), nullable=False, unique=True)
    password = sa.Column(sa.String(180), nullable=False)
    nombre = sa.Column(sa.String(40), nullable=False)
    apellido = sa.Column(sa.String(40), nullable=False)
    telefono = sa.Column(sa.String(10), nullable=False)
    estado = sa.Column(sa.Integer, nullable=False, default=1)
    fecha_creacion = sa.Column(
        sa.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_password(self, password):
        self.password = generate_password_hash(password)
