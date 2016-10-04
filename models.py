from database import Base
from sqlalchemy import Column,Integer,String

class User(Base):
    __tablename__ = 'user'

    name = Column(String(64), index=True)
    phone = Column(Integer,index=True,primary_key=True)
