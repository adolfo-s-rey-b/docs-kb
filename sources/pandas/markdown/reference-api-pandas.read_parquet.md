[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_parquet.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_parquet.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_parquet.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_parquet.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_parquet.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_parquet.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_parquet.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_parquet.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_parquet.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_parquet.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_parquet.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_parquet.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_parquet[#](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas-read-parquet "Link to this heading")

==========================================================================================================================================

pandas.read\_parquet(_path_, _engine\=<no\_default>_, _columns\=None_, _storage\_options\=None_, _dtype\_backend\=<no\_default>_, _filesystem\=None_, _filters\=None_, _to\_pandas\_kwargs\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/parquet.py#L573-L769)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas.read_parquet "Link to this definition")

Load a parquet object from the file path, returning a DataFrame.

This function requires the [pyarrow](https://arrow.apache.org/docs/python/)
 library.

The function automatically handles reading the data from a parquet file and creates a DataFrame with the appropriate structure.

Parameters:

**path**str, path object or file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `read()` function. The string could be a URL. Valid URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.parquet`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

A file URL can also be a path to a directory that contains multiple partitioned parquet files. Both pyarrow and fastparquet support paths to directories as well as file URLs. A directory path could be: `file://localhost/path/to/tables` or `s3://bucket/partition_dir`.

**engine**{‘auto’, ‘pyarrow’, ‘fastparquet’}, default ‘auto’

Parquet library to use. If ‘auto’, then the option `io.parquet.engine` is used. The default `io.parquet.engine` behavior is to try ‘pyarrow’, falling back to ‘fastparquet’ if ‘pyarrow’ is unavailable.

When using the `'pyarrow'` engine and no storage options are provided and a filesystem is implemented by both `pyarrow.fs` and `fsspec` (e.g. “s3://”), then the `pyarrow.fs` filesystem is attempted first. Use the filesystem keyword with an instantiated fsspec filesystem if you wish to use its implementation.

Deprecated since version 3.1.0: The `'fastparquet'` and `'auto'` engine options are deprecated. Use `'pyarrow'` or do not pass `engine` to use the default.

**columns**list, default=None

If not None, only these columns will be read from the file.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**filesystem**fsspec or pyarrow filesystem, default None

Filesystem object to use when reading the parquet file. Only implemented for `engine="pyarrow"`.

Added in version 2.1.0.

**filters**List\[Tuple\] or List\[List\[Tuple\]\], default None

To filter out data. Filter syntax: \[\[(column, op, val), …\],…\] where op is \[==, =, >, >=, <, <=, !=, in, not in\] The innermost tuples are transposed into a set of filters applied through an AND operation. The outer list combines these sets of filters through an OR operation. A single list of tuples can also be used, meaning that no OR operation between set of filters is to be conducted.

Using this argument will NOT result in row-wise filtering of the final partitions unless `engine="pyarrow"` is also specified. For other engines, filtering is only performed at the partition level, that is, to prevent the loading of some row-groups and/or files.

Added in version 2.1.0.

**to\_pandas\_kwargs**dict | None, default None

Keyword arguments to pass through to `pyarrow.Table.to_pandas()` when `engine="pyarrow"`.

Added in version 3.0.0.

**\*\*kwargs**

Additional keyword arguments passed to the engine:

*   For `engine="pyarrow"`: passed to [`pyarrow.parquet.read_table()`](https://arrow.apache.org/docs/python/generated/pyarrow.parquet.read_table.html#pyarrow.parquet.read_table "(in Apache Arrow v26.0.1)")
    
*   For `engine="fastparquet"`: passed to `fastparquet.ParquetFile.to_pandas()`
    

Returns:

DataFrame

DataFrame based on parquet file.

See also

[`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")

Create a parquet object that serializes a DataFrame.

Examples

\>>> original\_df \= pd.DataFrame({"foo": range(5), "bar": range(5, 10)})
\>>> original\_df
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9
\>>> df\_parquet\_bytes \= original\_df.to\_parquet()
\>>> from io import BytesIO
\>>> restored\_df \= pd.read\_parquet(BytesIO(df\_parquet\_bytes))
\>>> restored\_df
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9
\>>> restored\_df.equals(original\_df)
True
\>>> restored\_bar \= pd.read\_parquet(BytesIO(df\_parquet\_bytes), columns\=\["bar"\])
\>>> restored\_bar
    bar
0    5
1    6
2    7
3    8
4    9
\>>> restored\_bar.equals(original\_df\[\["bar"\]\])
True

Copy to clipboard

The function uses kwargs that are passed directly to the engine. In the following example, we use the filters argument of the pyarrow engine to filter the rows of the DataFrame.

Since pyarrow is the default engine, we can omit the engine argument. Note that the filters argument is implemented by the pyarrow engine, which can benefit from multithreading and also potentially be more economical in terms of memory.

\>>> sel \= \[("foo", ">", 2)\]
\>>> restored\_part \= pd.read\_parquet(BytesIO(df\_parquet\_bytes), filters\=sel)
\>>> restored\_part
    foo  bar
0    3    8
1    4    9

Copy to clipboard

On this page