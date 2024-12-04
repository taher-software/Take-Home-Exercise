import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL"
    ) or "sqlite:///" + os.path.join(basedir, "app.db")
    APISPEC_SPEC = APISpec(
        title="Take Home Exercise",
        version="v1.0",
        plugins=[MarshmallowPlugin()],
        openapi_version="2.0.0",
    )
    APISPEC_SWAGGER_URL = "/swagger/"  # Corresponds to Documentation
    APISPEC_SWAGGER_UI_URL = "/"  # Corresponds to MainSwagger UI
