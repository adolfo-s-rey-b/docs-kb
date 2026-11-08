[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_feather.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_feather.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_feather.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_feather.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_feather.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_feather.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_feather.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_feather.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_feather.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_feather.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_feather.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_feather.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_feather[#](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#pandas-read-feather "Link to this heading")

==========================================================================================================================================

pandas.read\_feather(_path_, _columns\=None_, _use\_threads\=True_, _storage\_options\=None_, _dtype\_backend\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/feather_format.py#L85-L183)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#pandas.read_feather "Link to this definition")

Load a feather-format object from the file path.

This function requires the [pyarrow](https://arrow.apache.org/docs/python/)
 library.

Feather is particularly useful for scenarios that require efficient serialization and deserialization of tabular data. It supports schema preservation, making it a reliable choice for use cases such as sharing data between Python and R, or persisting intermediate results during data processing pipelines. This method provides additional flexibility with options for selective column reading, thread parallelism, and choosing the backend for data types.

Parameters:

**path**str, path object, or file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `read()` function. The string could be a URL. Valid URL schemes include http, ftp, s3, gs and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.feather`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

**columns**sequence, default None

If not provided, all columns are read.

**use\_threads**bool, default True

Whether to parallelize reading using multiple threads.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    .
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

Returns:

type of object stored in file

DataFrame object stored in the file.

See also

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into a pandas DataFrame.

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel file into a pandas DataFrame.

[`read_spss`](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html#pandas.read_spss "pandas.read_spss")

Read an SPSS file into a pandas DataFrame.

[`read_orc`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")

Load an ORC object into a pandas DataFrame.

[`read_sas`](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#pandas.read_sas "pandas.read_sas")

Read SAS file into a pandas DataFrame.

Examples

\>>> df \= pd.read\_feather("path/to/file.feather")

Copy to clipboard

On this page