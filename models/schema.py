from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped,mapped_column

class Base(DeclarativeBase):
    pass

class Customer(Base):
    __tablename__ = "customer"
    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name : Mapped[str] 
    last_name : Mapped[str]
