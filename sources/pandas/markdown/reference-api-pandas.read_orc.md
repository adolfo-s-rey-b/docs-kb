[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_orc[#](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas-read-orc "Link to this heading")

==============================================================================================================================

pandas.read\_orc(_path_, _columns\=None_, _dtype\_backend\=<no\_default>_, _filesystem\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/orc.py#L42-L145)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "Link to this definition")

Load an ORC object from the file path, returning a DataFrame.

This function requires the [pyarrow](https://arrow.apache.org/docs/python/)
 library.

ORC is a columnar storage format that provides efficient compression and fast retrieval for analytical workloads. It allows reading specific columns, handling different filesystem types (such as local storage, cloud storage via fsspec, or pyarrow filesystem), and supports different data type backends, including numpy\_nullable and pyarrow.

Parameters:

**path**str, path object, or file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `read()` function. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.orc`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

**columns**list, default None

If not None, only these columns will be read from the file. Output always follows the ordering of the file and not the columns list. This mirrors the original behaviour of [`pyarrow.orc.ORCFile.read()`](https://arrow.apache.org/docs/python/generated/pyarrow.orc.ORCFile.html#pyarrow.orc.ORCFile.read "(in Apache Arrow v26.0.1)")
.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**filesystem**fsspec or pyarrow filesystem, default None

Filesystem object to use when reading the orc file.

Added in version 2.1.0.

**\*\*kwargs**

Any additional kwargs are passed to pyarrow.

Returns:

DataFrame

DataFrame based on the ORC file.

See also

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into a pandas DataFrame.

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel file into a pandas DataFrame.

[`read_spss`](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html#pandas.read_spss "pandas.read_spss")

Read an SPSS file into a pandas DataFrame.

[`read_sas`](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#pandas.read_sas "pandas.read_sas")

Load a SAS file into a pandas DataFrame.

[`read_feather`](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#pandas.read_feather "pandas.read_feather")

Load a feather-format object into a pandas DataFrame.

Notes

Before using this function you should read the [user guide about ORC](https://pandas.pydata.org/docs/user_guide/io.html#io-orc)
 and [install optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-warn-orc)
.

If `path` is a URI scheme pointing to a local or remote file (e.g. “s3://”), a `pyarrow.fs` filesystem will be attempted to read the file. You can also pass a pyarrow or fsspec filesystem object into the filesystem keyword to override this behavior.

Examples

\>>> result \= pd.read\_orc("example\_pa.orc")

Copy to clipboard

On this page