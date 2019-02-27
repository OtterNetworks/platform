from models.db_records import ItemRecord
from sqlalchemy.orm.exc import NoResultFound


class ItemRepository:
  def __init__(self, session):
    self.session = session

  def save(self, item):
    self.session.add(item)

  def delete(self, id):
    self.session.query(ItemRecord).filter_by(id=id).delete()

  def find_single_by(self, **args):
    try:
        item = self.session.query(ItemRecord).filter_by(**args).one()
    except NoResultFound:
        return None
    return item