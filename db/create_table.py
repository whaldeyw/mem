from sqlalchemy import select, update, delete
from create_db import Reg, async_session, engine
import asyncio
import asyncpg


async def set_user():
    async with async_session() as session:
        session.add(Reg(login = 'Mor', password='1234'))
        await session.commit()

# async def get_user():
#     async with async_session() as session:
#         # user = await session.scalar(select(User).where(User.name=='More'))
#         # print(user.name)
#         users = await session.scalars(select(User))
#         print([i.name for i in users])
#
# async def edit_user():
#     async with async_session() as session:
#         await session.execute(update(User).where(User.name== 'More').values(name='Gire'))
#         await session.commit()
#
# async def delete_user():
#     async with async_session() as session:
#         await session.execute(delete(User).where(User.name== 'Gire'))
#         await session.commit()



asyncio.run(set_user())