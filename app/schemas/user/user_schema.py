from marshmallow import Schema, fields


class UserSchema(Schema):
    tiktok_username = fields.Str()
