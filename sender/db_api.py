import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine(r"sqlite:///C:\Users\student\Documents\Ковановський_Владислав\project14-1-back\first_project\db.sqlite3")

Base = declarative_base()
session = sessionmaker(bind=engine)