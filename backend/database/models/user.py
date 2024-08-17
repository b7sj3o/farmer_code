from sqlalchemy import ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List, Any

from .. import Base


class User(Base):
    # id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int]
    username: Mapped[str]
    authenticated: Mapped[bool] = mapped_column(default=False)
    # resourses: Mapped[dict[str, Any]]