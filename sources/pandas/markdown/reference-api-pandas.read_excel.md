[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_excel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_excel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_excel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_excel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_excel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_excel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_excel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_excel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_excel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_excel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_excel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_excel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_excel[#](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas-read-excel "Link to this heading")

====================================================================================================================================

pandas.read\_excel(_io_, _sheet\_name\=0_, _\*_, _header\=0_, _names\=None_, _index\_col\=None_, _usecols\=None_, _dtype\=None_, _engine\=None_, _converters\=None_, _true\_values\=None_, _false\_values\=None_, _skiprows\=None_, _nrows\=None_, _na\_values\=None_, _keep\_default\_na\=True_, _na\_filter\=True_, _verbose\=False_, _parse\_dates\=False_, _date\_format\=None_, _thousands\=None_, _decimal\='.'_, _comment\=None_, _skipfooter\=0_, _storage\_options\=None_, _dtype\_backend\=<no\_default>_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/excel/_base.py#L162-L554)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "Link to this definition")

Read an Excel file into a `DataFrame`.

Supports xls, xlsx, xlsm, xlsb, odf, ods and odt file extensions read from a local filesystem or URL. Supports an option to read a single sheet or a list of sheets.

This function requires an external library depending on the file format; see the `engine` parameter below.

Parameters:

**io**str, ExcelFile, workbook object, path object, or file-like object

Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.xlsx`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

If you want to pass in a path object, pandas accepts any `os.PathLike`.

By file-like object, we refer to objects with a `read()` method, such as a file handle (e.g. via builtin `open` function) or `StringIO`.

A workbook object from a supported engine’s library, such as an `openpyxl.Workbook`, is read with that engine.

**sheet\_name**str, int, list, or None, default 0

Strings are used for sheet names. Integers are used in zero-indexed sheet positions (chart sheets do not count as a sheet position). Lists of strings/integers are used to request multiple sheets. When `None`, will return a dictionary containing DataFrames for each sheet.

Available cases:

*   Defaults to `0`: 1st sheet as a DataFrame
    
*   `1`: 2nd sheet as a DataFrame
    
*   `"Sheet1"`: Load sheet with name “Sheet1”
    
*   `[0, 1, "Sheet5"]`: Load first, second and sheet named “Sheet5” as a dict of DataFrame
    
*   `None`: Returns a dictionary containing DataFrames for each sheet.
    

**header**int, list of int, default 0

Row (0-indexed) to use for the column labels of the parsed DataFrame. If a list of integers is passed those row positions will be combined into a `MultiIndex`. Use None if there is no header.

**names**array-like, default None

List of column names to use. If file contains no header row, then you should explicitly pass header=None.

**index\_col**int, str, list of int, default None

Column (0-indexed) to use as the row labels of the DataFrame. Pass None if there is no such column. If a list is passed, those columns will be combined into a `MultiIndex`. If a subset of data is selected with `usecols`, index\_col is based on the subset.

Missing values will be forward filled to allow roundtripping with `to_excel` for `merged_cells=True`. To avoid forward filling the missing values use `set_index` after reading the data instead of `index_col`.

When `header` is a list of two or more rows (`MultiIndex` columns), the row after the last header row is expected to hold the index name(s) — blank if the index is unnamed — as written by `to_excel`. A file lacking this separator row can lose its first data row to the index name(s); see [the user guide](https://pandas.pydata.org/docs/user_guide/io.html#io-excel-reading-multiindex)
 for details.

**usecols**str, list-like, or callable, default None

*   If None, then parse all columns.
    
*   If str, then indicates comma separated list of Excel column letters and column ranges (e.g. “A:E” or “A,C,E:F”). Ranges are inclusive of both sides.
    
*   If list of int, then indicates list of column numbers to be parsed (0-indexed).
    
*   If list of string, then indicates list of column names to be parsed.
    
*   If callable, then evaluate each column name against it and parse the column if the callable returns `True`.
    

Returns a subset of the columns according to behavior above. Element order is ignored, so `usecols=[0, 1]` is the same as `[1, 0]`. To instantiate a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 with element order preserved use `pd.read_excel(path, usecols=['foo', 'bar'])[['foo', 'bar']]` for columns in `['foo', 'bar']` order or `pd.read_excel(path, usecols=['foo', 'bar'])[['bar', 'foo']]` for `['bar', 'foo']` order.

**dtype**Type name or dict of column -> type, default None

Data type for data or columns. E.g. {‘a’: np.float64, ‘b’: np.int32} Use `object` to preserve data as stored in Excel and not interpret dtype, which will necessarily result in `object` dtype. Specifying a `dtype` does not change how missing values are parsed; values recognized as missing (see `na_values` and `keep_default_na`) are still read as `NaN` (or the dtype’s NA value) rather than cast to the requested `dtype`. If converters are specified, they will be applied INSTEAD of dtype conversion. If you use `None`, it will infer the dtype of each column based on the data.

**engine**{‘openpyxl’, ‘calamine’, ‘odf’, ‘pyxlsb’, ‘xlrd’}, default None

Engine compatibility :

*   `openpyxl` supports newer Excel file formats.
    
*   `calamine` supports Excel (.xls, .xlsx, .xlsm, .xlsb) and OpenDocument (.ods) file formats.
    
*   `odf` supports OpenDocument file formats (.odf, .ods, .odt).
    
*   `pyxlsb` supports Binary Excel files.
    
*   `xlrd` supports old-style Excel files (.xls).
    

When `engine=None`, the following logic will be used to determine the engine:

*   If `io` is a workbook object, the engine that created it will be used.
    
*   Otherwise if `path_or_buffer` is an OpenDocument format (.odf, .ods, .odt), then [odf](https://pypi.org/project/odfpy/)
     will be used.
    
*   Otherwise if `path_or_buffer` is an xls format, `xlrd` will be used.
    
*   Otherwise if `path_or_buffer` is in xlsb format, `pyxlsb` will be used.
    
*   Otherwise `openpyxl` will be used.
    

Deprecated since version 3.1.0: For xlsx/xlsm files the default engine will change from `openpyxl` to `calamine` in a future version. Pass `engine` explicitly, or set the `io.excel.xlsx.reader` option (xlsm files are format-detected as xlsx), to keep the current behavior.

**converters**dict, default None

Dict of functions for converting values in certain columns. Keys can either be integers or column labels, values are functions that take one input argument, the Excel cell content, and return the transformed content.

**true\_values**list, default None

Values to consider as True.

**false\_values**list, default None

Values to consider as False.

**skiprows**list-like, int, or callable, optional

Line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file. If callable, the callable function will be evaluated against the row indices, returning True if the row should be skipped and False otherwise. An example of a valid callable argument would be `lambda x: x in [0, 2]`.

**nrows**int, default None

Number of rows to parse. Does not include header rows.

**na\_values**scalar, str, list-like, or dict, default None

Additional strings to recognize as NA/NaN. If dict passed, specific per-column NA values. By default the following values are interpreted as NaN: ‘’, ‘#N/A’, ‘#N/A N/A’, ‘#NA’, ‘-1.#IND’, ‘-1.#QNAN’, ‘-NaN’, ‘-nan’, ‘1.#IND’, ‘1.#QNAN’, ‘<NA>’, ‘N/A’, ‘NA’, ‘NULL’, ‘NaN’, ‘None’, ‘n/a’, ‘nan’, ‘null’.

**keep\_default\_na**bool, default True

Whether or not to include the default NaN values when parsing the data. Depending on whether `na_values` is passed in, the behavior is as follows:

*   If `keep_default_na` is True, and `na_values` are specified, `na_values` is appended to the default NaN values used for parsing.
    
*   If `keep_default_na` is True, and `na_values` are not specified, only the default NaN values are used for parsing.
    
*   If `keep_default_na` is False, and `na_values` are specified, only the NaN values specified `na_values` are used for parsing.
    
*   If `keep_default_na` is False, and `na_values` are not specified, no strings will be parsed as NaN.
    

Note that if na\_filter is passed in as False, the `keep_default_na` and `na_values` parameters will be ignored.

**na\_filter**bool, default True

Detect missing value markers (empty strings and the value of na\_values). In data without any NAs, passing `na_filter=False` can improve the performance of reading a large file.

**verbose**bool, default False

Indicate number of NA values placed in non-numeric columns.

**parse\_dates**bool, list-like, or dict, default False

The behavior is as follows:

*   `bool`. If True -> try parsing the index.
    
*   `list` of int or names. e.g. If \[1, 2, 3\] -> try parsing columns 1, 2, 3 each as a separate date column.
    
*   `list` of lists. e.g. If \[\[1, 3\]\] -> combine columns 1 and 3 and parse as a single date column.
    
*   `dict`, e.g. {‘foo’ : \[1, 3\]} -> parse columns 1, 3 as date and call result ‘foo’
    

If a column or index contains an unparsable date, the entire column or index will be returned unaltered as an object data type. If you don\`t want to parse some cells as date just change their type in Excel to “Text”. For non-standard datetime parsing, use `pd.to_datetime` after `pd.read_excel`.

Note: A fast-path exists for iso8601-formatted dates.

**date\_format**str or dict of column -> format, default `None`

If used in conjunction with `parse_dates`, will parse dates according to this format. For anything more complex, please read in as `object` and then apply [`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
 as-needed.

Added in version 2.0.0.

**thousands**str, default None

Thousands separator for parsing string columns to numeric. Note that this parameter is only necessary for columns stored as TEXT in Excel, any numeric columns will automatically be parsed, regardless of display format.

**decimal**str, default ‘.’

Character to recognize as decimal point for parsing string columns to numeric. Note that this parameter is only necessary for columns stored as TEXT in Excel, any numeric columns will automatically be parsed, regardless of display format.(e.g. use ‘,’ for European data).

**comment**str, default None

Comments out remainder of line. Pass a character or characters to this argument to indicate comments in the input file. Any data between the comment string and the end of the current line is ignored.

**skipfooter**int, default 0

Rows at the end to skip (0-indexed).

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

**engine\_kwargs**dict, optional

Arbitrary keyword arguments passed to excel engine.

Returns:

DataFrame or dict of DataFrames

DataFrame from the passed in Excel file. See notes in sheet\_name argument for more information on when a dict of DataFrames is returned.

See also

[`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")

Write DataFrame to an Excel file.

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write DataFrame to a comma-separated values (csv) file.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

[`read_fwf`](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas.read_fwf "pandas.read_fwf")

Read a table of fixed-width formatted lines into DataFrame.

Notes

For specific information on the methods used for each Excel engine, refer to the pandas [user guide](https://pandas.pydata.org/docs/user_guide/io.html#io-excel-reader)

Examples

The file can be read using the file name as string or an open file object:

\>>> pd.read\_excel("tmp.xlsx", index\_col\=0)
       Name  Value
0   string1      1
1   string2      2
2  #Comment      3

Copy to clipboard

\>>> pd.read\_excel(open("tmp.xlsx", "rb"), sheet\_name\="Sheet3")
   Unnamed: 0      Name  Value
0           0   string1      1
1           1   string2      2
2           2  #Comment      3

Copy to clipboard

Index and header can be specified via the index\_col and header arguments

\>>> pd.read\_excel("tmp.xlsx", index\_col\=None, header\=None)
     0         1      2
0  NaN      Name  Value
1  0.0   string1      1
2  1.0   string2      2
3  2.0  #Comment      3

Copy to clipboard

Column types are inferred but can be explicitly specified

\>>> pd.read\_excel(
...     "tmp.xlsx", index\_col\=0, dtype\={"Name": str, "Value": float}
... )
       Name  Value
0   string1    1.0
1   string2    2.0
2  #Comment    3.0

Copy to clipboard

True, False, and NA values, and thousands separators have defaults, but can be explicitly specified, too. Supply the values you would like as strings or lists of strings!

\>>> pd.read\_excel(
...     "tmp.xlsx", index\_col\=0, na\_values\=\["string1", "string2"\]
... )
       Name  Value
0       NaN      1
1       NaN      2
2  #Comment      3

Copy to clipboard

Comment lines in the excel input file can be skipped using the `comment` kwarg.

\>>> pd.read\_excel("tmp.xlsx", index\_col\=0, comment\="#")
      Name  Value
0  string1    1.0
1  string2    2.0
2     None    NaN

Copy to clipboard

On this page