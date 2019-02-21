import unittest

from services import ItemService
from models.db_records import ItemRecord
from db import Session

class ItemRepositoryTest(unittest.TestCase):
  def setUp(self):
    self.session = Session()
    self.service = ItemService(self.session)

  def tearDown(self):
    self.session.query(ItemRecord).filter_by(name='test').delete()
    self.session.flush()
    self.session.close()
    
  def test_create_item_through_serivce(self):
    result = self.service.save({
      'name': 'test', 
      'type': 'test', 
      'status': 'test'
    })

    assert self.session.query(ItemRecord).filter_by(name='test').first() is not None
