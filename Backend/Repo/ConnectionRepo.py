from sqlalchemy import String, Integer, create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
import urllib

import json

class Base(DeclarativeBase):
    pass


class EmailAddress(Base):
    __tablename__ = "EmailAddress"
    __table_args__ = {"schema": "Person"}

    EmailAddressId: Mapped[int] = mapped_column(Integer, primary_key=True)
    EmailAddress: Mapped[str] = mapped_column(String(100), nullable=False)

    '''def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, email={self.email!r})"'''

class ConnectionRepo:

    def __init__(self):
        with open("Repo/config.json", "r", encoding="utf-8") as file:
            config = json.load(file)

        print("before connection")
        odbc_str = (
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=localhost\MSSQLSERVER03;"
            "DATABASE=AdventureWorks2022;"
            "UID="+config["username"]+";"
            "PWD="+config["password"]+";"
        )
        quoted_conn_str = urllib.parse.quote_plus(odbc_str)
        print("out")
        engine = create_engine(f"mssql+pyodbc:///?odbc_connect={quoted_conn_str}")   

    
        with Session(engine) as session:
            stmt = select(EmailAddress)
            fetched_user = session.scalars(stmt).first()
            print("Fetched from DB:", fetched_user)

