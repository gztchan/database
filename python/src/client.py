from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base


def make_engine(
    database_url: str,
    *,
    pool_size: int = 5,
):
    return create_engine(
        database_url,
        pool_pre_ping=True,
    )


def make_session_factory(engine: Engine):
    def session_factory():
        return sessionmaker(bind=engine, expire_on_commit=False)()
    return session_factory