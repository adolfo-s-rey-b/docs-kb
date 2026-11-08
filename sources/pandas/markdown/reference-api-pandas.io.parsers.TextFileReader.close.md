[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.close.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.parsers.TextFileReader.close.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.close.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.parsers.TextFileReader.close.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.parsers.TextFileReader.close.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.parsers.TextFileReader.close.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.parsers.TextFileReader.close.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.parsers.TextFileReader.close.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.parsers.TextFileReader.close.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.parsers.TextFileReader.close.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.parsers.TextFileReader.close.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.parsers.TextFileReader.close.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.parsers.TextFileReader.close.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.parsers.TextFileReader.close.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.parsers.TextFileReader.close[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.close.html#pandas-io-parsers-textfilereader-close "Link to this heading")

==================================================================================================================================================================================================

TextFileReader.close()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/parsers/readers.py#L2723-L2742)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.close.html#pandas.io.parsers.TextFileReader.close "Link to this definition")

Close the underlying file handle and parser engine.

Called automatically when the `TextFileReader` is used as a context manager.

See also

[`TextFileReader.read`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas.io.parsers.TextFileReader.read "pandas.io.parsers.TextFileReader.read")

Read rows from the file into a DataFrame.

[`TextFileReader.get_chunk`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#pandas.io.parsers.TextFileReader.get_chunk "pandas.io.parsers.TextFileReader.get_chunk")

Read the next chunk of rows.

Examples

\>>> reader \= pd.read\_csv("data.csv", chunksize\=5)
\>>> reader.close()

Copy to clipboard

On this page