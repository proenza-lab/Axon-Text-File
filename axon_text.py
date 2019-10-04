"""
Axon Text File (ATF) format module
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
import numpy as np


# functions

def read(in_file='atf'):
    """ read an atf file into a numpy array """
    try:
        with open(in_file, 'r') as in_data:
            pass
    except FileNotFoundError:
        raise

def write(out_file='atf'):
    """ write a numpy array into an atf file """
    with open(out_file, 'w') as out_data:
        pass

def merge(in_file1='atf', in_file2='atf', outfile='atf'):
    """ merge two atf files into one atf file """
    with open(in_file1, 'r') as in_data1:
        pass
    with open(in_file2, 'r') as in_data2:
        pass
    with open(out_file, 'w') as out_data:
        pass

if __name__ == "__main__":  # stand-alone execution
    pass
    