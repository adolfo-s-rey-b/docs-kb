[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.ExcelFile.parse.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.ExcelFile.parse.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.ExcelFile.parse.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.ExcelFile.parse.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.ExcelFile.parse.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.ExcelFile.parse.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.ExcelFile.parse.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.ExcelFile.parse.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.ExcelFile.parse.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.ExcelFile.parse.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.ExcelFile.parse.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.ExcelFile.parse.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.ExcelFile.parse[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html#pandas-excelfile-parse "Link to this heading")

==================================================================================================================================================

ExcelFile.parse(_sheet\_name\=0_, _header\=0_, _names\=None_, _index\_col\=None_, _usecols\=None_, _converters\=None_, _true\_values\=None_, _false\_values\=None_, _skiprows\=None_, _nrows\=None_, _na\_values\=None_, _parse\_dates\=False_, _date\_format\=None_, _thousands\=None_, _comment\=None_, _skipfooter\=0_, _dtype\_backend\=<no\_default>_, _\*\*kwds_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/excel/_base.py#L1725-L1917)
[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html#pandas.ExcelFile.parse "Link to this definition")

Parse specified sheet(s) into a DataFrame.

Deprecated since version 3.1.0: Use `pd.read_excel()` instead.

Equivalent to read\_excel(ExcelFile, …) See the read\_excel docstring for more info on accepted parameters.

Parameters:

**sheet\_name**str, int, list, or None, default 0

Strings are used for sheet names. Integers are used in zero-indexed sheet positions (chart sheets do not count as a sheet position). Lists of strings/integers are used to request multiple sheets. When `None`, will return a dictionary containing DataFrames for each sheet.

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

**converters**dict, default None

Dict of functions for converting values in certain columns. Keys can either be integers or column labels, values are functions that take one input argument, the Excel cell content, and return the transformed content.

**true\_values**list, default None

Values to consider as True.

**false\_values**list, default None

Values to consider as False.

**skiprows**list-like, int, or callable, optional

Line numbers to skip (0-indexed) or number of lines to skip (int) at the start of the file. If callable, the callable function will be evaluated against the row indices, returning True if the row should be skipped and False otherwise. An example of a valid callable argument would be `lambda x: x in [0, 2]`.

**nrows**int, default None

Number of rows to parse.

**na\_values**scalar, str, list-like, or dict, default None

Additional strings to recognize as NA/NaN. If dict passed, specific per-column NA values.

**parse\_dates**bool, list-like, or dict, default False

The behavior is as follows:

*   `bool`. If True -> try parsing the index.
    
*   `list` of int or names. e.g. If \[1, 2, 3\] -> try parsing columns 1, 2, 3 each as a separate date column.
    
*   `list` of lists. e.g. If \[\[1, 3\]\] -> combine columns 1 and 3 and parse as a single date column.
    
*   `dict`, e.g. {‘foo’ : \[1, 3\]} -> parse columns 1, 3 as date and call result ‘foo’
    

If a column or index contains an unparsable date, the entire column or index will be returned unaltered as an object data type. If you don\`t want to parse some cells as date just change their type in Excel to “Text”.For non-standard datetime parsing, use `pd.to_datetime` after `pd.read_excel`.

Note: A fast-path exists for iso8601-formatted dates.

**date\_format**str or dict of column -> format, default `None`

If used in conjunction with `parse_dates`, will parse dates according to this format. For anything more complex, please read in as `object` and then apply [`to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
 as-needed.

**thousands**str, default None

Thousands separator for parsing string columns to numeric. Note that this parameter is only necessary for columns stored as TEXT in Excel, any numeric columns will automatically be parsed, regardless of display format.

**comment**str, default None

Comments out remainder of line. Pass a character or characters to this argument to indicate comments in the input file. Any data between the comment string and the end of the current line is ignored.

**skipfooter**int, default 0

Rows at the end to skip (0-indexed).

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**\*\*kwds**dict, optional

Arbitrary keyword arguments passed to excel engine.

Returns:

DataFrame or dict of DataFrames

DataFrame from the passed in Excel file.

See also

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel sheet values (xlsx) file into DataFrame.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

[`read_fwf`](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas.read_fwf "pandas.read_fwf")

Read a table of fixed-width formatted lines into DataFrame.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2, 3\], \[4, 5, 6\]\], columns\=\["A", "B", "C"\])
\>>> df.to\_excel("myfile.xlsx")
\>>> file \= pd.ExcelFile("myfile.xlsx")
\>>> file.parse()

Copy to clipboard

On this page