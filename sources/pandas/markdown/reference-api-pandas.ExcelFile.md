[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.ExcelFile.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.ExcelFile.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.ExcelFile.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.ExcelFile.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.ExcelFile.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.ExcelFile.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.ExcelFile.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.ExcelFile.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.ExcelFile.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.ExcelFile.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.ExcelFile.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.ExcelFile.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.ExcelFile[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html#pandas-excelfile "Link to this heading")

================================================================================================================================

class pandas.ExcelFile(_path\_or\_buffer_, _engine\=None_, _storage\_options\=None_, _engine\_kwargs\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/excel/_base.py#L1567-L1989)
[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.html#pandas.ExcelFile "Link to this definition")

Class for parsing tabular Excel sheets into DataFrame objects.

See read\_excel for more documentation.

Parameters:

**path\_or\_buffer**str, bytes, pathlib.Path,

A file-like object or a workbook object from a supported engine. If a string or path object, expected to be a path to a .xls, .xlsx, .xlsb, .xlsm, .odf, .ods, or .odt file.

**engine**str, default None

Supported engines: `xlrd`, `openpyxl`, `odf`, `pyxlsb`, `calamine` Engine compatibility :

*   `xlrd` supports old-style Excel files (.xls).
    
*   `openpyxl` supports newer Excel file formats.
    
*   `odf` supports OpenDocument file formats (.odf, .ods, .odt).
    
*   `pyxlsb` supports Binary Excel files.
    
*   `calamine` supports Excel (.xls, .xlsx, .xlsm, .xlsb) and OpenDocument (.ods) file formats.
    

The engine [xlrd](https://xlrd.readthedocs.io/en/latest/)
 now only supports old-style `.xls` files. When `engine=None`, the following logic will be used to determine the engine:

*   If `path_or_buffer` is a workbook object, the engine that created it
    
    will be used.
    
*   Otherwise if `path_or_buffer` is an OpenDocument format (.odf, .ods, .odt),
    
    then [odf](https://pypi.org/project/odfpy/)
     will be used.
    
*   Otherwise if `path_or_buffer` is an xls format,
    
    `xlrd` will be used.
    
*   Otherwise if `path_or_buffer` is in xlsb format,
    
    [pyxlsb](https://pypi.org/project/pyxlsb/)
     will be used.
    
*   Otherwise if [openpyxl](https://pypi.org/project/openpyxl/)
     is installed,
    
    then `openpyxl` will be used.
    
*   Otherwise if `xlrd >= 2.0` is installed, a `ValueError` will be raised.
    

Deprecated since version 3.1.0: For xlsx/xlsm files the default engine will change from `openpyxl` to `calamine` in a future version. Pass `engine` explicitly, or set the `io.excel.xlsx.reader` option (xlsm files are format-detected as xlsx), to keep the current behavior.

Warning

Please do not report issues when using `xlrd` to read `.xlsx` files. This is not supported, switch to using `openpyxl` instead.

**storage\_options**dict, optional

Extra options that make sense for a particular storage connection, e.g. host, port, username, password, etc. For HTTP(S) URLs the key-value pairs are forwarded to `urllib.request.Request` as header options. For other URLs (e.g. starting with “s3://”, and “gcs://”) the key-value pairs are forwarded to `fsspec.open`. Please see `fsspec` and `urllib` for more details, and for more examples on storage options refer [here](https://pandas.pydata.org/docs/user_guide/io.html?highlight=storage_options#reading-writing-remote-files)
.

**engine\_kwargs**dict, optional

Arbitrary keyword arguments passed to excel engine.

See also

[`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")

Write DataFrame to an Excel file.

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write DataFrame to a comma-separated values (csv) file.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

[`read_fwf`](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas.read_fwf "pandas.read_fwf")

Read a table of fixed-width formatted lines into DataFrame.

Examples

\>>> file \= pd.ExcelFile("myfile.xlsx")
\>>> with pd.ExcelFile("myfile.xls") as xls:
...     df1 \= pd.read\_excel(xls, "Sheet1")

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| [`book`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.book.html#pandas.ExcelFile.book "pandas.ExcelFile.book") | Gets the Excel workbook. |
| [`sheet_names`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html#pandas.ExcelFile.sheet_names "pandas.ExcelFile.sheet_names") | Names of the sheets in the document. |

Methods

|     |     |
| --- | --- |
| `close`() | close io if necessary |
| [`parse`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html#pandas.ExcelFile.parse "pandas.ExcelFile.parse")<br>(\[sheet\_name, header, names, ...\]) | (DEPRECATED) Parse specified sheet(s) into a DataFrame. |

On this page