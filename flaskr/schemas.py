from marshmallow import Schema, fields


class RoleSchema(Schema):
    id = fields.Int(dump_only=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str(required=False)
    estado = fields.Int(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    nombre = fields.Str(required=True)
    apellido = fields.Str(required=True)
    telefono = fields.Str(required=True)
    estado = fields.Int(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
