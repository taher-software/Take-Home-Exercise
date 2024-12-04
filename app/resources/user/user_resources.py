from app.resources.base.base_model import BaseResource
from http import HTTPStatus
from flask_apispec import doc, use_kwargs, marshal_with
from app.schemas.user.user_schema import UserSchema
from app.schemas.response.response import DataResponseSchema, DataResult
from app.services.user.user_service import UserService
import asyncio
from app.models.users import Users


@doc(tags=["User"], produces=["application/json"])
class UserResource(BaseResource):
    def __init__(self):
        super().__init__()
        self._user_service = UserService()

    @use_kwargs(UserSchema)
    @marshal_with(DataResponseSchema)
    def post(self, **create_user_data):

        user_data = asyncio.run(
            self._user_service.get_user_data(create_user_data["tiktok_username"])
        )

        new_user = self._user_service.create_user(user_data)

        return DataResult(data=new_user)
