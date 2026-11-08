[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_pickle.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_pickle.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_pickle.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_pickle.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_pickle.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_pickle.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_pickle.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_pickle.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_pickle.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_pickle.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_pickle.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_pickle.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_pickle[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#pandas-dataframe-to-pickle "Link to this heading")

===============================================================================================================================================================

DataFrame.to\_pickle(_path_, _\*_, _compression\='infer'_, _protocol\=5_, _storage\_options\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L3087-L3183)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#pandas.DataFrame.to_pickle "Link to this definition")

Pickle (serialize) object to file.

Uses Python’s `pickle` module to serialize the object and write it to the specified file path. The resulting file can be loaded back using [`pandas.read_pickle()`](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html#pandas.read_pickle "pandas.read_pickle")
.

Parameters:

**path**str, path object, or file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `write()` function. File path where the pickled object will be stored.

**compression**str or dict, default ‘infer’

For on-the-fly compression of the output data. If ‘infer’ and ‘path\_or\_buf’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). Set to `None` for no compression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdCompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for faster compression and to create a reproducible gzip archive: `compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}`.

**protocol**int

Int which indicates which protocol should be used by the pickler, default HIGHEST\_PROTOCOL (see [\[1\]](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#rc4e85fbd536b-1)
 paragraph 12.1.2). The possible values are 0, 1, 2, 3, 4, 5. A negative value for the protocol parameter is equivalent to setting its value to HIGHEST\_PROTOCOL.

\[[1](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#id1)\
\]

[https://docs.python.org/3/library/pickle.html](https://docs.python.org/3/library/pickle.html)
.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

See also

[`read_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html#pandas.read_pickle "pandas.read_pickle")

Load pickled pandas object (or any object) from file.

[`DataFrame.to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")

Write DataFrame to an HDF5 file.

[`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")

Write DataFrame to a SQL database.

[`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")

Write a DataFrame to the binary parquet format.

Examples

\>>> original\_df \= pd.DataFrame(
...     {"foo": range(5), "bar": range(5, 10)}
... )
\>>> original\_df
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9
\>>> original\_df.to\_pickle("./dummy.pkl")

Copy to clipboard

\>>> unpickled\_df \= pd.read\_pickle("./dummy.pkl")
\>>> unpickled\_df
   foo  bar
0    0    5
1    1    6
2    2    7
3    3    8
4    4    9

Copy to clipboard

On this page