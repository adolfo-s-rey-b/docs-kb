[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_hdf[#](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#pandas-read-hdf "Link to this heading")

==============================================================================================================================

pandas.read\_hdf(_path\_or\_buf_, _key\=None_, _mode\='r'_, _errors\='strict'_, _where\=None_, _start\=None_, _stop\=None_, _columns\=None_, _iterator\=False_, _chunksize\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L366-L538)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#pandas.read_hdf "Link to this definition")

Read from the store, close it if we opened it.

Retrieve pandas object stored in file, optionally based on where criteria. This function requires the [PyTables](https://www.pytables.org/)
 library.

Note

This function only reads HDF5 files written by pandas (via [`DataFrame.to_hdf()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")
, [`Series.to_hdf()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_hdf.html#pandas.Series.to_hdf "pandas.Series.to_hdf")
, or `HDFStore`), which use a pandas-specific layout built on PyTables. Arbitrary HDF5 files produced by other tools such as `h5py` or plain PyTables are not supported; use those libraries directly to read such files.

Warning

Pandas uses PyTables for reading and writing HDF5 files, which allows serializing object-dtype data with pickle when using the “fixed” format. Loading pickled data received from untrusted sources can be unsafe.

See: [https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
 for more.

Parameters:

**path\_or\_buf**str, path object, pandas.HDFStore

Any valid string path is acceptable. Only supports the local file system, remote URLs and file-like objects are not supported.

If you want to pass in a path object, pandas accepts any `os.PathLike`.

Alternatively, pandas accepts an open `pandas.HDFStore` object.

**key**object, optional

The group identifier in the store. Can be omitted if the HDF file contains a single pandas object.

**mode**{‘r’, ‘r+’, ‘a’}, default ‘r’

Mode to use when opening the file. Ignored if path\_or\_buf is a `pandas.HDFStore`. Default is ‘r’.

**errors**str, default ‘strict’

Specifies how encoding and decoding errors are to be handled. See the errors argument for [`open()`](https://docs.python.org/3/builtins/functions.html#open "(in Python v3.15)")
 for a full list of options.

**where**list, optional

A list of Term (or convertible) objects.

**start**int, optional

Row number to start selection.

**stop**int, optional

Row number to stop selection.

**columns**list, optional

A list of columns names to return.

**iterator**bool, optional

Return an iterator object.

**chunksize**int, optional

Number of rows to include in an iteration when using an iterator.

**\*\*kwargs**

Additional keyword arguments passed to HDFStore.

Returns:

object

The selected object. Return type depends on the object stored.

See also

[`DataFrame.to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")

Write an HDF file from a DataFrame.

`HDFStore`

Low-level access to HDF files.

Notes

When `errors="surrogatepass"`, `pd.options.future.infer_string` is true, and PyArrow is installed, if a UTF-16 surrogate is encountered when decoding to UTF-8, the resulting dtype will be `pd.StringDtype(storage="python", na_value=np.nan)`.

Examples

\>>> df \= pd.DataFrame(\[\[1, 1.0, "a"\]\], columns\=\["x", "y", "z"\])
\>>> df.to\_hdf("./store.h5", key\="data")
\>>> reread \= pd.read\_hdf("./store.h5")

Copy to clipboard

On this page