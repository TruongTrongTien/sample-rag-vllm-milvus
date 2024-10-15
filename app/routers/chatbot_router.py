from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from app.schemas.base import GenericResponseModel

router = APIRouter(
    prefix="/test",
    tags=["test"],
    responses={404: {"description": "Not found"}},
)

@router.post("/")
async def test(data: str):
    return GenericResponseModel(data=data, status_code=200)