[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_parquet[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas-dataframe-to-parquet "Link to this heading")

==================================================================================================================================================================

DataFrame.to\_parquet(_path\=None_, _\*_, _engine\=<no\_default>_, _compression\='snappy'_, _index\=None_, _partition\_cols\=None_, _storage\_options\=None_, _filesystem\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L2870-L3012)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "Link to this definition")

Write a DataFrame to the binary parquet format.

This function writes the dataframe as a [parquet file](https://parquet.apache.org/)
. You can choose different parquet backends, and have the option of compression. See [the user guide](https://pandas.pydata.org/docs/user_guide/io.html#io-parquet)
 for more details.

Parameters:

**path**str, path object, file-like object, or None, default None

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `write()` function. If None, the result is returned as bytes. If a string or path, it will be used as the root directory path when writing a partitioned dataset.

The string could be a URL. Valid URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.parquet`. A remote example could be: `s3://bucket/path/to/table.parquet`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

**engine**{‘auto’, ‘pyarrow’, ‘fastparquet’}, default ‘auto’

Parquet library to use. If ‘auto’, then the option `io.parquet.engine` is used. The default `io.parquet.engine` behavior is to try ‘pyarrow’, falling back to ‘fastparquet’ if ‘pyarrow’ is unavailable.

Deprecated since version 3.1.0: The `'fastparquet'` and `'auto'` engine options are deprecated. Use `'pyarrow'` or do not pass `engine` to use the default.

**compression**str or None, default ‘snappy’

Name of the compression to use. Use `None` for no compression. Supported options: ‘snappy’, ‘gzip’, ‘brotli’, ‘lz4’, ‘zstd’.

**index**bool, default None

If `True`, include the dataframe’s index(es) in the file output. If `False`, they will not be written to the file. If `None`, similar to `True` the dataframe’s index(es) will be saved. However, instead of being saved as values, the RangeIndex will be stored as a range in the metadata so it doesn’t require much space and is faster. Other indexes will be included as columns in the file output.

**partition\_cols**list, optional, default None

Column names by which to partition the dataset. Columns are partitioned in the order they are given. Must be None if path is not a string.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**filesystem**fsspec or pyarrow filesystem, default None

Filesystem object to use when reading the parquet file. Only implemented for `engine="pyarrow"`.

Added in version 2.1.0.

**\*\*kwargs**

Additional arguments passed to the parquet library. See [pandas io](https://pandas.pydata.org/docs/user_guide/io.html#io-parquet)
 for more details.

Returns:

bytes if no path argument is provided else None

Returns the DataFrame converted to the binary parquet format as bytes if no path argument. Returns None and writes the DataFrame to the specified location in the Parquet format if the path argument is provided.

See also

[`read_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas.read_parquet "pandas.read_parquet")

Read a parquet file.

[`DataFrame.to_orc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#pandas.DataFrame.to_orc "pandas.DataFrame.to_orc")

Write an orc file.

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write a csv file.

[`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")

Write to a sql table.

[`DataFrame.to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")

Write to hdf.

Notes

*   This function requires either the [fastparquet](https://pypi.org/project/fastparquet)
     or [pyarrow](https://arrow.apache.org/docs/python/)
     library.
    
*   When saving a DataFrame with categorical columns to parquet, the file size may increase due to the inclusion of all possible categories, not just those present in the data. This behavior is expected and consistent with pandas’ handling of categorical data. To manage file size and ensure a more predictable roundtrip process, consider using [`Categorical.remove_unused_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_unused_categories.html#pandas.Categorical.remove_unused_categories "pandas.Categorical.remove_unused_categories")
     on the DataFrame before saving.
    

Examples

\>>> df \= pd.DataFrame(data\={"col1": \[1, 2\], "col2": \[3, 4\]})
\>>> df.to\_parquet("df.parquet.gzip", compression\="gzip")
\>>> pd.read\_parquet("df.parquet.gzip")
   col1  col2
0     1     3
1     2     4

Copy to clipboard

If you want to get a buffer to the parquet content you can use a io.BytesIO object, as long as you don’t use partition\_cols, which creates multiple files.

\>>> import io
\>>> f \= io.BytesIO()
\>>> df.to\_parquet(f)
\>>> f.seek(0)
0
\>>> content \= f.read()

Copy to clipboard

On this page