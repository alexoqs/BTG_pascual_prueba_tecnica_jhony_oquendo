from datetime import date


class PersonalInfo:
    def __init__(self, name: str, lastname: str, city: str):
        self.name = name
        self.lastname = lastname
        self.city = city


class ContactInfo:
    def __init__(self, email: str, phone: str):
        self.email = email
        self.phone = phone


class Suscriptions:
    def __init__(
        self,
        fund_id: str,
        start_date: date,
        end_date: date,
        notification_preferences: list[str],
        invested_amount: float
    ):
        self.fund_id = fund_id
        self.start_date = start_date
        self.end_date = end_date
        self.notification_preferences = notification_preferences
        self.invested_amount = invested_amount


class ClientEntity:
    def __init__(
        self, id: int,
        personal_info: PersonalInfo,
        contact_info: ContactInfo,
        balance: float,
        suscriptions: Suscriptions
    ):
        self.id = id
        self.personal_info = personal_info
        self.contact_info = contact_info
        self.balance = balance
        self.suscriptions = suscriptions
