# imports

import axon_text
import io
import os
import unittest
from unittest.mock import Mock


# classes

class FileObjectCase(unittest.TestCase):
    """ check for file object errors """
    
    def setUp(self):
        """ initialization for each test method """
        self.mock_path = os.path.join("")
        self.mock_file = Mock(spec=io.TextIOBase, return_value=self.mock_path)

    def tearDown(self):
        """ termination for each test method """
        pass

    def test_ReadFileCase(self):
        """ test read file object errors """
        self.assertRaises(FileNotFoundError, axon_text.read, self.mock_file())

# functions

if __name__ == '__main__':  # stand-alone execution
    unittest.main()
    