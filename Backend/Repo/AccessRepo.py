from .ConnectionRepo import ConnectionRepo
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped
from sqlalchemy import select, Integer, String


class Base(DeclarativeBase):
    pass

class EmailAddress(Base):
    __tablename__ = "EmailAddress"
    __table_args__ = {"schema": "Person"}

    businessEntityId: Mapped[int] = mapped_column("BusinessEntityID", Integer, primary_key=True)
    emailAddressId: Mapped[int] = mapped_column("EmailAddressID", Integer, primary_key=True)
    emailAddress: Mapped[str] = mapped_column("EmailAddress", String(50), nullable=True)

class AccessRepo(ConnectionRepo):
    connection = None
    def __init__(self):
        self.connection = ConnectionRepo()


    def selectUser(self, emailaddress: str):
        engine = self.connection.connecttoSQLServer()
        with Session(engine) as session:
            stmt = select(EmailAddress.emailAddress).where(EmailAddress.emailAddress == emailaddress)
            return session.execute(stmt).scalar_one_or_none()
