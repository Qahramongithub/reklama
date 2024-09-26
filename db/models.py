import os
from sqlalchemy import create_engine, DateTime, func, BigInteger
from sqlalchemy.orm import DeclarativeBase, declared_attr, Session
from sqlalchemy.orm import Mapped, mapped_column
from dotenv import load_dotenv
import psycopg2

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

engine = create_engine(f'postgresql+psycopg2://postgres:2505@localhost:5432/promo_db')
session = Session(bind=engine)

class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower() + 's'

class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(nullable=True)
    last_name: Mapped[str] = mapped_column(nullable=True)
    user_id: Mapped[int] = mapped_column(BigInteger)
    username: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime, server_default=func.now())

    def __repr__(self) -> str:
        return (f'User(id={self.id!r}, full_name={self.full_name!r}, last_name={self.last_name!r}, '
                f'user_id={self.user_id!r}, username={self.username!r})')

class Promo(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(nullable=True)
    dictionary: Mapped[str] = mapped_column(nullable=True)
    photo: Mapped[str] = mapped_column(nullable=True)
    video: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return (f'Promo(id={self.id!r}, title={self.title!r}, dictionary={self.dictionary!r}, '
                f'photo={self.photo!r}, video={self.video!r})')
class My(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    dectionary: Mapped[str] = mapped_column(nullable=True)
    photo: Mapped[str] = mapped_column(nullable=True)
    phone: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f'My(id={self.id!r}, dectionary={self.dectionary!r}, photo={self.photo!r}, phone={self.phone!r})'
Base.metadata.create_all(engine)
