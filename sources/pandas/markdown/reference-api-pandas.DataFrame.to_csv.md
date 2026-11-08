[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_csv.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_csv.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_csv.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_csv.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_csv.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_csv.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_csv.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_csv.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_csv.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_csv.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_csv.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_csv.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_csv[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas-dataframe-to-csv "Link to this heading")

======================================================================================================================================================

DataFrame.to\_csv(_path\_or\_buf\=None_, _\*_, _sep\=','_, _na\_rep\=''_, _float\_format\=None_, _columns\=None_, _header\=True_, _index\=True_, _index\_label\=None_, _mode\='w'_, _encoding\=None_, _compression\='infer'_, _quoting\=None_, _quotechar\='"'_, _lineterminator\=None_, _chunksize\=None_, _date\_format\=None_, _doublequote\=True_, _escapechar\=None_, _decimal\='.'_, _errors\='strict'_, _storage\_options\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L3828-L4043)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "Link to this definition")

Write object to a comma-separated values (csv) file.

By default, the resulting file includes row index and column headers. Supports customization of delimiter, encoding, compression, and more. The output can be written to a file path, file-like buffer, or returned as a string.

Parameters:

**path\_or\_buf**str, path object, file-like object, or None, default None

String, path object (implementing os.PathLike\[str\]), or file-like object implementing a write() function. If None, the result is returned as a string. If a non-binary file object is passed, it should be opened with newline=’’, disabling universal newlines. If a binary file object is passed, mode might need to contain a ‘b’.

**sep**str, default ‘,’

String of length 1. Field delimiter for the output file.

**na\_rep**str, default ‘’

Missing data representation.

**float\_format**str, Callable, default None

Format string for floating point numbers. If a Callable is given, it takes precedence over other numeric formatting parameters, like decimal.

**columns**sequence, optional

Columns to write.

**header**bool or list of str, default True

Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.

**index**bool, default True

Write row names (index).

**index\_label**str or sequence, or False, default None

Column label for index column(s) if desired. If None is given, and header and index are True, then the index names are used. A sequence should be given if the object uses MultiIndex. If False do not print fields for index names. Use index\_label=False for easier importing in R.

**mode**{‘w’, ‘x’, ‘a’}, default ‘w’

Forwarded to either open(mode=) or fsspec.open(mode=) to control the file opening. Typical values include:

*   ‘w’, truncate the file first.
    
*   ‘x’, exclusive creation, failing if the file already exists.
    
*   ‘a’, append to the end of file if it exists.
    

**encoding**str, optional

A string representing the encoding to use in the output file, defaults to ‘utf-8’. encoding is not supported if path\_or\_buf is a non-binary file object.

**compression**str or dict, default ‘infer’

For on-the-fly compression of the output data. If ‘infer’ and ‘path\_or\_buf’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). Set to `None` for no compression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdCompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for faster compression and to create a reproducible gzip archive: `compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}`.

> May be a dict with key ‘method’ as compression mode and other entries as additional compression options if compression mode is ‘zip’.
> 
> Passing compression options as keys in dict is supported for compression modes ‘gzip’, ‘bz2’, ‘zstd’, and ‘zip’.

**quoting**optional constant from csv module

Defaults to csv.QUOTE\_MINIMAL. If you have set a float\_format then floats are converted to strings and thus csv.QUOTE\_NONNUMERIC will treat them as non-numeric.

**quotechar**str, default ‘"’

String of length 1. Character used to quote fields.

**lineterminator**str, optional

The newline character or character sequence to use in the output file. Defaults to os.linesep, which depends on the OS in which this method is called (’\\n’ for linux, ‘\\r\\n’ for Windows, i.e.).

**chunksize**int or None

Rows to write at a time.

**date\_format**str, default None

Format string for datetime objects.

**doublequote**bool, default True

Control quoting of quotechar inside a field.

**escapechar**str, default None

String of length 1. Character used to escape sep and quotechar when appropriate.

**decimal**str, default ‘.’

Character recognized as decimal separator. E.g. use ‘,’ for European data.

**errors**str, default ‘strict’

Specifies how encoding and decoding errors are to be handled. See the errors argument for [`open()`](https://docs.python.org/3/builtins/functions.html#open "(in Python v3.15)")
 for a full list of options.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

Returns:

None or str

If path\_or\_buf is None, returns the resulting csv format as a string. Otherwise returns None.

See also

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Load a CSV file into a DataFrame.

[`to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")

Write DataFrame to an Excel file.

Examples

Create ‘out.csv’ containing ‘df’ without indices

\>>> df \= pd.DataFrame(
...     \[\["Raphael", "red", "sai"\], \["Donatello", "purple", "bo staff"\]\],
...     columns\=\["name", "mask", "weapon"\],
... )
\>>> df.to\_csv("out.csv", index\=False)

Copy to clipboard

Create ‘out.zip’ containing ‘out.csv’

\>>> df.to\_csv(index\=False)
'name,mask,weapon\\nRaphael,red,sai\\nDonatello,purple,bo staff\\n'
\>>> compression\_opts \= dict(
...     method\="zip", archive\_name\="out.csv"
... )
\>>> df.to\_csv(
...     "out.zip", index\=False, compression\=compression\_opts
... )

Copy to clipboard

To write a csv file to a new folder or nested folder you will first need to create it using either Pathlib or os:

\>>> from pathlib import Path
\>>> filepath \= Path("folder/subfolder/out.csv")
\>>> filepath.parent.mkdir(parents\=True, exist\_ok\=True)
\>>> df.to\_csv(filepath)

Copy to clipboard

\>>> import os
\>>> os.makedirs("folder/subfolder", exist\_ok\=True)
\>>> df.to\_csv("folder/subfolder/out.csv")

Copy to clipboard

Format floats to two decimal places:

\>>> df.to\_csv("out1.csv", float\_format\="%.2f")

Copy to clipboard

Format floats using scientific notation:

\>>> df.to\_csv("out2.csv", float\_format\="{:.2e}".format)

Copy to clipboard

On this page