from models import Item
from infrastructure.exceptions import InvalidModel
from repositories import ItemRepository


class ItemService:
  def __init__(self, session):
    self.session = session
    self.repository = ItemRepository(self.session)

  def save(self, params):
    item = Item(params)

    if item.is_invalid():
      raise InvalidModel(item.errors)
    
    db_record = item.to_db_record()
    self.repository.save(db_record)
    self.session.flush()
    item.attrs['id'] = db_record.id
    return item