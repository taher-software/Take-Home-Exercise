from marshmallow import Schema
from marshmallow.fields import Bool, Str


class ResponseSchema(Schema):
    success = Bool()


class MessageResponseSchema(ResponseSchema):
    messages = Str()
