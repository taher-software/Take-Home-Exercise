from TikTokApi import TikTokApi
import asyncio
import os
from app.orm import session
from app.models.users import Users
from app.decorators.transactionnal_decorators import trunsactional


class UserService:
    def __init__(self):
        self.ms_token = os.environ.get("ms_token", None)
        self._model = Users

    @trunsactional
    def create_user(self, metadata):
        new_record = self._model(**metadata)
        session.add(new_record)
        return metadata

    async def get_user_data(self, username: str, raw=False):
        result = dict()
        async with TikTokApi() as api:
            await api.create_sessions(
                ms_tokens=[self.ms_token],
                num_sessions=1,
                sleep_after=3,
            )
            user = api.user(username)
            user_data = await user.info()
            if raw:
                return user_data

            result["user_id"] = user_data["userInfo"]["user"]["uniqueId"]
            result["verified"] = user_data["userInfo"]["user"]["verified"]
            result["followerCount"] = user_data["userInfo"]["stats"]["followerCount"]
            result["followingCount"] = user_data["userInfo"]["stats"]["followingCount"]
            result["friendCount"] = user_data["userInfo"]["stats"]["friendCount"]
            return result
