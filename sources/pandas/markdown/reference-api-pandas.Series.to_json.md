[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_json.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_json.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_json.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_json.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_json.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_json.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_json.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_json.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_json.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_json.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_json.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_json.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_json[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html#pandas-series-to-json "Link to this heading")

================================================================================================================================================

Series.to\_json(_path\_or\_buf\=None_, _\*_, _orient\=None_, _date\_format\=None_, _double\_precision\=10_, _force\_ascii\=True_, _date\_unit\='ms'_, _default\_handler\=None_, _lines\=False_, _compression\='infer'_, _index\=None_, _indent\=None_, _storage\_options\=None_, _mode\='w'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L2279-L2642)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html#pandas.Series.to_json "Link to this definition")

Convert the object to a JSON string.

Note NaN’s and None will be converted to null and datetime objects will be converted to UNIX timestamps.

Parameters:

**path\_or\_buf**str, path object, file-like object, or None, default None

String, path object (implementing os.PathLike\[str\]), or file-like object implementing a write() function. If None, the result is returned as a string.

**orient**str

Indication of expected JSON string format.

*   Series:
    
    > *   default is ‘index’
    >     
    > *   allowed values are: {‘split’, ‘records’, ‘index’, ‘table’}.
    >     
    > *   the format of the JSON string:
    >     
    >     *   ‘split’ : dict like {‘name’ -> name, ‘index’ -> \[index\], ‘data’ -> \[values\]}
    >         
    >     *   ‘records’ : list like \[value, … , value\]; the index labels and the Series name are not included
    >         
    >     *   ‘index’ : dict like {index -> value}
    >         
    >     *   ‘table’ : dict like {‘schema’: {schema}, ‘data’: {data}}
    >         
    
*   DataFrame:
    
    > *   default is ‘columns’
    >     
    > *   allowed values are: {‘split’, ‘records’, ‘index’, ‘columns’, ‘values’, ‘table’}.
    >     
    > *   the format of the JSON string:
    >     
    >     *   ‘split’ : dict like {‘index’ -> \[index\], ‘columns’ -> \[columns\], ‘data’ -> \[values\]}
    >         
    >     *   ‘records’ : list like \[{column -> value}, … , {column -> value}\]
    >         
    >     *   ‘index’ : dict like {index -> {column -> value}}
    >         
    >     *   ‘columns’ : dict like {column -> {index -> value}}
    >         
    >     *   ‘values’ : just the values array
    >         
    >     *   ‘table’ : dict like {‘schema’: {schema}, ‘data’: {data}}
    >         
    

For `orient='table'`, the data component is like `orient='records'`.

**date\_format**{None, ‘epoch’, ‘iso’}

Type of date conversion. ‘epoch’ = epoch milliseconds, ‘iso’ = ISO8601. The default depends on the orient. For `orient='table'`, the default is ‘iso’. For all other orients, the default is ‘epoch’.

Deprecated since version 3.0.0: ‘epoch’ date format is deprecated and will be removed in a future version, please use ‘iso’ instead.

**double\_precision**int, default 10

The number of decimal places to use when encoding floating point values. The possible maximal value is 15. Passing double\_precision greater than 15 will raise a ValueError.

**force\_ascii**bool, default True

Force encoded string to be ASCII.

**date\_unit**str, default ‘ms’ (milliseconds)

The time unit to encode to, governs timestamp and ISO8601 precision. One of ‘s’, ‘ms’, ‘us’, ‘ns’ for second, millisecond, microsecond, and nanosecond respectively.

**default\_handler**callable, default None

Handler to call if object cannot otherwise be converted to a suitable format for JSON. Should receive a single argument which is the object to convert and return a serialisable object.

**lines**bool, default False

If ‘orient’ is ‘records’ write out line-delimited json format. Will throw ValueError if incorrect ‘orient’ since others are not list-like.

**compression**str or dict, default ‘infer’

For on-the-fly compression of the output data. If ‘infer’ and ‘path\_or\_buf’ is path-like, then detect compression from the following extensions: ‘.gz’, ‘.bz2’, ‘.zip’, ‘.xz’, ‘.zst’, ‘.tar’, ‘.tar.gz’, ‘.tar.xz’ or ‘.tar.bz2’ (otherwise no compression). Set to `None` for no compression. Can also be a dict with key `'method'` set to one of {`'zip'`, `'gzip'`, `'bz2'`, `'zstd'`, `'xz'`, `'tar'`} and other key-value pairs are forwarded to `zipfile.ZipFile`, `gzip.GzipFile`, `bz2.BZ2File`, `zstandard.ZstdCompressor`, `lzma.LZMAFile` or `tarfile.TarFile`, respectively. As an example, the following could be passed for faster compression and to create a reproducible gzip archive: `compression={'method': 'gzip', 'compresslevel': 1, 'mtime': 1}`.

**index**bool or None, default None

The index is only used when ‘orient’ is ‘split’, ‘index’, ‘column’, or ‘table’. Of these, ‘index’ and ‘column’ do not support index=False. The string ‘index’ as a column name with empty [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 or if it is ‘index’ will raise a `ValueError`.

**indent**int, optional

Length of whitespace used to indent each record.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**mode**str, default ‘w’ (writing)

Specify the IO mode for output when supplying a path\_or\_buf. Accepted args are ‘w’ (writing) and ‘a’ (append) only. mode=’a’ is only supported when lines is True and orient is ‘records’.

Returns:

None or str

If path\_or\_buf is None, returns the resulting json format as a string. Otherwise returns None.

See also

[`read_json`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")

Convert a JSON string to pandas object.

Notes

The behavior of `indent=0` varies from the stdlib, which does not indent the output but does insert newlines. Currently, `indent=0` and the default `indent=None` are equivalent in pandas, though this may change in a future release.

`orient='table'` contains a ‘pandas\_version’ field under ‘schema’. This stores the version of pandas used in the latest revision of the schema.

Examples

\>>> from json import loads, dumps
\>>> df \= pd.DataFrame(
...     \[\["a", "b"\], \["c", "d"\]\],
...     index\=\["row 1", "row 2"\],
...     columns\=\["col 1", "col 2"\],
... )

Copy to clipboard

\>>> result \= df.to\_json(orient\="split")
\>>> parsed \= loads(result)
\>>> dumps(parsed, indent\=4)
{
    "columns": \[\
        "col 1",\
        "col 2"\
    \],
    "index": \[\
        "row 1",\
        "row 2"\
    \],
    "data": \[\
        \[\
            "a",\
            "b"\
        \],\
        \[\
            "c",\
            "d"\
        \]\
    \]
}

Copy to clipboard

Encoding/decoding a Dataframe using `'records'` formatted JSON. Note that index labels are not preserved with this encoding.

\>>> result \= df.to\_json(orient\="records")
\>>> parsed \= loads(result)
\>>> dumps(parsed, indent\=4)
\[\
    {\
        "col 1": "a",\
        "col 2": "b"\
    },\
    {\
        "col 1": "c",\
        "col 2": "d"\
    }\
\]

Copy to clipboard

A Series with `orient="records"` is encoded as a JSON array of its values only, without the index labels; with `lines=True`, each value is written on its own line:

\>>> ser \= pd.Series(\[1, 2, 3\])
\>>> ser.to\_json(orient\="records")
'\[1,2,3\]'
\>>> ser.to\_json(orient\="records", lines\=True)
'1\\n2\\n3\\n'

Copy to clipboard

For a Series, the default `orient="index"` maps index labels to values, and `orient="split"` has a ‘name’ entry in place of a DataFrame’s ‘columns’:

\>>> ser.to\_json()
'{"0":1,"1":2,"2":3}'
\>>> ser.to\_json(orient\="split")
'{"name":null,"index":\[0,1,2\],"data":\[1,2,3\]}'

Copy to clipboard

Encoding/decoding a Dataframe using `'index'` formatted JSON:

\>>> result \= df.to\_json(orient\="index")
\>>> parsed \= loads(result)
\>>> dumps(parsed, indent\=4)
{
    "row 1": {
        "col 1": "a",
        "col 2": "b"
    },
    "row 2": {
        "col 1": "c",
        "col 2": "d"
    }
}

Copy to clipboard

Encoding/decoding a Dataframe using `'columns'` formatted JSON:

\>>> result \= df.to\_json(orient\="columns")
\>>> parsed \= loads(result)
\>>> dumps(parsed, indent\=4)
{
    "col 1": {
        "row 1": "a",
        "row 2": "c"
    },
    "col 2": {
        "row 1": "b",
        "row 2": "d"
    }
}

Copy to clipboard

Encoding/decoding a Dataframe using `'values'` formatted JSON:

\>>> result \= df.to\_json(orient\="values")
\>>> parsed \= loads(result)
\>>> dumps(parsed, indent\=4)
\[\
    \[\
        "a",\
        "b"\
    \],\
    \[\
        "c",\
        "d"\
    \]\
\]

Copy to clipboard

Encoding with Table Schema:

\>>> result \= df.to\_json(orient\="table")
\>>> parsed \= loads(result)
\>>> dumps(parsed, indent\=4)
{
    "schema": {
        "fields": \[\
            {\
                "name": "index",\
                "type": "string"\
            },\
            {\
                "name": "col 1",\
                "type": "string"\
            },\
            {\
                "name": "col 2",\
                "type": "string"\
            }\
        \],
        "primaryKey": \[\
            "index"\
        \],
        "pandas\_version": "1.4.0"
    },
    "data": \[\
        {\
            "index": "row 1",\
            "col 1": "a",\
            "col 2": "b"\
        },\
        {\
            "index": "row 2",\
            "col 1": "c",\
            "col 2": "d"\
        }\
    \]
}

Copy to clipboard

On this page