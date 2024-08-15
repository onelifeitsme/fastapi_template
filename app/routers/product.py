from typing import List
from sqlalchemy import select
from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import product as schemas
from models.product import Product
from fastapi import Depends
from database import get_async_session


router = APIRouter()

db_session = Depends(get_async_session)
@router.get('/products', response_model=List[schemas.ProductBase])
async def get_all_products(session: AsyncSession = db_session):
    result = await session.execute(select(Product))
    return result.scalars().all()
