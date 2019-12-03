
import unittest
from setup import app
from config import Config

class TestBackendApp(unittest.TestCase):

  def test_hello(self):
    assert Config().envname() == "Development"

if __name__ == '__main__':
  unittest.main()
