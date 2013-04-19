'''
    test dice.py
'''
from dice import Die
import unittest
from time import sleep

class DieTest(unittest.TestCase):
    def setUp(self):
        self.tstDie = Die()
        sleep(1)

    def tearDown(self):
        self.tstDie = ''

    def test_value_ne_zero(self):
        self.assertTrue(self.tstDie.value != 0)

    def test_value_gt_zero(self):
        self.assertTrue(self.tstDie.value > 0)

    def test_value_is_int(self):
        self.assertEquals(type(self.tstDie.value), type(1))
    
    def test_value_is_lt_seven(self):
        self.assertTrue(self.tstDie.value < 7)

    def test_face_is_str(self):
        self.assertEquals(type(self.tstDie.face), type('xxx'))

if __name__ is "__main__":
    unittest.main()

