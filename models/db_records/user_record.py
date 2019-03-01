from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class UserRecord(Base):
  __tablename__ = 'user'

  id = Column('id', Integer, primary_key=True)
  name = Column('email', String, nullable=False)
  type = Column('username', String, nullable=False)
  status = Column('token', String, nullable=False)