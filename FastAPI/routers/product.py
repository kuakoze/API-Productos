### Product DB API ###

from fastapi import APIRouter, HTTPException, status
from db.models.product import Product
from db.schemas.product import product_schema, products_schema
from db.client import db_client
from bson import objectid

router = APIRouter(prefix="/productdb",
                   tags=["productdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})


@router.get("/", response_model=list[Product])
async def products():
    return products_schema(db_client.products.find())

@router