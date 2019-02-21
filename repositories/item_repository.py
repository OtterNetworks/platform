from models.db_records import ItemRecord
from sqlalchemy.orm.exc import NoResultFound


class ItemRepository:
  def __init__(self, session):
    self.session = session

  def save(self, item):
    self.session.add(item)

  def get_by_id(self, id):
    try:
        case = self.session.query(ItemRecord).filter_by(id=id).one()
    except NoResultFound:
        return None
    return case

  def delete(self, id):
    self.session.query(ItemRecord).filter_by(id=id).delete()