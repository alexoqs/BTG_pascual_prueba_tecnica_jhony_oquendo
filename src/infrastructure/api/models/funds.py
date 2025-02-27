from bson import ObjectId
from pydantic import BaseModel


class Found(BaseModel):
    _id: ObjectId
    name: str
    required_amount: int
    status: str
