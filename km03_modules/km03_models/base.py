# from sqlalchemy import create_engine, inspect
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker, Session, relationship
# from .config import config
# import os


# Base = declarative_base()
# engine = create_engine(config.SQL_URI, echo = False, connect_args={"check_same_thread": False})
# Session = sessionmaker(bind = engine)
# sess = Session()
from sqlalchemy import create_engine, inspect, text
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from .config import config

Base = declarative_base()
# engine = create_engine(config.SQL_URI_WHAT_STICKS_DB, echo = False, connect_args={"check_same_thread": False})
engine = create_engine(config.SQL_URI, pool_recycle=3600)
DatabaseSession = sessionmaker(bind = engine)

