[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.parsers.TextFileReader.read[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas-io-parsers-textfilereader-read "Link to this heading")

===============================================================================================================================================================================================

TextFileReader.read(_nrows\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/parsers/readers.py#L3015-L3114)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas.io.parsers.TextFileReader.read "Link to this definition")

Read rows from the file into a `DataFrame`.

Advances the internal cursor by the number of rows returned, so successive calls yield later rows of the file. Used with readers created via `read_csv()` or `read_table()` with `iterator=True` or `chunksize` set.

Parameters:

**nrows**int, optional

Number of rows to read. If `None`, read until end of file. Ignored when the underlying engine is `"pyarrow"`, which always reads the full file.

Returns:

DataFrame

The parsed rows.

See also

[`TextFileReader.get_chunk`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#pandas.io.parsers.TextFileReader.get_chunk "pandas.io.parsers.TextFileReader.get_chunk")

Read the next chunk of rows.

`read_csv`

Read a comma-separated values (csv) file into a DataFrame.

Examples

\>>> with pd.read\_csv("data.csv", iterator\=True) as reader:
...     df \= reader.read()

Copy to clipboard

On this page