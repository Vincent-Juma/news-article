import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
  '''
  test Source class behaviour
  Args:
    unittest.testCase: parent class with all test functions
  '''

  def setUp(self):
    self.test_source = Source(
      'abc-news',
      'ABC News',
      'Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.',
      'https://abcnews.go.com',
      'general',
      'en',
      'us'
    )

  def test_instance(self):
    self.assertTrue(isinstance(self.test_source, Source))