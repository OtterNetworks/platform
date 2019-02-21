import unittest

from repositories import ItemRepository
from models.db_records import ItemRecord
from db import Session

class ItemRepositoryTest(unittest.TestCase):
  def setUp(self):
    self.model = ItemRecord(name='test', type='test', status='test')
    self.session = Session()
    self.repository = ItemRepository(self.session)

  def tearDown(self):
    self.repository.delete(self.model.id)
    self.session.flush()
    self.session.close()
    
  def test_item_repository_create_get(self):
    self.repository.save(self.model)
    self.session.flush()

    assert self.repository.get_by_id(self.model.id) is not None
    self.session.flush()
    self.session.close()
