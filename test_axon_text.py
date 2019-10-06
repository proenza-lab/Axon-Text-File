# imports

import axon_text
import io
import numpy as np
import os
import unittest
from unittest.mock import Mock


# classes

class FileObjectCase(unittest.TestCase):
    """ check for file object errors """
    
    def setUp(self):
        """ initialization for each test method """
        self.mock_path = os.path.join("")
        self.mock_file = Mock(spec=io.StringIO, return_value=self.mock_path)

    def tearDown(self):
        """ termination for each test method """
        pass

    def test_ReadFileCase(self):
        """ test read file object errors """
        self.assertRaises(FileNotFoundError, axon_text.read, self.mock_file())

class DataTypeObject(unittest.TestCase):
    """ check for data type errors """

    def setUp(self):
        """ initialization for each test method """
        pass

    def tearDown(self):
        """ termination for each test method """
        pass

    def test_ReadDataCase(self):
        """ test read data errors """
        axon_record = axon_text.read()
        self.assertIsInstance(axon_record, np.ndarray)
        self.assertEqual(axon_record.shape, (4,))

# functions

if __name__ == '__main__':  # stand-alone execution
    unittest.main()
    