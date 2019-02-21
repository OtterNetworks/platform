from models.db_records import ItemRecord
from models.base_model import BaseModel


class Item(BaseModel):
  def __init__(self, params):
    super().__init__()
    self.attrs = params

  def to_db_record(self):
    return ItemRecord(**self.attrs)
    