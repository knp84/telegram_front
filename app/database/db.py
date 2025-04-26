from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import User
class Database:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_user(self, id: int) -> None:
        user = await self.session.get(User, id)
        if not user:
            user = User(
                id=id
            )
            self.session.add(user)
        await self.session.commit()