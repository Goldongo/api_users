from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DOCKER_MYSQL_HOST = "54.221.47.71"  
DOCKER_MYSQL_PORT = 3306


MYSQL_DATABASE = "users"
MYSQL_USER = "my_user"
MYSQL_PASSWORD = "my_password"

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{DOCKER_MYSQL_HOST}:{DOCKER_MYSQL_PORT}/{MYSQL_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()