"""
Axon Text File (ATF) format module - unittest module
Copyright (C) 2019 Christian Rickert <mail@crickert.de>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNBESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.

Version 1.0
"""

# imports

import io
import os
import unittest
from unittest.mock import Mock
import numpy as np
from numpy import testing as nptest
import axon_text

# classes

class FileObjectCase(unittest.TestCase):
    """ test for file object errors """

    def setUp(self):
        """ initialization for each test method """
        self.mock_path = os.path.join("")
        self.mock_file = Mock(spec=io.StringIO, return_value=self.mock_path)

    def test_read_file_case(self):
        """ test read file object errors """
        self.assertRaises(FileNotFoundError, axon_text.read, self.mock_file())

class DataTypeObject(unittest.TestCase):
    """ test for data errors """

    def setUp(self):
        """ initialization for each test method """
        self.axon_data = axon_text.read(in_file='data.atf')

    def tearDown(self):
        """ termination for each test method """
        try:
            os.remove('copy.atf')
        except FileNotFoundError:
            pass

    def test_read_data_case(self):
        """ test for data read errors """
        self.assertIsInstance(self.axon_data, np.ndarray)
        self.assertEqual(self.axon_data.shape, (5,))

    def test_write_data_case(self):
        """ test for data write errors """
        axon_text.write(out_file='copy.atf', out_record=self.axon_data)
        axon_copy = axon_text.read(in_file='copy.atf')
        self.assertEqual(self.axon_data[0:3].tolist(), axon_copy[0:3].tolist())  # string data
        nptest.assert_allclose(self.axon_data[4], axon_copy[4])  # numerical data

    def test_merge_data_class(self):
        """ test for data merge errors """
        axon_merge = axon_text.merge(in_file1='data.atf', in_file2='data.atf', out_file='merge.atf')
        self.assertIsInstance(axon_merge, np.ndarray)
        self.assertEqual(self.axon_data.shape, (5,))
        self.assertEqual(axon_merge[1][1], axon_merge[4][1].size)
        self.assertEqual(axon_merge[1][1], axon_merge[4][-1].size)
        self.assertEqual(axon_merge[4].size, 2*self.axon_data[4].size)

# functions

if __name__ == '__main__':  # stand-alone execution
    unittest.main()
    