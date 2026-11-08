[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.book.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.ExcelFile.book[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.book.html#pandas-excelfile-book "Link to this heading")

===============================================================================================================================================

property ExcelFile.book[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/excel/_base.py#L1919-L1947)
[#](https://pandas.pydata.org/docs/reference/api/pandas.ExcelFile.book.html#pandas.ExcelFile.book "Link to this definition")

Gets the Excel workbook.

Workbook is the top-level container for all document information.

Returns:

Excel Workbook

The workbook object of the type defined by the engine being used.

See also

[`read_excel`](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html#pandas.read_excel "pandas.read_excel")

Read an Excel file into a pandas DataFrame.

Examples

\>>> file \= pd.ExcelFile("myfile.xlsx")
\>>> file.book
<openpyxl.workbook.workbook.Workbook object at 0x11eb5ad70>
\>>> file.book.path
'/xl/workbook.xml'
\>>> file.book.active
<openpyxl.worksheet.\_read\_only.ReadOnlyWorksheet object at 0x11eb5b370>
\>>> file.book.sheetnames
\['Sheet1', 'Sheet2'\]

Copy to clipboard

On this page