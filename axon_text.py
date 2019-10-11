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
            full_record = []  # python list
            for _ in range(0, 2):
                full_record.append(in_data.readline().strip().split())  # first and second record
            full_record.append([in_data.readline().strip() for line in range(0, int(full_record[1][0]))])  # optional record
            full_record.append(in_data.readline().strip().split('\t'))  # title record
            full_record.append(np.genfromtxt(in_data, delimiter='\t', autostrip=True))  # data record
    except FileNotFoundError:
        print("Error! File not found.")
        raise
    else:
        return np.array(full_record)  # ndarray.shape == (5,)

def write(out_file='atf', out_record=np.zeros((5,))):
    """ write a numpy array into an atf file """
    try:
        with open(out_file, 'w') as out_data:
            for array in out_record[0:2]:  # first and second record
                for element in array[0:-1]:
                    out_data.write(str(element) + '\t')
                out_data.write(str(array[-1] + '\n'))
            for array in out_record[2]:  # optional record
                out_data.write(str(array) + '\n')
            for element in out_record[3][0:-1]:  # title record
                out_data.write(str(element) + '\t')
            out_data.write(str(out_record[3][-1]) + '\n')
            np.savetxt(out_data, np.stack(out_record[4]), fmt='%.7f', delimiter='\t')
    except PermissionError:
        print("Error! No file permission.")
        raise

def merge(in_record_1=np.zeros((5,)), in_record_2=np.zeros((5,))):
    """ merge two atf files into one atf file """
    merge_record = []
    merge_record.append(["ATF", "1.0"])  # first record
    optional_record = in_record_1[2] + in_record_2[2]
    record_comment = str(len(optional_record))
    record_column = str(len(in_record_1[3]) if len(in_record_1[3]) >= len(in_record_2[3]) else in_record_2[3])
    merge_record.append([record_comment, record_column])  # second record
    merge_record.append(optional_record)  # optional record
    merge_record.append(in_record_2[3])  # title record
    data_rows_1, _ = in_record_1[4].shape  # rows, columns
    data_rows_2, _ = in_record_2[4].shape
    if data_rows_1 != data_rows_2:  # avoid memory-intensive reshaping
        print("Error! Array shapes incompatible.")
        merge_record.append(np.zeros(1))
    else:
        merge_record.append(np.concatenate((in_record_1[4], in_record_2[4])))
    return np.array(merge_record)

if __name__ == "__main__":  # stand-alone execution
    pass
    