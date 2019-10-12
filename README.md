# Axon-Text-File
 Python module for common tasks involving the Axon Text File format ([ATF](https://mdc.custhelp.com/app/answers/detail/a_id/18883/~/genepix%C2%AE-file-formats#atf)) from Molecular Devices

The ATF format module provides very basic Python functions for the reading, writing, and merging of Axon Text Files  from Molecular Devices. For reasons of memory-efficiency and compatibility with different experimental setups, the information is stored in a single NumPy array with subarrays representing the individual records - individual data is represented as strings.
If you know that your data records are numerical, you can easily change the ```dtype``` parameters for ```np.genfromtxt``` and ```np.savetxt``` to a numerical representation for futher calculations.

The ATF format unittest module was the basis for the test-driven development ([TDD](https://en.wikipedia.org/wiki/Test-driven_development)) process.

## Usage
Save the ATF format module file in the same folder as your main code and [import](https://docs.python.org/3/reference/simple_stmts.html#the-import-statement) its functions:
```
import atf_text
```
Then you can then call the three functions provided by the ATF format module:
```
# read an ATF file into a NumPy array
axon_data = axon_text.read(in_file='data.atf')

# copy a NumPy array into another file
axon_text.write(out_file='copy.atf', out_atf=axon_data)

# merge two NumPy arrays into a single NumPy array
axon_merge = axon_text.merge(in_atf_1=axon_data, in_atf_2=axon_data)
```

## Software requirements

If you want to use the ATF format module you'll need recent versions of [Python](https://www.python.org/downloads/) and [NumPy](https://www.scipy.org/scipylib/download.html). The latest Windows version of NumPy can be downloaded from [Christoph Gohlke's repository](https://www.lfd.uci.edu/~gohlke/pythonlibs/). These are my version recommendations:

- Python      (>= 3.7.4)
- NumPy       (>= 1.17.2)
