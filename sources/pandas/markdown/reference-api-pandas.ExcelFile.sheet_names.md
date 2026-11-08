[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.ExcelFile.sheet_names.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.ExcelFile.sheet_names.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.ExcelFile.sheet_names.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.ExcelFile.sheet_names.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.ExcelFile.sheet_names.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.ExcelFile.sheet_names.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.ExcelFile.sheet_names.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.ExcelFile.sheet_names.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.ExcelFile.sheet_names.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.ExcelFile.sheet_names.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.ExcelFile.sheet_names.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.ExcelFile.sheet_names.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.ExcelFile.sheet\_names[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html#pandas-excelfile-sheet-names "Link to this heading")

=====================================================================================================================================================================

property ExcelFile.sheet\_names[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/excel/_base.py#L1949-L1974)
[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.sheet_names.html#pandas.ExcelFile.sheet_names "Link to this definition")

Names of the sheets in the document.

This is particularly useful for loading a specific sheet into a DataFrame when you do not know the sheet names beforehand.

Returns:

list of str

List of sheet names in the document.

See also

[`ExcelFile.parse`](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.parse.html#pandas.ExcelFile.parse "pandas.ExcelFile.parse")

Parse a sheet into a DataFrame.

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel file into a pandas DataFrame. If you know the sheet names, it may be easier to specify them directly to read\_excel.

Examples

\>>> file \= pd.ExcelFile("myfile.xlsx")
\>>> file.sheet\_names
\["Sheet1", "Sheet2"\]

Copy to clipboard

On this page