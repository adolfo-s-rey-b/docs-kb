[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.ExcelWriter.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.ExcelWriter.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.ExcelWriter.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.ExcelWriter.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.ExcelWriter.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.ExcelWriter.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.ExcelWriter.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.ExcelWriter.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.ExcelWriter.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.ExcelWriter.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.ExcelWriter.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.ExcelWriter.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.ExcelWriter[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas-excelwriter "Link to this heading")

======================================================================================================================================

class pandas.ExcelWriter(_path_, _engine\=None_, _date\_format\=None_, _datetime\_format\=None_, _mode\='w'_, _storage\_options\=None_, _if\_sheet\_exists\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/excel/_base.py#L989-L1463)
[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter "Link to this definition")

Class for writing DataFrame objects into excel sheets.

The default `engine` is chosen based on the file extension. The values below are the engine strings (i.e. valid values for the `engine` keyword); the package each one wraps is shown in parentheses:

*   `.xlsx`: `"xlsxwriter"` ([XlsxWriter](https://pypi.org/project/XlsxWriter/)
    ) if installed, otherwise `"openpyxl"` ([openpyxl](https://pypi.org/project/openpyxl/)
    ).
    
*   `.xlsm`: `"openpyxl"` ([openpyxl](https://pypi.org/project/openpyxl/)
    ).
    
*   `.ods`: `"odf"` ([odfpy](https://pypi.org/project/odfpy/)
    ).
    

These defaults can be overridden via the `engine` argument or by setting the `io.excel.<extension>.writer` option.

See [`DataFrame.to_excel()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")
 for typical usage.

The writer should be used as a context manager. Otherwise, call close() to save and close any opened file handles.

Parameters:

**path**str or typing.BinaryIO

Path to xlsx, xlsm, or ods file.

**engine**{‘openpyxl’, ‘xlsxwriter’, ‘odf’}, optional

Engine to use for writing, given as the engine string (not the package name). Which engines are accepted depends on the file extension:

*   `.xlsx`: `"openpyxl"` or `"xlsxwriter"`.
    
*   `.xlsm`: `"openpyxl"`.
    
*   `.ods`: `"odf"` (provided by the `odfpy` package).
    

If None, defaults to `io.excel.<extension>.writer`. NOTE: can only be passed as a keyword argument.

**date\_format**str, default None

Format string for dates written into Excel files (e.g. ‘YYYY-MM-DD’).

**datetime\_format**str, default None

Format string for datetime objects written into Excel files. (e.g. ‘YYYY-MM-DD HH:MM:SS’).

**mode**{‘w’, ‘a’}, default ‘w’

File mode to use (write or append). Append does not work with fsspec URLs.

Warning

In append mode the existing workbook is read and completely rewritten by the engine, so any content the engine cannot represent (e.g. VBA macros in `.xlsm` files, charts or images) is silently lost and the workbook may be otherwise altered.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**if\_sheet\_exists**{‘error’, ‘new’, ‘replace’, ‘overlay’}, default ‘error’

How to behave when trying to write to a sheet that already exists (append mode only).

*   error: raise a ValueError.
    
*   new: Create a new sheet, with a name determined by the engine.
    
*   replace: Delete the contents of the sheet before writing to it.
    
*   overlay: Write contents to the existing sheet without first removing, but possibly over top of, the existing contents.
    

**engine\_kwargs**dict, optional

Keyword arguments to be passed into the engine. The bullets below are keyed by the `engine` string (not the package name); for each engine, `engine_kwargs` is forwarded as follows:

*   `"xlsxwriter"`: `xlsxwriter.Workbook(file, **engine_kwargs)`
    
*   `"openpyxl"` (write mode): `openpyxl.Workbook(**engine_kwargs)`
    
*   `"openpyxl"` (append mode): `openpyxl.load_workbook(file, **engine_kwargs)`
    
*   `"odf"`: `odf.opendocument.OpenDocumentSpreadsheet(**engine_kwargs)`
    

See also

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel sheet values (xlsx) file into DataFrame.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

[`read_fwf`](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas.read_fwf "pandas.read_fwf")

Read a table of fixed-width formatted lines into DataFrame.

Notes

For compatibility with CSV writers, ExcelWriter serializes lists and dicts to strings before writing.

Examples

Default usage:

\>>> df \= pd.DataFrame(\[\["ABC", "XYZ"\]\], columns\=\["Foo", "Bar"\])
\>>> with pd.ExcelWriter("path\_to\_file.xlsx") as writer:
...     df.to\_excel(writer)

Copy to clipboard

To write to separate sheets in a single file:

\>>> df1 \= pd.DataFrame(\[\["AAA", "BBB"\]\], columns\=\["Spam", "Egg"\])
\>>> df2 \= pd.DataFrame(\[\["ABC", "XYZ"\]\], columns\=\["Foo", "Bar"\])
\>>> with pd.ExcelWriter("path\_to\_file.xlsx") as writer:
...     df1.to\_excel(writer, sheet\_name\="Sheet1")
...     df2.to\_excel(writer, sheet\_name\="Sheet2")

Copy to clipboard

You can set the date format or datetime format:

\>>> from datetime import date, datetime
\>>> df \= pd.DataFrame(
...     \[\
...         \[date(2014, 1, 31), date(1999, 9, 24)\],\
...         \[datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)\],\
...     \],
...     index\=\["Date", "Datetime"\],
...     columns\=\["X", "Y"\],
... )
\>>> with pd.ExcelWriter(
...     "path\_to\_file.xlsx",
...     date\_format\="YYYY-MM-DD",
...     datetime\_format\="YYYY-MM-DD HH:MM:SS",
... ) as writer:
...     df.to\_excel(writer)

Copy to clipboard

You can also append to an existing Excel file:

\>>> with pd.ExcelWriter("path\_to\_file.xlsx", mode\="a", engine\="openpyxl") as writer:
...     df.to\_excel(writer, sheet\_name\="Sheet3")

Copy to clipboard

Here, the if\_sheet\_exists parameter can be set to replace a sheet if it already exists:

\>>> with pd.ExcelWriter(
...     "path\_to\_file.xlsx",
...     mode\="a",
...     engine\="openpyxl",
...     if\_sheet\_exists\="replace",
... ) as writer:
...     df.to\_excel(writer, sheet\_name\="Sheet1")

Copy to clipboard

You can also write multiple DataFrames to a single sheet. Note that the `if_sheet_exists` parameter needs to be set to `overlay`:

\>>> with pd.ExcelWriter(
...     "path\_to\_file.xlsx",
...     mode\="a",
...     engine\="openpyxl",
...     if\_sheet\_exists\="overlay",
... ) as writer:
...     df1.to\_excel(writer, sheet\_name\="Sheet1")
...     df2.to\_excel(writer, sheet\_name\="Sheet1", startcol\=3)

Copy to clipboard

You can store Excel file in RAM:

\>>> import io
\>>> df \= pd.DataFrame(\[\["ABC", "XYZ"\]\], columns\=\["Foo", "Bar"\])
\>>> buffer \= io.BytesIO()
\>>> with pd.ExcelWriter(buffer) as writer:
...     df.to\_excel(writer)

Copy to clipboard

You can pack Excel file into zip archive:

\>>> import zipfile
\>>> df \= pd.DataFrame(\[\["ABC", "XYZ"\]\], columns\=\["Foo", "Bar"\])
\>>> with zipfile.ZipFile("path\_to\_file.zip", "w") as zf:
...     with zf.open("filename.xlsx", "w") as buffer:
...         with pd.ExcelWriter(buffer) as writer:
...             df.to\_excel(writer)

Copy to clipboard

You can specify additional arguments to the underlying engine:

\>>> with pd.ExcelWriter(
...     "path\_to\_file.xlsx",
...     engine\="xlsxwriter",
...     engine\_kwargs\={"options": {"nan\_inf\_to\_errors": True}},
... ) as writer:
...     df.to\_excel(writer)

Copy to clipboard

In append mode, `engine_kwargs` are passed through to openpyxl’s `load_workbook`:

\>>> with pd.ExcelWriter(
...     "path\_to\_file.xlsx",
...     engine\="openpyxl",
...     mode\="a",
...     engine\_kwargs\={"keep\_vba": True},
... ) as writer:
...     df.to\_excel(writer, sheet\_name\="Sheet2")

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| `book` | Book instance. |
| `date_format` | Format string for dates written into Excel files (e.g. 'YYYY-MM-DD'). |
| `datetime_format` | Format string for dates written into Excel files (e.g. 'YYYY-MM-DD'). |
| `engine` | Name of engine. |
| `if_sheet_exists` | How to behave when writing to a sheet that already exists in append mode. |
| `sheets` | Mapping of sheet names to sheet objects. |
| `supported_extensions` | Extensions that writer engine supports. |

Methods

|     |     |
| --- | --- |
| `check_extension`(ext) | checks that path's extension against the Writer's supported extensions. |
| `close`() | synonym for save, to make it more file-like |

On this page