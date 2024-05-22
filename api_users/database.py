# Honestly I don't know what this does at all. It creates or links a database file I guess.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://admin:Ut3c9208@database-1.c4lofrzrpfew.us-east-1.rds.amazonaws.com:3306/api_users"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./api_users.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()