from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import env

username = env.MYSQL_USERNAME
password = env.MYSQL_PASSWORD
hostname = env.MYSQL_HOSTNAME
database = env.MYSQL_DATABASE
port = env.MYSQL_PORT

url = f"mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}?charset=utf8mb4"

engine = create_engine(url, encoding="utf-8", pool_size=3, max_overflow=-1, pool_recycle=60)

session: scoped_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))

Base = declarative_base()
Base.query = session.query_property()
