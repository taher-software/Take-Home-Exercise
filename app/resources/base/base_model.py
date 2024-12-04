from app.schemas.base.base_response import MessageResponseSchema
from flask_apispec import MethodResource, marshal_with
from flask_restful import Resource
from http import HTTPStatus


@marshal_with(
    MessageResponseSchema,
    code=HTTPStatus.INTERNAL_SERVER_ERROR,
    description=HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
)
class BaseResource(Resource, MethodResource):
    pass
