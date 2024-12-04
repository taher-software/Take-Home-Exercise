from app.resources.user.user_resources import UserResource
from app.resources.user.user_instance import UserInstanceResource


def add_routers(API, DOCS):
    API.add_resource(UserResource, "/user")
    DOCS.register(UserResource)
    API.add_resource(UserInstanceResource, "/user/<tiktok_identifier>")
    DOCS.register(UserInstanceResource)
