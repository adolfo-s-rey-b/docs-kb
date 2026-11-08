[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_json.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_json.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_json.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_json.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_json.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_json.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_json.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_json.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_json.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_json.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_json.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_json.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_json[#](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas-read-json "Link to this heading")

=================================================================================================================================

pandas.read\_json(_path\_or\_buf_, _\*_, _orient\=None_, _typ\='frame'_, _dtype\=None_, _convert\_axes\=None_, _convert\_dates\=<no\_default>_, _keep\_default\_dates\=<no\_default>_, _precise\_float\=False_, _date\_unit\=None_, _encoding\=None_, _encoding\_errors\='strict'_, _lines\=False_, _chunksize\=None_, _compression\='infer'_, _nrows\=None_, _storage\_options\=None_, _dtype\_backend\=<no\_default>_, _engine\='ujson'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/json/_json.py#L635-L1017)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "Link to this definition")

Convert a JSON string to pandas object.

This method reads JSON files or JSON-like data and converts them into pandas objects. It supports a variety of input formats, including line-delimited JSON, compressed files, and various data representations (table, records, index-based, etc.). When chunksize is specified, an iterator is returned instead of loading the entire data into memory.

Parameters:

**path\_or\_buf**a str path, path object or file-like object

Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.json`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

If you want to pass in a path object, pandas accepts any `os.PathLike`.

By file-like object, we refer to objects with a `read()` method, such as a file handle (e.g. via builtin `open` function) or `StringIO`.

**orient**str, optional

Indication of expected JSON string format. Compatible JSON strings can be produced by `to_json()` with a corresponding orient value. When `typ == 'frame'`, the set of possible orients is:

*   `'split'` : dict like `{index -> [index], columns -> [columns], data -> [values]}`
    
*   `'records'` : list like `[{column -> value}, ... , {column -> value}]`
    
*   `'index'` : dict like `{index -> {column -> value}}`
    
*   `'columns'` : dict like `{column -> {index -> value}}`
    
*   `'values'` : just the values array
    
*   `'table'` : dict like `{'schema': {schema}, 'data': {data}}`
    

When `typ == 'series'`, the shapes differ, since a Series has no columns:

*   `'split'` : dict like `{name -> name, index -> [index], data -> [values]}`
    
*   `'records'` : list like `[value, ... , value]`
    
*   `'index'` : dict like `{index -> value}`
    

The allowed and default values depend on the value of the typ parameter.

*   when `typ == 'series'`,
    
    *   allowed orients are `{'split','records','index'}`
        
    *   default is `'index'`
        
    *   The Series index must be unique for orient `'index'`.
        
*   when `typ == 'frame'`,
    
    *   allowed orients are `{'split','records','index', 'columns','values', 'table'}`
        
    *   default is `'columns'`
        
    *   The DataFrame index must be unique for orients `'index'` and `'columns'`.
        
    *   The DataFrame columns must be unique for orients `'index'`, `'columns'`, and `'records'`.
        

**typ**{‘frame’, ‘series’}, default ‘frame’

The type of object to recover.

**dtype**bool or dict, default None

If True, infer dtypes; if a dict of column to dtype, then use those; if False, then don’t infer dtypes at all, applies only to the data.

For all `orient` values except `'table'`, default is True.

**convert\_axes**bool, default None

Try to convert the axes to the proper dtypes.

For all `orient` values except `'table'`, default is True.

**convert\_dates**bool or list of str, default True

If True then default datelike columns may be converted (depending on keep\_default\_dates). If False, no dates will be converted. If a list of column names, then those columns will be converted and default datelike columns may also be converted (depending on keep\_default\_dates).

Deprecated since version 3.1.0: Pass `dtype=False` to disable type conversion, or parse date columns with [`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
 after reading.

**keep\_default\_dates**bool, default True

If parsing dates (convert\_dates is not False), then try to parse the default datelike columns. A column label is datelike if

*   it ends with `'_at'`,
    
*   it ends with `'_time'`,
    
*   it begins with `'timestamp'`,
    
*   it is `'modified'`, or
    
*   it is `'date'`.
    

Deprecated since version 3.1.0: Pass `dtype=False` to disable type conversion, or parse date columns with [`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
 after reading.

**precise\_float**bool, default False

Set to enable usage of higher precision (strtod) function when decoding string to double values. Default (False) is to use fast but less precise builtin functionality.

**date\_unit**str, default None

The timestamp unit to detect if converting dates. The default behaviour is to try and detect the correct precision, but if this is not desired then pass one of ‘s’, ‘ms’, ‘us’ or ‘ns’ to force parsing only seconds, milliseconds, microseconds or nanoseconds respectively.

**encoding**str, default is ‘utf-8’

The encoding to use to decode py3 bytes.

**encoding\_errors**str, optional, default “strict”

How encoding errors are treated. [List of possible values](https://docs.python.org/3/library/codecs.html#error-handlers)
 .

**lines**bool, default False

Read the file as a json object per line.

**chunksize**int, optional

Return JsonReader object for iteration. See the [line-delimited json docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#line-delimited-json)
 for more information on `chunksize`. This can only be passed if lines=True. If this is None, the file will be read into memory all at once.

**compression**str or dict, default ‘infer’

For on-the-fly decompression of on-disk data. If ‘infer’ and ‘path\_or\_buf’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). If using ‘zip’ or ‘tar’, the ZIP file must contain only one data file to be read in. Set to `None` for no decompression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdDecompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for Zstandard decompression using a custom compression dictionary: `compression={'method': 'zstd', 'dict_data': my_compression_dict}`.

**nrows**int, optional

The number of lines from the line-delimited jsonfile that has to be read. This can only be passed if lines=True. If this is None, all the rows will be returned.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**engine**{“ujson”, “pyarrow”}, default “ujson”

Parser engine to use. The `"pyarrow"` engine is only available when `lines=True`, and only supports `typ="frame"` with default parsing options; passing an option it cannot apply (for example `convert_dates`, `date_unit`, `precise_float`, `encoding`, or a non-`ArrowDtype` `dtype`) raises `ValueError`.

Added in version 2.0.

Returns:

Series, DataFrame, or pandas.api.typing.JsonReader

A JsonReader is returned when `chunksize` is not `0` or `None`. Otherwise, the type returned depends on the value of `typ`.

See also

[`DataFrame.to_json`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json "pandas.DataFrame.to_json")

Convert a DataFrame to a JSON string.

[`Series.to_json`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html#pandas.Series.to_json "pandas.Series.to_json")

Convert a Series to a JSON string.

[`json_normalize`](https://pandas.pydata.org/docs/reference/api/pandas.json_normalize.html#pandas.json_normalize "pandas.json_normalize")

Normalize semi-structured JSON data into a flat table.

Notes

Specific to `orient='table'`, if a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 with a literal [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 name of index gets written with `to_json()`, the subsequent read operation will incorrectly set the [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 name to `None`. This is because index is also used by [`DataFrame.to_json()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json "pandas.DataFrame.to_json")
 to denote a missing [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 name, and the subsequent [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
 operation cannot distinguish between the two. The same limitation is encountered with a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
 and any names beginning with `'level_'`.

Examples

\>>> from io import StringIO
\>>> df \= pd.DataFrame(
...     \[\["a", "b"\], \["c", "d"\]\],
...     index\=\["row 1", "row 2"\],
...     columns\=\["col 1", "col 2"\],
... )

Copy to clipboard

Encoding/decoding a Dataframe using `'split'` formatted JSON:

\>>> df.to\_json(orient\="split")
'{"columns":\["col 1","col 2"\],"index":\["row 1","row 2"\],"data":\[\["a","b"\],\["c","d"\]\]}'

Copy to clipboard

\>>> pd.read\_json(StringIO(\_), orient\="split")  \# noqa: F821
      col 1 col 2
row 1     a     b
row 2     c     d

Copy to clipboard

Encoding/decoding a Dataframe using `'index'` formatted JSON:

\>>> df.to\_json(orient\="index")
'{"row 1":{"col 1":"a","col 2":"b"},"row 2":{"col 1":"c","col 2":"d"}}'

Copy to clipboard

\>>> pd.read\_json(StringIO(\_), orient\="index")  \# noqa: F821
      col 1 col 2
row 1     a     b
row 2     c     d

Copy to clipboard

Encoding/decoding a Dataframe using `'records'` formatted JSON. Note that index labels are not preserved with this encoding.

\>>> df.to\_json(orient\="records")
'\[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}\]'

Copy to clipboard

\>>> pd.read\_json(StringIO(\_), orient\="records")  \# noqa: F821
  col 1 col 2
0     a     b
1     c     d

Copy to clipboard

Encoding with Table Schema

\>>> df.to\_json(orient\="table")
'{"schema":{"fields":\[{"name":"index","type":"string","extDtype":"str"},{"name":"col 1","type":"string","extDtype":"str"},{"name":"col 2","type":"string","extDtype":"str"}\],"primaryKey":\["index"\],"pandas\_version":"1.4.0"},"data":\[{"index":"row 1","col 1":"a","col 2":"b"},{"index":"row 2","col 1":"c","col 2":"d"}\]}'

Copy to clipboard

The following example uses `dtype_backend="numpy_nullable"`

\>>> data \= '''{"index": {"0": 0, "1": 1},
...        "a": {"0": 1, "1": null},
...        "b": {"0": 2.5, "1": 4.5},
...        "c": {"0": true, "1": false},
...        "d": {"0": "a", "1": "b"},
...        "e": {"0": 1577.2, "1": 1577.1}}'''
\>>> pd.read\_json(StringIO(data), dtype\_backend\="numpy\_nullable")
   index     a    b      c  d       e
0      0     1  2.5   True  a  1577.2
1      1  <NA>  4.5  False  b  1577.1

Copy to clipboard

On this page