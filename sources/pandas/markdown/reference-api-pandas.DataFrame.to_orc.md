[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_orc.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_orc.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_orc.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_orc.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_orc.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_orc.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_orc.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_orc.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_orc.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_orc.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_orc.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_orc.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_orc[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#pandas-dataframe-to-orc "Link to this heading")

======================================================================================================================================================

DataFrame.to\_orc(_path\=None_, _\*_, _engine\='pyarrow'_, _index\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L3044-L3145)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#pandas.DataFrame.to_orc "Link to this definition")

Write a DataFrame to the Optimized Row Columnar (ORC) format.

ORC is a self-describing, type-aware columnar file format designed for Hadoop workloads. It provides efficient compression and encoding schemes, making it well-suited for large-scale data storage and analytics. This method requires the `pyarrow` library.

Parameters:

**path**str, file-like object or None, default None

If a string, it will be used as the root directory path when writing a partitioned dataset. By file-like object, we refer to objects with a write() method, such as a file handle (e.g. via builtin open function). If path is None, a bytes object is returned.

The string could be a URL. Valid URL schemes include http, ftp, s3, gs, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.orc`. A remote example could be: `s3://bucket/path/to/table.orc`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

**engine**{‘pyarrow’}, default ‘pyarrow’

ORC library to use.

**index**bool, optional

If `True`, include the dataframe’s index(es) in the file output. If `False`, they will not be written to the file. If `None`, similar to `infer` the dataframe’s index(es) will be saved. However, instead of being saved as values, the RangeIndex will be stored as a range in the metadata so it doesn’t require much space and is faster. Other indexes will be included as columns in the file output.

**engine\_kwargs**dict\[str, Any\] or None, default None

Additional keyword arguments passed to [`pyarrow.orc.write_table()`](https://arrow.apache.org/docs/python/generated/pyarrow.orc.write_table.html#pyarrow.orc.write_table "(in Apache Arrow v26.0.1)")
.

Returns:

bytes if no `path` argument is provided else None

Bytes object with DataFrame data if `path` is not specified else None.

Raises:

NotImplementedError

Dtype of one or more columns is category, unsigned integers, interval, period or sparse.

ValueError

engine is not pyarrow.

See also

[`read_orc`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")

Read a ORC file.

[`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")

Write a parquet file.

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write a csv file.

[`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")

Write to a sql table.

[`DataFrame.to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")

Write to hdf.

Notes

*   Find more information on ORC [here](https://en.wikipedia.org/wiki/Apache_ORC)
    .
    
*   Before using this function you should read the [user guide about ORC](https://pandas.pydata.org/docs/user_guide/io.html#io-orc)
     and [install optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-warn-orc)
    .
    
*   This function requires [pyarrow](https://arrow.apache.org/docs/python/)
     library.
    
*   For supported dtypes please refer to [supported ORC features in Arrow](https://arrow.apache.org/docs/cpp/orc.html#data-types)
    .
    
*   Currently timezones in datetime columns are not preserved when a dataframe is converted into ORC files.
    

Examples

\>>> df \= pd.DataFrame(data\={"col1": \[1, 2\], "col2": \[4, 3\]})
\>>> df.to\_orc("df.orc")
\>>> pd.read\_orc("df.orc")
   col1  col2
0     1     4
1     2     3

Copy to clipboard

If you want to get a buffer to the orc content you can write it to io.BytesIO

\>>> import io
\>>> b \= io.BytesIO(df.to\_orc())
\>>> b.seek(0)
0
\>>> content \= b.read()

Copy to clipboard

On this page