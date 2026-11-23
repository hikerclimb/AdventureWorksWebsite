from sqlalchemy import String, Integer, create_engine, select
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column
import urllib

import json

class ConnectionRepo:

    def connecttoSQLServer(self):
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
        return engine
    
       
