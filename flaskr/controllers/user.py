from flaskr.extensions import db
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError

from flaskr.models import UserModel


class UserController:
    def get_users(self):
        return db.session.execute(db.select(UserModel)).scalars()

    def create_user(self, user_data):
        if db.session.execute(
            db.select(UserModel).filter_by(username=user_data["username"])
        ).first():
            abort(409, message="El nombre de usuario ya esta registrado.")

        user = UserModel(**user_data)
        user.set_password(user_data["password"])

        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500, message=str(e))

        return {"message": "Usuario creado exitosamente."}
