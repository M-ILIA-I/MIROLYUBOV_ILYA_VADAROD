from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from os import getenv
from dotenv import load_dotenv


load_dotenv()
Base = declarative_base()

async_engine = create_async_engine(getenv("DATABASE_URL"), echo=False)
async_session = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_async_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        