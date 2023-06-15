from fastapi import APIRouter

router: APIRouter = APIRouter()

@router.get("/ping", status_code=200)
async def healthcheck() -> dict:
    return {"status": 'OK'}
