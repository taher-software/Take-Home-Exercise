from ..orm import Model
from sqlalchemy import Column, Integer, String, Boolean


class Users(Model):
    __tablename__ = "users"
    user_id = Column(String(255), primary_key=True)
    verified = Column(Boolean, nullable=False)
    followerCount = Column(Integer, nullable=False)
    followingCount = Column(Integer, nullable=False)
    friendCount = Column(Integer, nullable=False)
