[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_stata[#](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html#pandas-read-stata "Link to this heading")

====================================================================================================================================

pandas.read\_stata(_filepath\_or\_buffer_, _\*_, _convert\_dates\=True_, _convert\_categoricals\=True_, _index\_col\=None_, _convert\_missing\=False_, _preserve\_dtypes\=True_, _columns\=None_, _order\_categoricals\=True_, _chunksize\=None_, _iterator\=False_, _compression\='infer'_, _storage\_options\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/stata.py#L2150-L2305)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html#pandas.read_stata "Link to this definition")

Read Stata file into DataFrame.

This function reads `.dta` files produced by Stata, with support for converting date variables, categorical data, and missing value representations.

Parameters:

**filepath\_or\_buffer**str, path object or file-like object

Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.dta`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

If you want to pass in a path object, pandas accepts any `os.PathLike`.

By file-like object, we refer to objects with a `read()` method, such as a file handle (e.g. via builtin `open` function) or `StringIO`.

**convert\_dates**bool, default True

Convert date variables to DataFrame time values.

**convert\_categoricals**bool, default True

Read value labels and convert columns to Categorical/Factor variables.

**index\_col**str, optional

Column to set as index.

**convert\_missing**bool, default False

Flag indicating whether to convert missing values to their Stata representations. If False, missing values are replaced with nan. If True, columns containing missing values are returned with object data types and missing values are represented by StataMissingValue objects.

**preserve\_dtypes**bool, default True

Preserve Stata datatypes. If False, numeric data are upcast to pandas default types for foreign data (float64 or int64).

**columns**list or None

Columns to retain. Columns will be returned in the given order. None returns all columns.

**order\_categoricals**bool, default True

Flag indicating whether converted categorical data are ordered.

**chunksize**int, default None

Return StataReader object for iterations, returns chunks with given number of lines.

**iterator**bool, default False

Return StataReader object.

**compression**str or dict, default ‘infer’

For on-the-fly decompression of on-disk data. If ‘infer’ and ‘filepath\_or\_buffer’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). If using ‘zip’ or ‘tar’, the ZIP file must contain only one data file to be read in. Set to `None` for no decompression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdDecompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for Zstandard decompression using a custom compression dictionary: `compression={'method': 'zstd', 'dict_data': my_compression_dict}`.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

Returns:

DataFrame, pandas.api.typing.StataReader

If iterator or chunksize, returns StataReader, else DataFrame.

See also

`io.stata.StataReader`

Low-level reader for Stata data files.

[`DataFrame.to_stata`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html#pandas.DataFrame.to_stata "pandas.DataFrame.to_stata")

Export Stata data files.

Notes

Categorical variables read through an iterator may not have the same categories and dtype. This occurs when a variable stored in a DTA file is associated to an incomplete set of value labels that only label a strict subset of the values.

Examples

Creating a dummy stata for this example

\>>> df \= pd.DataFrame(
...     {
...         "animal": \["falcon", "parrot", "falcon", "parrot"\],
...         "speed": \[350, 18, 361, 15\],
...     }
... )
\>>> df.to\_stata("animals.dta")

Copy to clipboard

Read a Stata dta file:

\>>> df \= pd.read\_stata("animals.dta")

Copy to clipboard

Read a Stata dta file in 10,000 line chunks:

\>>> values \= np.random.randint(
...     0, 10, size\=(20\_000, 1), dtype\="uint8"
... )
\>>> df \= pd.DataFrame(values, columns\=\["i"\])
\>>> df.to\_stata("filename.dta")

Copy to clipboard

\>>> with pd.read\_stata('filename.dta', chunksize\=10000) as itr:
\>>>     for chunk in itr:
...         \# Operate on a single chunk, e.g., chunk.mean()
...         pass

Copy to clipboard

On this page