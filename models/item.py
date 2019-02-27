from models.db_records import ItemRecord
from models.base_model import BaseModel


class Item(BaseModel):
  def __init__(self, params):
    super().__init__()
    self.attrs = params

  def to_db_record(self):
    return ItemRecord(**self.attrs)

  def from_db_record(self, record):
    attrs = {
      'id': record.id,
      'name': record.name,
      'status': record.status,
      'type': 'type'
    }
    return Item(self, attrs)
    