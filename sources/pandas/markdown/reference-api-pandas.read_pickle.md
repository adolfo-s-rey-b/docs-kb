[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_pickle[#](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html#pandas-read-pickle "Link to this heading")

=======================================================================================================================================

pandas.read\_pickle(_filepath\_or\_buffer_, _compression\='infer'_, _storage\_options\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pickle.py#L131-L254)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_pickle.html#pandas.read_pickle "Link to this definition")

Load pickled pandas object (or any object) from file and return unpickled object.

Warning

Loading pickled data received from untrusted sources can be unsafe. See [here](https://docs.python.org/3/library/pickle.html)
.

Parameters:

**filepath\_or\_buffer**str, path object, or file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `read()` function. Also accepts URL. URL is not limited to S3 and GCS.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

**compression**str or dict, default ‘infer’

For on-the-fly decompression of on-disk data. If ‘infer’ and ‘filepath\_or\_buffer’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). If using ‘zip’ or ‘tar’, the ZIP file must contain only one data file to be read in. Set to `None` for no decompression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdDecompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for Zstandard decompression using a custom compression dictionary: `compression={'method': 'zstd', 'dict_data': my_compression_dict}`.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

Returns:

object

The unpickled pandas object (or any object) that was stored in file.

See also

[`DataFrame.to_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#pandas.DataFrame.to_pickle "pandas.DataFrame.to_pickle")

Pickle (serialize) DataFrame object to file.

[`Series.to_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_pickle.html#pandas.Series.to_pickle "pandas.Series.to_pickle")

Pickle (serialize) Series object to file.

[`read_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.read_hdf.html#pandas.read_hdf "pandas.read_hdf")

Read HDF5 file into a DataFrame.

[`read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas.read_sql "pandas.read_sql")

Read SQL query or database table into a DataFrame.

[`read_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas.read_parquet "pandas.read_parquet")

Load a parquet object, returning a DataFrame.

Notes

read\_pickle is only guaranteed to be backwards compatible with pickles created by the current or previous major version of pandas, provided the object was serialized with to\_pickle. For example, in pandas 3.x.y, the earliest supported pickle would be from 2.0.0.

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
\>>> pd.to\_pickle(original\_df, "./dummy.pkl")

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