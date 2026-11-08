[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.put.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.put[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.put.html#pandas-hdfstore-put "Link to this heading")

=========================================================================================================================================

HDFStore.put(_key_, _value_, _format\=None_, _index\=True_, _append\=False_, _complib\=None_, _complevel\=None_, _min\_itemsize\=None_, _nan\_rep\=None_, _data\_columns\=None_, _encoding\=None_, _errors\='strict'_, _track\_times\=<no\_default>_, _dropna\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1343-L1493)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.put.html#pandas.HDFStore.put "Link to this definition")

Store object in HDFStore.

This method writes a pandas DataFrame or Series into an HDF5 file using either the fixed or table format. The table format allows additional operations like incremental appends and queries but may have performance trade-offs. The fixed format provides faster read/write operations but does not support appends or queries.

Parameters:

**key**str

Key of object to store in file.

**value**{Series, DataFrame}

Value of object to store in file.

**format**‘fixed(f)|table(t)’, default is ‘fixed’

Format to use when storing object in HDFStore. Value can be one of:

`'fixed'`

Fixed format. Fast writing/reading. Not-appendable, nor searchable.

`'table'`

Table format. Write as a PyTables Table structure which may perform worse but allow more flexible operations like searching / selecting subsets of the data.

**index**bool, default True

Write DataFrame index as a column.

**append**bool, default False

This will force Table format, append the input data to the existing.

**complib**{‘zlib’, ‘lzo’, ‘bzip2’, ‘blosc’}, default None

Compression library to use, only applied with `format='table'`. None disables compression. See the `complib` parameter of `HDFStore` for the full list of supported compressors.

**complevel**int, 0-9, default None

Specifies a compression level for data. A value of 0 or None disables compression.

**min\_itemsize**int, dict, or None

Minimum number of bytes reserved for object columns. If int, all columns reserve ‘min\_itemsize’ bytes per stored value. If dict, specific columns reserve ‘min\_itemsize’ bytes per stored value. Strings are stored as encoded bytes. Since some characters require multiple bytes, required size may be larger than string length.

**nan\_rep**str, optional

String used on disk to represent missing values in string columns (`format="table"` only). By default a sentinel that collides with no value in the column is used, so a literal `"nan"` round-trips unchanged; when this is passed, a value equal to it is read back as a missing value.

**data\_columns**list of columns or True, default None

List of columns to create as data columns, or True to use all columns. See [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#query-via-data-columns)
.

**encoding**str, default None

Provide an encoding for strings.

**errors**str, default ‘strict’

The error handling scheme to use for encoding errors. The default is ‘strict’ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and ‘xmlcharrefreplace’ as well as any other name registered with codecs.register\_error that can handle UnicodeEncodeErrors.

**track\_times**bool, default True

Parameter is propagated to ‘create\_table’ method of ‘PyTables’. If set to False it enables to have the same h5 files (same hashes) independent on creation time.

Deprecated since version 3.1.0: The default value of `track_times` will change from `True` to `False` in a future version. Pass `track_times=False` explicitly to silence this warning and get deterministic HDF5 files.

**dropna**bool, default False, optional

Remove missing values.

Deprecated since version 3.1.0: The `dropna` keyword is deprecated and will be removed in a future version. Use [`DataFrame.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")
 before writing instead.

See also

[`HDFStore.info`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.info.html#pandas.HDFStore.info "pandas.HDFStore.info")

Prints detailed information on the store.

[`HDFStore.get_storer`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.get_storer.html#pandas.HDFStore.get_storer "pandas.HDFStore.get_storer")

Returns the storer object for a key.

Notes

Writing an empty `DataFrame` or `Series` with `format='table'` or `append=True` is a no-op: the store is not modified and a `UserWarning` is emitted. Use `format='fixed'` to store an empty object.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df)

Copy to clipboard

On this page