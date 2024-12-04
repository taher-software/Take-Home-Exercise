from app.resources.base.base_model import BaseResource
from http import HTTPStatus
from flask_apispec import doc, use_kwargs, marshal_with
from app.schemas.response.response import DataResponseSchema, DataResult
from app.services.user.user_service import UserService
import asyncio


@doc(tags=["User"], produces=["application/json"])
class UserInstanceResource(BaseResource):
    def __init__(self):
        super().__init__()
        self._user_service = UserService()

    @marshal_with(DataResponseSchema)
    def get(self, tiktok_identifier):

        user_data = asyncio.run(
            self._user_service.get_user_data(tiktok_identifier, raw=True)
        )

        return DataResult(data=user_data)
