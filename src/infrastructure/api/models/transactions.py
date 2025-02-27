from datetime import date
from bson import ObjectId
from pydantic import BaseModel


class Transactions(BaseModel):
    _id: ObjectId
    user_id: ObjectId
    fund_id: ObjectId
    type: str
    amount: str
    timestamp: date
