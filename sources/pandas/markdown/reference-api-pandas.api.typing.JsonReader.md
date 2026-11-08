[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.JsonReader.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.JsonReader[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.JsonReader.html#pandas-api-typing-jsonreader "Link to this heading")

====================================================================================================================================================================

class pandas.api.typing.JsonReader(_filepath\_or\_buffer_, _orient_, _typ_, _dtype_, _convert\_axes_, _convert\_dates_, _keep\_default\_dates_, _precise\_float_, _date\_unit_, _encoding_, _lines_, _chunksize_, _compression_, _nrows_, _storage\_options\=None_, _encoding\_errors\='strict'_, _dtype\_backend\=<no\_default>_, _engine\='ujson'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/json/_json.py#L1020-L1437)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.JsonReader.html#pandas.api.typing.JsonReader "Link to this definition")

JsonReader provides an interface for reading in a JSON file.

If initialized with `lines=True` and `chunksize`, can be iterated over `chunksize` lines at a time. Otherwise, calling `read` reads in the whole document.

A `JsonReader` is returned by [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 when `chunksize` is passed; it is not usually instantiated directly.

Parameters:

**filepath\_or\_buffer**a str path, path object or file-like object

Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. pandas accepts any `os.PathLike`, or file-like object with a `read()` method, such as a file handle or `StringIO`.

**orient**str

Indication of expected JSON string format. Compatible JSON strings can be produced by `to_json()` with a corresponding orient value. See [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 for the set of possible orients.

**typ**{“frame”, “series”}

The type of object to recover.

**dtype**bool or dict

If True, infer dtypes; if a dict of column to dtype, then use those; if False, then don’t infer dtypes at all, applies only to the data.

**convert\_axes**bool or None

Try to convert the axes to the proper dtypes.

**convert\_dates**bool or list of str

If True then default datelike columns may be converted (depending on `keep_default_dates`). If False, no dates will be converted. If a list of column names, then those columns will be converted and default datelike columns may also be converted (depending on `keep_default_dates`).

**keep\_default\_dates**bool

If parsing dates (`convert_dates` is not False), then try to parse the default datelike columns. See [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 for the criteria used to determine whether a column label is datelike.

**precise\_float**bool

Set to enable usage of higher precision (strtod) function when decoding string to double values.

**date\_unit**str or None

The timestamp unit to detect if converting dates. The default behaviour is to try and detect the correct precision, but if this is not desired then pass one of ‘s’, ‘ms’, ‘us’ or ‘ns’ to force parsing only seconds, milliseconds, microseconds or nanoseconds respectively.

**encoding**str or None

The encoding to use to decode py3 bytes.

**lines**bool

Read the file as a json object per line.

**chunksize**int or None

Return a `JsonReader` for iteration, yielding `chunksize` lines at a time. Can only be passed if `lines=True`. If this is None, the file will be read into memory all at once.

**compression**str or dict

For on-the-fly decompression of on-disk data, see [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 for the accepted values.

**nrows**int or None

The number of lines from the line-delimited json file that has to be read. Can only be passed if `lines=True`. If this is None, all the rows will be returned.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. See [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 for more details.

**encoding\_errors**str, optional, default “strict”

How encoding errors are treated. [List of possible values](https://docs.python.org/3/library/codecs.html#error-handlers)
 .

**dtype\_backend**{“numpy\_nullable”, “pyarrow”}

Back-end data type applied to the resultant `DataFrame` (still experimental). See [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 for more details.

**engine**{“ujson”, “pyarrow”}, default “ujson”

Parser engine to use. See [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 for the restrictions on the `"pyarrow"` engine.

See also

`read_json`

Convert a JSON string to pandas object.

Examples

\>>> from io import StringIO
\>>> df \= pd.DataFrame({"a": \[1, 2\], "b": \[3, 4\]})
\>>> reader \= pd.read\_json(
...     StringIO(df.to\_json(orient\="records", lines\=True)),
...     lines\=True,
...     chunksize\=1,
... )
\>>> for chunk in reader:
...     print(chunk)
   a  b
0  1  3
   a  b
1  2  4

Copy to clipboard

Methods

|     |     |
| --- | --- |
| `close`() | Close the underlying file handle, if one was opened by the reader. |
| `read`() | Read the whole JSON input into a pandas object. |

On this page