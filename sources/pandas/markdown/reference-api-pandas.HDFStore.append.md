[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.HDFStore.append.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.HDFStore.append.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.HDFStore.append.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.HDFStore.append.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.HDFStore.append.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.HDFStore.append.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.HDFStore.append.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.HDFStore.append.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.HDFStore.append.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.HDFStore.append.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.HDFStore.append.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.HDFStore.append.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.HDFStore.append[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas-hdfstore-append "Link to this heading")

==================================================================================================================================================

HDFStore.append(_key_, _value_, _format\=None_, _axes\=None_, _index\=True_, _append\=True_, _complib\=None_, _complevel\=None_, _columns\=None_, _min\_itemsize\=None_, _nan\_rep\=None_, _chunksize\=None_, _expectedrows\=None_, _dropna\=<no\_default>_, _data\_columns\=None_, _encoding\=None_, _errors\='strict'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/pytables.py#L1572-L1730)
[#](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append.html#pandas.HDFStore.append "Link to this definition")

Append to Table in file.

Node must already exist and be Table format.

Parameters:

**key**str

Key of object to append.

**value**{Series, DataFrame}

Value of object to append.

**format**‘table’ is the default

Format to use when storing object in HDFStore. Value can be one of:

`'table'`

Table format. Write as a PyTables Table structure which may perform worse but allow more flexible operations like searching / selecting subsets of the data.

**axes**list, default None

Single-element list selecting the axis to store as the table’s indexed (appendable) axis: `[0]` for the index (the default) or `[1]` for the columns. Ignored when appending to an existing table, which keeps the axes it was created with.

**index**bool, default True

Write DataFrame index as a column.

**append**bool, default True

Append the input data to the existing.

**complib**{‘zlib’, ‘lzo’, ‘bzip2’, ‘blosc’}, default None

Compression library to use; None disables compression. See the `complib` parameter of `HDFStore` for the full list of supported compressors.

**complevel**int, 0-9, default None

Specifies a compression level for data. A value of 0 or None disables compression.

**columns**default None

This parameter is currently not accepted, try data\_columns.

**min\_itemsize**int, dict, or None

Minimum number of bytes reserved for object columns. If int, all columns reserve ‘min\_itemsize’ bytes per stored value. If dict, specific columns reserve ‘min\_itemsize’ bytes per stored value. Strings are stored as encoded bytes. Since some characters require multiple bytes, required size may be larger than string length.

**nan\_rep**str, optional

String used on disk to represent missing values in string columns. By default a sentinel that collides with no value in the column is used, so a literal `"nan"` round-trips unchanged; when this is passed, a value equal to it is read back as a missing value. Only used when the table is created; ignored on later appends, which reuse whatever the table already stores.

**chunksize**int, default 100000

Number of rows to write in each chunk.

**expectedrows**int

Expected TOTAL row size of this table.

**dropna**bool, default False, optional

Do not write an ALL nan row to the store settable by the option ‘io.hdf.dropna\_table’.

Deprecated since version 3.1.0: The `dropna` keyword is deprecated and will be removed in a future version. Use [`DataFrame.dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")
 before writing instead.

**data\_columns**list of columns, or True, default None

List of columns to create as indexed data columns for on-disk queries, or True to use all columns. By default only the axes of the object are indexed. See [here](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html#query-via-data-columns)
.

**encoding**default None

Provide an encoding for str.

**errors**str, default ‘strict’

The error handling scheme to use for encoding errors. The default is ‘strict’ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and ‘xmlcharrefreplace’ as well as any other name registered with codecs.register\_error that can handle UnicodeEncodeErrors.

See also

[`HDFStore.append_to_multiple`](https://pandas.pydata.org/docs/reference/api/pandas.HDFStore.append_to_multiple.html#pandas.HDFStore.append_to_multiple "pandas.HDFStore.append_to_multiple")

Append to multiple tables.

Notes

Does _not_ check if data being appended overlaps with existing data in the table, so be careful

Appending an empty `DataFrame` or `Series` is a no-op: the store is not modified and a `UserWarning` is emitted.

Examples

\>>> df1 \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["A", "B"\])
\>>> store \= pd.HDFStore("store.h5", "w")
\>>> store.put("data", df1, format\="table")
\>>> df2 \= pd.DataFrame(\[\[5, 6\], \[7, 8\]\], columns\=\["A", "B"\])
\>>> store.append("data", df2)
\>>> store.close()
   A  B
0  1  2
1  3  4
0  5  6
1  7  8

Copy to clipboard

On this page