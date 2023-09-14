from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    cedula = fields.Str(required=True)
