from nose.tools import assert_raises
import unittest
import os

from swel.buoy import Buoy

class Buoy_test(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("SetUp()")
        cwd = os.getcwd()
        self.datadir = "{}/data".format(cwd)
        if not os.path.exists(self.datadir):
            os.makedirs(self.datadir)
        self.buoy = Buoy(46086)

    def test_get_data(self):
        dest = self.buoy.get_data()
        print("DEST: ",dest)
        assert dest != None, "get_data() returns a file path"
        path, dirs, files = next(os.walk(self.datadir))
        file_count = len(files)
        assert file_count > 0, "got the data file"

    @classmethod
    def tearDown(self):
        print("tearDown()")
        import shutil
        shutil.rmtree(self.datadir)
