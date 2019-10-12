"""
Axon Text File (ATF) format unittest module
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

    def test_read_file_case(self):
        """ test read file object errors """
        mock_path = os.path.join("")
        mock_file = Mock(spec=io.StringIO, return_value=mock_path)
        self.assertRaises(FileNotFoundError, axon_text.read, mock_file())  # mock file oject as source

    def test_write_file_case(self):
        """ test write file object errors """
        self.assertRaises(PermissionError, axon_text.write, out_file='.')  # current directory as target

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
        axon_text.write(out_file='copy.atf', out_atf=self.axon_data)
        axon_copy = axon_text.read(in_file='copy.atf')
        self.assertEqual(self.axon_data[0:3].tolist(), axon_copy[0:3].tolist())  # python string list
        nptest.assert_array_equal(self.axon_data[4], axon_copy[4])  # numpy string array

    def test_merge_data_class(self):
        """ test for data merge errors """
        axon_merge = axon_text.merge(in_atf_1=self.axon_data, in_atf_2=self.axon_data)
        self.assertRaises(IndexError, axon_text.merge, np.zeros((1,)), np.zeros((2,)))
        self.assertIsInstance(axon_merge, np.ndarray)
        self.assertEqual(self.axon_data.shape, (5,))
        self.assertEqual(axon_merge[0], ["ATF", "1.0"])
        self.assertEqual(int(axon_merge[1][0]), len(axon_merge[2]) + 1)  # optional record
        self.assertEqual(int(axon_merge[1][1]), len(axon_merge[3][0]))  # title record
        self.assertEqual(int(axon_merge[1][1]), len(axon_merge[3][1]))
        self.assertEqual(int(axon_merge[1][1]), axon_merge[4][1].size)  # first data record
        self.assertEqual(int(axon_merge[1][1]), axon_merge[4][-1].size)  # last data record
        self.assertEqual(axon_merge[4].size, 2*self.axon_data[4].size)

# functions

if __name__ == '__main__':  # stand-alone execution
    unittest.main()
    