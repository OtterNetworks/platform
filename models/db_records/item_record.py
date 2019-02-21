from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class ItemRecord(Base):
  __tablename__ = 'item'

  id = Column('id', Integer, primary_key=True)
  name = Column('name', String, nullable=False)
  type = Column('type', String, nullable=False)
  status = Column('status', String, nullable=False)
