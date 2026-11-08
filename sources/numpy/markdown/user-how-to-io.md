[Skip to main content](https://numpy.org/doc/stable/user/how-to-io.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/user/how-to-io.html)
[2.5 (stable)](https://numpy.org/doc/stable/user/how-to-io.html)
[2.4](https://numpy.org/doc/2.4/user/how-to-io.html)
[2.3](https://numpy.org/doc/2.3/user/how-to-io.html)
[2.2](https://numpy.org/doc/2.2/user/how-to-io.html)
[2.1](https://numpy.org/doc/2.1/user/how-to-io.html)
[2.0](https://numpy.org/doc/2.0/user/how-to-io.html)
[1.26](https://numpy.org/doc/1.26/user/how-to-io.html)
[1.25](https://numpy.org/doc/1.25/user/how-to-io.html)
[1.24](https://numpy.org/doc/1.24/user/how-to-io.html)
[1.23](https://numpy.org/doc/1.23/user/how-to-io.html)
[1.22](https://numpy.org/doc/1.22/user/how-to-io.html)
[1.21](https://numpy.org/doc/1.21/user/how-to-io.html)
[1.20](https://numpy.org/doc/1.20/user/how-to-io.html)
[1.19](https://numpy.org/doc/1.19/user/how-to-io.html)
[1.18](https://numpy.org/doc/1.18/user/how-to-io.html)
[1.17](https://numpy.org/doc/1.17/user/how-to-io.html)
[1.16](https://numpy.org/doc/1.16/user/how-to-io.html)
[1.15](https://numpy.org/doc/1.15/user/how-to-io.html)
[1.14](https://numpy.org/doc/1.14/user/how-to-io.html)
[1.13](https://numpy.org/doc/1.13/user/how-to-io.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Reading and writing files[#](https://numpy.org/doc/stable/user/how-to-io.html#reading-and-writing-files "Link to this heading")

================================================================================================================================

This page tackles common applications; for the full collection of I/O routines, see [Input and output](https://numpy.org/doc/stable/reference/routines.io.html#routines-io)
.

Reading text and [CSV](https://en.wikipedia.org/wiki/Comma-separated_values)
 files[#](https://numpy.org/doc/stable/user/how-to-io.html#reading-text-and-csv-files "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### With no missing values[#](https://numpy.org/doc/stable/user/how-to-io.html#with-no-missing-values "Link to this heading")

Use [`numpy.loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")
.

### With missing values[#](https://numpy.org/doc/stable/user/how-to-io.html#with-missing-values "Link to this heading")

Use [`numpy.genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")
.

[`numpy.genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")
 will either

*   return a [masked array](https://numpy.org/doc/stable/reference/maskedarray.generic.html#maskedarray-generic)
     **masking out missing values** (if `usemask=True`), or
    
*   **fill in the missing value** with the value specified in `filling_values` (default is `np.nan` for float, -1 for int).
    

#### With non-whitespace delimiters[#](https://numpy.org/doc/stable/user/how-to-io.html#with-non-whitespace-delimiters "Link to this heading")

\>>> with open("csv.txt", "r") as f:
...     print(f.read())
1, 2, 3
4,, 6
7, 8, 9

Copy to clipboard

##### Masked-array output[#](https://numpy.org/doc/stable/user/how-to-io.html#masked-array-output "Link to this heading")

\>>> np.genfromtxt("csv.txt", delimiter\=",", usemask\=True)
masked\_array(
  data=\[\[1.0, 2.0, 3.0\],\
        \[4.0, --, 6.0\],\
        \[7.0, 8.0, 9.0\]\],
  mask=\[\[False, False, False\],\
        \[False,  True, False\],\
        \[False, False, False\]\],
  fill\_value=1e+20)

Copy to clipboard

##### Array output[#](https://numpy.org/doc/stable/user/how-to-io.html#array-output "Link to this heading")

\>>> np.genfromtxt("csv.txt", delimiter\=",")
array(\[\[ 1.,  2.,  3.\],\
       \[ 4., nan,  6.\],\
       \[ 7.,  8.,  9.\]\])

Copy to clipboard

##### Array output, specified fill-in value[#](https://numpy.org/doc/stable/user/how-to-io.html#array-output-specified-fill-in-value "Link to this heading")

\>>> np.genfromtxt("csv.txt", delimiter\=",", dtype\=np.int8, filling\_values\=99)
array(\[\[ 1,  2,  3\],\
       \[ 4, 99,  6\],\
       \[ 7,  8,  9\]\], dtype=int8)

Copy to clipboard

#### Whitespace-delimited[#](https://numpy.org/doc/stable/user/how-to-io.html#whitespace-delimited "Link to this heading")

[`numpy.genfromtxt`](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html#numpy.genfromtxt "numpy.genfromtxt")
 can also parse whitespace-delimited data files that have missing values if

*   **Each field has a fixed width**: Use the width as the _delimiter_ argument.:
    
    \# File with width=4. The data does not have to be justified (for example,
    \# the 2 in row 1), the last column can be less than width (for example, the 6
    \# in row 2), and no delimiting character is required (for instance 8888 and 9
    \# in row 3)
    
    \>>> with open("fixedwidth.txt", "r") as f:
    ...    data \= (f.read())
    \>>> print(data)
    1   2      3
    44      6
    7   88889
    
    \# Showing spaces as ^
    \>>> print(data.replace(" ","^"))
    1^^^2^^^^^^3
    44^^^^^^6
    7^^^88889
    
    \>>> np.genfromtxt("fixedwidth.txt", delimiter\=4)
    array(\[\[1.000e+00, 2.000e+00, 3.000e+00\],\
           \[4.400e+01,       nan, 6.000e+00\],\
           \[7.000e+00, 8.888e+03, 9.000e+00\]\])
    
    Copy to clipboard
    
*   **A special value (e.g. “x”) indicates a missing field**: Use it as the _missing\_values_ argument.
    
    \>>> with open("nan.txt", "r") as f:
    ...     print(f.read())
    1 2 3
    44 x 6
    7  8888 9
    
    Copy to clipboard
    
    \>>> np.genfromtxt("nan.txt", missing\_values\="x")
    array(\[\[1.000e+00, 2.000e+00, 3.000e+00\],\
           \[4.400e+01,       nan, 6.000e+00\],\
           \[7.000e+00, 8.888e+03, 9.000e+00\]\])
    
    Copy to clipboard
    
*   **You want to skip the rows with missing values**: Set _invalid\_raise=False_.
    
    \>>> with open("skip.txt", "r") as f:
    ...     print(f.read())
    1 2   3
    44    6
    7 888 9
    
    Copy to clipboard
    
    \>>> np.genfromtxt("skip.txt", invalid\_raise\=False)  
    \_\_main\_\_:1: ConversionWarning: Some errors were detected !
        Line #2 (got 2 columns instead of 3)
    array(\[\[  1.,   2.,   3.\],\
           \[  7., 888.,   9.\]\])
    
    Copy to clipboard
    
*   **The delimiter whitespace character is different from the whitespace that indicates missing data**. For instance, if columns are delimited by `\t`, then missing data will be recognized if it consists of one or more spaces.:
    
    \>>> with open("tabs.txt", "r") as f:
    ...    data \= (f.read())
    \>>> print(data)
    1       2       3
    44              6
    7       888     9
    
    \# Tabs vs. spaces
    \>>> print(data.replace("\\t","^"))
    1^2^3
    44^ ^6
    7^888^9
    
    \>>> np.genfromtxt("tabs.txt", delimiter\="\\t", missing\_values\=" +")
    array(\[\[  1.,   2.,   3.\],\
           \[ 44.,  nan,   6.\],\
           \[  7., 888.,   9.\]\])
    
    Copy to clipboard
    

Read a file in .npy or .npz format[#](https://numpy.org/doc/stable/user/how-to-io.html#read-a-file-in-npy-or-npz-format "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

Choices:

*   Use [`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
    . It can read files generated by any of [`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
    , [`numpy.savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")
    , or [`numpy.savez_compressed`](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed")
    .
    
*   Use memory mapping. See [`numpy.lib.format.open_memmap`](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.open_memmap.html#numpy.lib.format.open_memmap "numpy.lib.format.open_memmap")
    .
    

Write to a file to be read back by NumPy[#](https://numpy.org/doc/stable/user/how-to-io.html#write-to-a-file-to-be-read-back-by-numpy "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

### Binary[#](https://numpy.org/doc/stable/user/how-to-io.html#binary "Link to this heading")

Use [`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
, or to store multiple arrays [`numpy.savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")
 or [`numpy.savez_compressed`](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed")
.

For [security and portability](https://numpy.org/doc/stable/user/how-to-io.html#how-to-io-pickle-file)
, set `allow_pickle=False` unless the dtype contains Python objects, which requires pickling.

Masked arrays [`can't currently be saved`](https://numpy.org/doc/stable/reference/generated/numpy.ma.MaskedArray.tofile.html#numpy.ma.MaskedArray.tofile "numpy.ma.MaskedArray.tofile")
, nor can other arbitrary array subclasses.

### Human-readable[#](https://numpy.org/doc/stable/user/how-to-io.html#human-readable "Link to this heading")

[`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
 and [`numpy.savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")
 create binary files. To **write a human-readable file**, use [`numpy.savetxt`](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy.savetxt "numpy.savetxt")
. The array can only be 1- or 2-dimensional, and there’s no `savetxtz` for multiple files.

### Large arrays[#](https://numpy.org/doc/stable/user/how-to-io.html#large-arrays "Link to this heading")

See [Write or read large arrays](https://numpy.org/doc/stable/user/how-to-io.html#how-to-io-large-arrays)
.

Read an arbitrarily formatted binary file (“binary blob”)[#](https://numpy.org/doc/stable/user/how-to-io.html#read-an-arbitrarily-formatted-binary-file-binary-blob "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use a [structured array](https://numpy.org/doc/stable/user/basics.rec.html)
.

**Example:**

The `.wav` file header is a 44-byte block preceding `data_size` bytes of the actual sound data:

chunk\_id         "RIFF"
chunk\_size       4\-byte unsigned little\-endian integer
format           "WAVE"
fmt\_id           "fmt "
fmt\_size         4\-byte unsigned little\-endian integer
audio\_fmt        2\-byte unsigned little\-endian integer
num\_channels     2\-byte unsigned little\-endian integer
sample\_rate      4\-byte unsigned little\-endian integer
byte\_rate        4\-byte unsigned little\-endian integer
block\_align      2\-byte unsigned little\-endian integer
bits\_per\_sample  2\-byte unsigned little\-endian integer
data\_id          "data"
data\_size        4\-byte unsigned little\-endian integer

Copy to clipboard

The `.wav` file header as a NumPy structured dtype:

wav\_header\_dtype \= np.dtype(\[\
    ("chunk\_id", (bytes, 4)), \# flexible-sized scalar type, item size 4\
    ("chunk\_size", "<u4"),    \# little-endian unsigned 32-bit integer\
    ("format", "S4"),         \# 4-byte string, alternate spelling of (bytes, 4)\
    ("fmt\_id", "S4"),\
    ("fmt\_size", "<u4"),\
    ("audio\_fmt", "<u2"),     #\
    ("num\_channels", "<u2"),  \# .. more of the same ...\
    ("sample\_rate", "<u4"),   #\
    ("byte\_rate", "<u4"),\
    ("block\_align", "<u2"),\
    ("bits\_per\_sample", "<u2"),\
    ("data\_id", "S4"),\
    ("data\_size", "<u4"),\
    #\
    \# the sound data itself cannot be represented here:\
    \# it does not have a fixed size\
\])

header \= np.fromfile(f, dtype\=wave\_header\_dtype, count\=1)\[0\]

Copy to clipboard

This `.wav` example is for illustration; to read a `.wav` file in real life, use Python’s built-in module [`wave`](https://docs.python.org/3/library/wave.html#module-wave "(in Python v3.14)")
.

(Adapted from Pauli Virtanen, [Advanced NumPy](https://scipy-lectures.org/advanced/advanced_numpy/index.html#advanced-numpy "(in Scipy lecture notes v2022.1)")
, licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
.)

Write or read large arrays[#](https://numpy.org/doc/stable/user/how-to-io.html#write-or-read-large-arrays "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

**Arrays too large to fit in memory** can be treated like ordinary in-memory arrays using memory mapping.

*   Raw array data written with [`numpy.ndarray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")
     or [`numpy.ndarray.tobytes`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tobytes.html#numpy.ndarray.tobytes "numpy.ndarray.tobytes")
     can be read with [`numpy.memmap`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.html#numpy.memmap "numpy.memmap")
    :
    
    array \= numpy.memmap("mydata/myarray.arr", mode\="r", dtype\=np.int16, shape\=(1024, 1024))
    
    Copy to clipboard
    
*   Files output by [`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
     (that is, using the numpy format) can be read using [`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
     with the `mmap_mode` keyword argument:
    
    large\_array\[some\_slice\] \= np.load("path/to/small\_array", mmap\_mode\="r")
    
    Copy to clipboard
    

Memory mapping lacks features like data chunking and compression; more full-featured formats and libraries usable with NumPy include:

*   **HDF5**: [h5py](https://www.h5py.org/)
     or [PyTables](https://www.pytables.org/)
    .
    
*   **Zarr**: [here](https://zarr.readthedocs.io/en/stable/tutorial.html#reading-and-writing-data)
    .
    
*   **NetCDF**: [`scipy.io.netcdf_file`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.io.netcdf_file.html#scipy.io.netcdf_file "(in SciPy v1.18.0)")
    .
    

For tradeoffs among memmap, Zarr, and HDF5, see [pythonspeed.com](https://pythonspeed.com/articles/mmap-vs-zarr-hdf5/)
.

Write files for reading by other (non-NumPy) tools[#](https://numpy.org/doc/stable/user/how-to-io.html#write-files-for-reading-by-other-non-numpy-tools "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Formats for **exchanging data** with other tools include HDF5, Zarr, and NetCDF (see [Write or read large arrays](https://numpy.org/doc/stable/user/how-to-io.html#how-to-io-large-arrays)
).

Write or read a JSON file[#](https://numpy.org/doc/stable/user/how-to-io.html#write-or-read-a-json-file "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

NumPy arrays and most NumPy scalars are **not** directly [JSON serializable](https://github.com/numpy/numpy/issues/12481)
. Instead, use a custom [`json.JSONEncoder`](https://docs.python.org/3/library/json.html#json.JSONEncoder "(in Python v3.14)")
 for NumPy types, which can be found using your favorite search engine.

Save/restore using a pickle file[#](https://numpy.org/doc/stable/user/how-to-io.html#save-restore-using-a-pickle-file "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

Avoid when possible; [pickles](https://docs.python.org/3/library/pickle.html "(in Python v3.14)")
 are not secure against erroneous or maliciously constructed data.

Use [`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
 and [`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
. Set `allow_pickle=False`, unless the array dtype includes Python objects, in which case pickling is required.

[`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
 and [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "(in Python v3.14)")
 submodule also support unpickling files created with NumPy 1.26.

Convert from a pandas DataFrame to a NumPy array[#](https://numpy.org/doc/stable/user/how-to-io.html#convert-from-a-pandas-dataframe-to-a-numpy-array "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

See [`pandas.Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "(in pandas v3.0.3)")
.

Save/restore using [`tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")
 and [`fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")
[#](https://numpy.org/doc/stable/user/how-to-io.html#save-restore-using-tofile-and-fromfile "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In general, prefer [`numpy.save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")
 and [`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load "numpy.load")
.

[`numpy.ndarray.tofile`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile "numpy.ndarray.tofile")
 and [`numpy.fromfile`](https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html#numpy.fromfile "numpy.fromfile")
 lose information on endianness and precision and so are unsuitable for anything but scratch storage.

On this page