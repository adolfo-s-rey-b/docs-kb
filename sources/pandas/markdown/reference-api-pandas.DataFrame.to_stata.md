[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_stata[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html#pandas-dataframe-to-stata "Link to this heading")

============================================================================================================================================================

DataFrame.to\_stata(_path_, _\*_, _convert\_dates\=None_, _write\_index\=True_, _byteorder\=None_, _time\_stamp\=None_, _data\_label\=None_, _variable\_labels\=None_, _version\=114_, _convert\_strl\=None_, _compression\='infer'_, _storage\_options\=None_, _value\_labels\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L2507-L2673)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html#pandas.DataFrame.to_stata "Link to this definition")

Export DataFrame object to Stata dta format.

Writes the DataFrame to a Stata dataset file. “dta” files contain a Stata dataset.

Parameters:

**path**str, path object, or buffer

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `write()` function.

**convert\_dates**dict

Dictionary mapping columns containing datetime types to stata internal format to use when writing the dates. Options are ‘tc’, ‘td’, ‘tm’, ‘tw’, ‘th’, ‘tq’, ‘ty’. Column can be either an integer or a name. Datetime columns that do not have a conversion type specified will be converted to ‘tc’. Raises NotImplementedError if a datetime column has timezone information.

**write\_index**bool

Write the index to Stata dataset.

**byteorder**str

Can be “>”, “<”, “little”, or “big”. default is sys.byteorder.

**time\_stamp**datetime

A datetime to use as file creation date. Default is the current time.

**data\_label**str, optional

A label for the data set. Must be 80 characters or smaller.

**variable\_labels**dict

Dictionary containing columns as keys and variable labels as values. Each label must be 80 characters or smaller.

**version**{114, 117, 118, 119, None}, default 114

Version to use in the output dta file. Set to None to let pandas decide between 118 or 119 formats depending on the number of columns in the frame. Version 114 can be read by Stata 10 and later. Version 117 can be read by Stata 13 or later. Version 118 is supported in Stata 14 and later. Version 119 is supported in Stata 15 and later. Version 114 limits string variables to 244 characters or fewer while versions 117 and later allow strings with lengths up to 2,000,000 characters. Versions 118 and 119 support Unicode characters, and version 119 supports more than 32,767 variables.

Version 119 should usually only be used when the number of variables exceeds the capacity of dta format 118. Exporting smaller datasets in format 119 may have unintended consequences, and, as of November 2020, Stata SE cannot read version 119 files.

**convert\_strl**list, optional

List of column names to convert to string columns to Stata StrL format. Only available if version is 117. Storing strings in the StrL format can produce smaller dta files if strings have more than 8 characters and values are repeated.

**compression**str or dict, default ‘infer’

For on-the-fly compression of the output data. If ‘infer’ and ‘path’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). Set to `None` for no compression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdCompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for faster compression and to create a reproducible gzip archive: `compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}`.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**value\_labels**dict of dicts

Dictionary containing columns as keys and dictionaries of column value to labels as values. Labels for a single variable must be 32,000 characters or smaller.

Raises:

NotImplementedError

*   If datetimes contain timezone information
    
*   Column dtype is not representable in Stata
    

ValueError

*   Columns listed in convert\_dates are neither datetime64\[ns\] or datetime.datetime
    
*   Column listed in convert\_dates is not in DataFrame
    
*   Categorical label contains more than 32,000 characters
    

See also

[`read_stata`](https://pandas.pydata.org/docs/reference/api/pandas.read_stata.html#pandas.read_stata "pandas.read_stata")

Import Stata data files.

`io.stata.StataWriter`

Low-level writer for Stata data files.

`io.stata.StataWriter117`

Low-level writer for version 117 files.

Examples

\>>> df \= pd.DataFrame(
...     \[\["falcon", 350\], \["parrot", 18\]\], columns\=\["animal", "parrot"\]
... )
\>>> df.to\_stata("animals.dta")

Copy to clipboard

On this page