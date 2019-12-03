
import unittest
from setup import app

class TestBackendApp(unittest.TestCase):

  def test_hello(self):
    assert app.config.env_name() == "Development"

if __name__ == '__main__':
  unittest.main()
