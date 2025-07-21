import unittest

from util import loadScript

def test_load_script_from_json():
  assert loadScript("custom") == "hi"