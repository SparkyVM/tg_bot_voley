from sqlalchemy import BigInteger, Integer, Text, ForeignKey, String, Boolean, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from .database import Base


class User(Base):
    """Класс для таблицы Пользователи"""
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    full_name: Mapped[str] = mapped_column(String, nullable=True)

    # Отношение. Список броней Пользователя
    reserves: Mapped[list["Reserve"]] = relationship("Reserve", back_populates="user", cascade="all, delete-orphan")


class News(Base):
    """Класс для таблицы Новости"""
    __tablename__ = 'news'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=True)
    is_published: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


class Location(Base):
    """Класс для таблицы Местоположения"""
    __tablename__ = 'locations'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    adress: Mapped[str] = mapped_column(String, nullable=True)
    phone_number: Mapped[str] = mapped_column(String, nullable=True)
    courts_count: Mapped[int] = mapped_column(Integer, nullable=True)

    # Отношение. Список Кортов
    courts: Mapped[list["Court"]] = relationship("Court", back_populates="location", cascade="all, delete-orphan")

class Court(Base):#--------------------
    """Класс для таблицы Корт"""
    __tablename__ = 'courts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    court_name: Mapped[str] = mapped_column(String, nullable=True)
    capacity: Mapped[int] = mapped_column(Integer, nullable=True)
    location_id: Mapped[int] = mapped_column(Integer, ForeignKey("locations.id"))   # FK на Местоположение

    location = relationship("Location", back_populates="courts")        # Отношение. Зависимость от Местоположения
    # Отношение. Список броней на Корт
    reserves: Mapped[list["Reserve"]] = relationship("Reserve", back_populates="court", cascade="all, delete-orphan")


class Reserve(Base):#--------------------
    """Класс для таблицы Брони"""
    __tablename__ = 'reserves'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    date_reserve: Mapped[datetime] = mapped_column(Date, nullable=False)
    time_reserve: Mapped[datetime] = mapped_column(Integer, nullable=False)
    court_id: Mapped[int] = mapped_column(Integer, ForeignKey("courts.id"))     # FK на Корт
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))       # FK на Пользователя

    court = relationship("Court", back_populates="reserves")    # Отношение. Зависимость от Корт
    user = relationship("User", back_populates="reserves")      # Отношение. Зависимость от Пользователь


class Tournament(Base):
    """Класс для таблицы Соревнования"""
    __tablename__ = 'tournaments'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, nullable=True)
    date: Mapped[datetime] = mapped_column(Date, nullable=False)
    comands_quantity: Mapped[int] = mapped_column(Integer, nullable=True)
    contribution: Mapped[int] = mapped_column(Integer, nullable=True)
    prize: Mapped[int] = mapped_column(Integer, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)


class Info(Base):
    """Класс для таблицы Информация"""
    __tablename__ = 'info'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    text: Mapped[str] = mapped_column(Text, nullable=True)