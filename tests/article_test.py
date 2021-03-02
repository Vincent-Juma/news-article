import unittest
from app.models import Article

class TestArticle(unittest.TestCase):
  '''
  tests that article class is functional
  '''

  def setUp(self):
    '''
    set up method that will run before every test
    '''

    self.test_article = Article('', '', '', '', '', '', '')

  def test_instance(self):
    self.assertTrue(isinstance(self.test_article, Article))
