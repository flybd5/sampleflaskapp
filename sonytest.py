import os
import requests
import unittest
import sonyflask

class SonyflaskTestCase(unittest.TestCase): 

  # initialization logic for the test suite declared in the test module
  # code that is executed before all tests in one test run
  @classmethod
  def setUpClass(cls):
    # None needed
    pass

  # clean up logic for the test suite declared in the test module
  # code that is executed after all tests in one test run
  @classmethod
  def tearDownClass(cls):
    # None needed
    pass 

  # initialization logic
  # code that is executed before each test
  def setUp(self):
    self.app = sonyflask.app.test_client()
    self.app.testing = True 

  # clean up logic
  # code that is executed after each test
  def tearDown(self):
    # None needed
    pass 

# Test that there are some titles in the list when requesting all

  def test_request_all(self):
    resp = self.app.get('/games/')
    assert b"XCOM 2: War of the Chosen" in resp.data
    assert b"Undertale" in resp.data
    assert b"Nioh: Bloodshed's End" in resp.data
    assert b"Dark Star One" not in resp.data

# Test that when requesting one specific game, correct one is returned when specified
# and not there when misspelled

  def test_request_singles(self):
    resp = self.app.get('/game/sonic-mania')
    assert b'Sonic Mania' in resp.data
    resp = self.app.get('/game/sonic-man')
    assert b'Sonic Mania' not in resp.data

if __name__ == '__main__':
  unittest.main()
