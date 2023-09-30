from flaskr.extensions import db
from flask_smorest import abort
from sqlalchemy.exc import SQLAlchemyError

from flaskr.models import UserModel


class UserController:
    def get_users(self):
        pass

    def create_user(self, user_data):
        pass
