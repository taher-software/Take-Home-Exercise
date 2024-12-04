from marshmallow import Schema
from marshmallow.fields import Bool, Str, List, Raw, Dict


class Response:
    def __init__(self, success=True):
        self.success = success


class MessageResponse(Response):
    def __init__(self, message, success=True):
        super().__init__(success)
        self.message = message if message else []


class DataResult(MessageResponse):
    def __init__(self, data, message=None, success=True):
        super().__init__(message)
        self.data = data


class ResponseSchema(Schema):
    success = Bool()


# class MessageResponseSchema(ResponseSchema):
#     message = List(Str())


class DataResponseSchema(ResponseSchema):
    data = Dict()
