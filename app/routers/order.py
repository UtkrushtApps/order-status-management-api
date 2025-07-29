from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import OrderUpdate, OrderResponse
from app.db.session import get_db
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["orders"])

@router.put("/{order_id}", response_model=OrderResponse)
async def update_order_status(order_id: int, order_update: OrderUpdate, db: AsyncSession = Depends(get_db)):
    pass
