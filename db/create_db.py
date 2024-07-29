import asyncio
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import select, update, delete




engine = create_async_engine('postgresql+asyncpg://haldey:root@127.0.0.1:5432/haldey', echo=True)

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class Reg(Base):
    __tablename__ = 'registr'

    id : Mapped[int] = mapped_column(primary_key=True)
    login : Mapped[str] = mapped_column(String(25))
    password : Mapped[str] = mapped_column(String(25))

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == '__main__':
    asyncio.run(async_main())
    