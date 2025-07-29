from sqlalchemy.ext.asyncio import AsyncSession
from app.models.order import OrderUpdate

class OrderService:
    @staticmethod
    async def update_order_status(order_id: int, order_update: OrderUpdate, db: AsyncSession):
        pass
