[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_hdf.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_hdf[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_hdf.html#pandas-series-to-hdf "Link to this heading")

=============================================================================================================================================

Series.to\_hdf(_path\_or\_buf_, _\*_, _key_, _mode\='a'_, _complevel\=None_, _complib\=None_, _append\=False_, _format\=None_, _index\=True_, _min\_itemsize\=None_, _nan\_rep\=None_, _dropna\=<no\_default>_, _data\_columns\=None_, _errors\='strict'_, _encoding\='UTF-8'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L2644-L2821)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_hdf.html#pandas.Series.to_hdf "Link to this definition")

Write the contained data to an HDF5 file using HDFStore.

Hierarchical Data Format (HDF) is self-describing, allowing an application to interpret the structure and contents of a file with no outside information. One HDF file can hold a mix of related objects which can be accessed as a group or as individual objects.

In order to add another DataFrame or Series to an existing HDF file please use append mode and a different a key.

Note

Files produced by this method use a pandas-specific layout on top of PyTables and are intended to be read back with [`read_hdf()`](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#pandas.read_hdf "pandas.read_hdf")
 or `HDFStore`. They are valid HDF5 files but are not a general-purpose interchange format for arbitrary HDF5 consumers.

Warning

One can store a subclass of `DataFrame` or `Series` to HDF5, but the type of the subclass is lost upon storing.

For more information see the [user guide](https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5)
.

Parameters:

**path\_or\_buf**str or pandas.HDFStore

File path or HDFStore object.

**key**str

Identifier for the group in the store.

**mode**{‘a’, ‘w’, ‘r+’}, default ‘a’

Mode to open file:

*   ‘w’: write, a new file is created (an existing file with the same name would be deleted).
    
*   ‘a’: append, an existing file is opened for reading and writing, and if the file does not exist it is created.
    
*   ‘r+’: similar to ‘a’, but the file must already exist.
    

**complevel**{0-9}, default None

Specifies a compression level for data. A value of 0 or None disables compression.

**complib**{‘zlib’, ‘lzo’, ‘bzip2’, ‘blosc’}, default ‘zlib’

Specifies the compression library to be used. This has no effect unless `complevel` is set to a value greater than 0; passing `complib` alone emits a `UserWarning` and writes the data uncompressed. These additional compressors for Blosc are supported (default if no compressor specified: ‘blosc:blosclz’): {‘blosc:blosclz’, ‘blosc:lz4’, ‘blosc:lz4hc’, ‘blosc:snappy’, ‘blosc:zlib’, ‘blosc:zstd’}. Specifying a compression library which is not available issues a ValueError.

**append**bool, default False

For Table formats, append the input data to the existing table. The object stored at `key` (if any) must already be in `'table'` format; appending to a `'fixed'` object raises `ValueError`. When creating a new key with `append=True`, `format` defaults to `'table'`. Each append must use exactly the same columns, in the same order, as the existing table.

**format**{‘fixed’, ‘table’, None}, default ‘fixed’

Possible values:

*   ‘fixed’: Fixed format. Fast writing/reading. Not-appendable, nor searchable.
    
*   ‘table’: Table format. Write as a PyTables Table structure which may perform worse but allow more flexible operations like searching / selecting subsets of the data.
    
*   If None, pd.get\_option(‘io.hdf.default\_format’) is checked, followed by fallback to “fixed”.
    

**index**bool, default True

Write DataFrame index as a column.

**min\_itemsize**dict or int, optional

Map column names to minimum string sizes for columns.

**nan\_rep**str, optional

String used on disk to represent missing values in string columns (`format="table"` only). By default a sentinel that collides with no value in the column is used, so a literal `"nan"` round-trips unchanged; when this is passed, a value equal to it is read back as a missing value. Only used when the table is created; ignored on later appends, which reuse whatever the table already stores.

**dropna**bool, default False, optional

Remove missing values.

Deprecated since version 3.1.0: The `dropna` keyword is deprecated and will be removed in a future version. Use [`DataFrame.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")
 before writing instead.

**data\_columns**list of columns or True, optional

List of columns to create as indexed data columns for on-disk queries, or True to use all columns. By default only the axes of the object are indexed. See [Query via data columns](https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5-query-data-columns)
. for more information. Applicable only to format=’table’.

**errors**str, default ‘strict’

Specifies how encoding and decoding errors are to be handled. See the errors argument for [`open()`](https://docs.python.org/3/builtins/functions.html#open "(in Python v3.15)")
 for a full list of options.

**encoding**str, default “UTF-8”

Set character encoding.

See also

[`read_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#pandas.read_hdf "pandas.read_hdf")

Read from HDF file.

[`DataFrame.to_orc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#pandas.DataFrame.to_orc "pandas.DataFrame.to_orc")

Write a DataFrame to the binary orc format.

[`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")

Write a DataFrame to the binary parquet format.

[`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")

Write to a SQL table.

[`DataFrame.to_feather`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html#pandas.DataFrame.to_feather "pandas.DataFrame.to_feather")

Write out feather-format for DataFrames.

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write out to a csv file.

Examples

\>>> df \= pd.DataFrame(
...     {"A": \[1, 2, 3\], "B": \[4, 5, 6\]}, index\=\["a", "b", "c"\]
... )
\>>> df.to\_hdf("data.h5", key\="df", mode\="w")

Copy to clipboard

We can add another object to the same file:

\>>> s \= pd.Series(\[1, 2, 3, 4\])
\>>> s.to\_hdf("data.h5", key\="s")

Copy to clipboard

Reading from HDF file:

\>>> pd.read\_hdf("data.h5", "df")
A  B
a  1  4
b  2  5
c  3  6
\>>> pd.read\_hdf("data.h5", "s")
0    1
1    2
2    3
3    4
dtype: int64

Copy to clipboard

On this page