from nose.tools import assert_raises
import unittest

from swel.buoy import Buoy

class Buoy_test(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.buoy = Buoy(46086)

    # test case for the function file_search()
    def test_file_search(self):
        data = self.buoy.get_data()
        assert data != None
