from sqlalchemy import ForeignKey, JSON
from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List, Any, Dict

from .. import Base


class User(Base):
    # id: Mapped[int] = mapped_column(primary_key=True)
    chat_id: Mapped[int]
    username: Mapped[str]
    authenticated: Mapped[bool] = mapped_column(default=False)
    responsed: Mapped[bool] = mapped_column(default=False)
    resources: Mapped[Dict[str, int]] = mapped_column(JSON, default={})