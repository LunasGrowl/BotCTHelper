import unittest

from app import utils

class TestLoad(unittest.TestCase):

  def test_load_script_from_json(self):
    self.assertEqual(utils.loadScript("custom"), ['hi'])

if __name__ == '__main__':
  unittest.main()