from datetime import date
from typing_extensions import List
from pydantic import BaseModel, Field


class PersonalInfo(BaseModel):
    name: str
    lastname: str
    city: str


class ContactInfo(BaseModel):
    email: str
    phone: str


class Suscriptions(BaseModel):
    fund_id: str
    start_date: date
    end_date: date
    notification_preferences: List[str]
    invested_amount: float


class ClientResponse(BaseModel):
    id: str = Field(alias="_id")
    personal_info: PersonalInfo
    contact_info: ContactInfo
    balance: float
    suscriptions: Suscriptions
