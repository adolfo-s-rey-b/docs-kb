[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_excel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.to_excel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_excel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.to_excel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.to_excel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.to_excel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.to_excel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.to_excel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.to_excel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.to_excel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.to_excel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.to_excel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.to_excel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.to_excel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.to\_excel[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_excel.html#pandas-series-to-excel "Link to this heading")

===================================================================================================================================================

Series.to\_excel(_excel\_writer_, _\*_, _sheet\_name\='Sheet1'_, _na\_rep\=''_, _float\_format\=None_, _columns\=None_, _header\=True_, _index\=True_, _index\_label\=None_, _startrow\=0_, _startcol\=0_, _engine\=None_, _merge\_cells\=True_, _inf\_rep\='inf'_, _freeze\_panes\=None_, _storage\_options\=None_, _engine\_kwargs\=None_, _autofilter\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L2105-L2277)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_excel.html#pandas.Series.to_excel "Link to this definition")

Write object to an Excel sheet.

To write a single object to an Excel .xlsx file it is only necessary to specify a target file name. To write to multiple sheets it is necessary to create an ExcelWriter object with a target file name, and specify a sheet in the file to write to.

Multiple sheets may be written to by specifying unique sheet\_name. With all data written to the file it is necessary to save the changes. Note that creating an ExcelWriter object with a file name that already exists will overwrite the existing file because the default mode is write.

Parameters:

**excel\_writer**path-like, file-like, or ExcelWriter object

File path or existing ExcelWriter.

**sheet\_name**str, default ‘Sheet1’

Name of sheet which will contain DataFrame.

**na\_rep**str, default ‘’

Missing data representation.

**float\_format**str, optional

Format string for floating point numbers. For example `float_format="%.2f"` will format 0.1234 to 0.12.

**columns**sequence or list of str, optional

Columns to write.

**header**bool or list of str, default True

Write out the column names. If a list of string is given it is assumed to be aliases for the column names.

**index**bool, default True

Write row names (index).

**index\_label**str or sequence, optional

Column label for index column(s) if desired. If not specified, and header and index are True, then the index names are used. A sequence should be given if the DataFrame uses MultiIndex.

**startrow**int, default 0

Upper left cell row to dump data frame.

**startcol**int, default 0

Upper left cell column to dump data frame.

**engine**str, optional

Write engine to use, ‘openpyxl’ or ‘xlsxwriter’. You can also set this via the options `io.excel.xlsx.writer` or `io.excel.xlsm.writer`.

**merge\_cells**bool or ‘columns’, default True

If True, write MultiIndex index and columns as merged cells. If ‘columns’, merge MultiIndex column cells only.

**inf\_rep**str, default ‘inf’

Representation for infinity (there is no native representation for infinity in Excel).

**freeze\_panes**tuple of int (length 2), optional

Specifies the one-based bottommost row and rightmost column that is to be frozen.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**engine\_kwargs**dict, optional

Arbitrary keyword arguments passed to excel engine.

**autofilter**bool, default False

If True, add automatic filters to all columns.

See also

[`to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_csv.html#pandas.Series.to_csv "pandas.Series.to_csv")

Write DataFrame to a comma-separated values (csv) file.

[`ExcelWriter`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter "pandas.ExcelWriter")

Class for writing DataFrame objects into excel sheets.

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel file into a pandas DataFrame.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

[`io.formats.style.Styler.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_excel.html#pandas.io.formats.style.Styler.to_excel "pandas.io.formats.style.Styler.to_excel")

Add styles to Excel sheet.

Notes

For compatibility with [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")
, to\_excel serializes lists and dicts to strings before writing.

Once a workbook has been saved it is not possible to write further data without rewriting the whole workbook.

pandas will check the number of rows, columns, and cell character count does not exceed Excel’s limitations. All other limitations must be checked by the user.

Examples

Create, write to and save a workbook:

\>>> df1 \= pd.DataFrame(
...     \[\["a", "b"\], \["c", "d"\]\],
...     index\=\["row 1", "row 2"\],
...     columns\=\["col 1", "col 2"\],
... )
\>>> df1.to\_excel("output.xlsx")

Copy to clipboard

To specify the sheet name:

\>>> df1.to\_excel("output.xlsx", sheet\_name\="Sheet\_name\_1")

Copy to clipboard

If you wish to write to more than one sheet in the workbook, it is necessary to specify an ExcelWriter object:

\>>> df2 \= df1.copy()
\>>> with pd.ExcelWriter("output.xlsx") as writer:
...     df1.to\_excel(writer, sheet\_name\="Sheet\_name\_1")
...     df2.to\_excel(writer, sheet\_name\="Sheet\_name\_2")

Copy to clipboard

ExcelWriter can also be used to append to an existing Excel file:

\>>> with pd.ExcelWriter("output.xlsx", mode\="a") as writer:
...     df1.to\_excel(writer, sheet\_name\="Sheet\_name\_3")

Copy to clipboard

To set the library that is used to write the Excel file, you can pass the engine keyword (the default engine is automatically chosen depending on the file extension):

\>>> df1.to\_excel("output1.xlsx", engine\="xlsxwriter")

Copy to clipboard

On this page