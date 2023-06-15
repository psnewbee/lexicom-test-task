from core.services import redis_service
from core.models import ContactInfoModel, AddressInfoModel
from fastapi import APIRouter, HTTPException, responses

from typing import Any


router: APIRouter = APIRouter()

@router.get("/check_data", status_code=200)
async def check_info(phone: str) -> Any:
    
    if not await redis_service.exists(phone):
        raise HTTPException(detail='Data associated with provided phone number was not found', status_code=404)
    
    redis_data: dict = await redis_service.hgetall(phone)
    address_info: AddressInfoModel = AddressInfoModel(**redis_data)
    return address_info


@router.post("/write_data", status_code=200)
async def add_info(input_data: ContactInfoModel) -> Any:
    
    input_data = input_data.dict()
    phone = input_data.pop('phone')

    db_record_exist = bool(await redis_service.exists(phone))
    await redis_service.hmset(name=phone, mapping=input_data)
    
    if db_record_exist:
        return responses.PlainTextResponse(content="Address record updated", status_code=200)
    
    return responses.PlainTextResponse(content="Address record created", status_code=201)
    