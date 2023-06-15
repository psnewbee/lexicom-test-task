from pydantic import BaseModel


class AddressInfoModel(BaseModel):
    """Address info model"""
    address: str

class ContactInfoModel(AddressInfoModel):
    """Contact info model."""
    phone: str
