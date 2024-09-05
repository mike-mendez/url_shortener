from datetime import datetime
from sqlalchemy import DateTime, Integer, String, UUID, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from uuid import uuid4


class Base(DeclarativeBase):
    pass


class Url(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uuid: Mapped[UUID] = mapped_column(
        String(36),
        nullable=False,
        default=lambda: str(uuid4()),
        unique=True,
        index=True,
    )
    url: Mapped[str] = mapped_column(String(255), nullable=False)
    short_code: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)
    visit_count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, nullable=False, default=datetime.now
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now,
    )
    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=1)
