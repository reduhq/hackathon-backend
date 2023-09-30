import sqlalchemy as sa
from datetime import datetime
from flaskr.extensions import db


class RoleModel(db.Model):
    __tablename__ = "roles"

    id = sa.Column(sa.Integer, primary_key=True)
    nombre = sa.Column(sa.String(30), nullable=False)
    descripcion = sa.Column(sa.Text)
    estado = sa.Column(sa.Integer, nullable=False, default=1)
    fecha_creacion = sa.Column(
        sa.DateTime,
        nullable=False,
        default=datetime.utcnow,
    )
