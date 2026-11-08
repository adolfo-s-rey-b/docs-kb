[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_sas[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#pandas-read-sas "Link to this heading")

==============================================================================================================================

pandas.read\_sas(_filepath\_or\_buffer_, _\*_, _format\=None_, _index\=None_, _encoding\=<no\_default>_, _chunksize\=None_, _iterator\=False_, _compression\='infer'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/sas/sasreader.py#L86-L214)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#pandas.read_sas "Link to this definition")

Read SAS files stored as either XPORT or SAS7BDAT format files.

The file format is inferred from the file extension if not explicitly specified. Supports both full reads and chunked iteration.

Parameters:

**filepath\_or\_buffer**str, path object, or file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `read()` function. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.sas7bdat`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

**format**str {‘xport’, ‘sas7bdat’} or None

If None, file format is inferred from file extension. If ‘xport’ or ‘sas7bdat’, uses the corresponding format.

**index**identifier of index column, defaults to None

Identifier of column that should be used as index of the DataFrame.

**encoding**str, ‘infer’ or None, default is None

Encoding for text data. If None, text data are stored as raw bytes. `'infer'` decodes SAS7BDAT files using the encoding recorded in the file header, falling back to latin-1 if the header does not name one pandas recognizes; XPORT files record no encoding, so `'infer'` means ISO-8859-1 there.

Deprecated since version 3.1.0: The default will change from `None` to `'infer'`, so text data will be decoded rather than returned as bytes. Pass `None` explicitly to keep the current behavior.

**chunksize**int

Read file chunksize lines at a time, returns iterator.

**iterator**bool, defaults to False

If True, returns an iterator for reading the file incrementally.

**compression**str or dict, default ‘infer’

For on-the-fly decompression of on-disk data. If ‘infer’ and ‘filepath\_or\_buffer’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). Set to `None` for no decompression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdCompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for faster compression and to create a reproducible gzip archive: `compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}`.

Returns:

DataFrame, SAS7BDATReader, or XportReader

DataFrame if iterator=False and chunksize=None, else SAS7BDATReader or XportReader, file format is inferred from file extension.

See also

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into a DataFrame.

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel file into a pandas DataFrame.

[`read_spss`](https://pandas.pydata.org/docs/reference/api/pandas.read_spss.html#pandas.read_spss "pandas.read_spss")

Read an SPSS file into a pandas DataFrame.

[`read_orc`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")

Load an ORC object into a pandas DataFrame.

[`read_feather`](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#pandas.read_feather "pandas.read_feather")

Load a feather-format object into a pandas DataFrame.

Examples

\>>> df \= pd.read\_sas("sas\_data.sas7bdat")

Copy to clipboard

On this page