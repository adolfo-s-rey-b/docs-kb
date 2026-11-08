[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.parsers.TextFileReader.get\_chunk[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#pandas-io-parsers-textfilereader-get-chunk "Link to this heading")

===============================================================================================================================================================================================================

TextFileReader.get\_chunk(_size\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/parsers/readers.py#L3116-L3160)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#pandas.io.parsers.TextFileReader.get_chunk "Link to this definition")

Read the next chunk of rows from the file.

Convenience wrapper around [`TextFileReader.read()`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas.io.parsers.TextFileReader.read "pandas.io.parsers.TextFileReader.read")
 that defaults `size` to the `chunksize` passed to `read_csv()` or `read_table()`, and respects a configured `nrows` limit by raising `StopIteration` once it has been reached.

Parameters:

**size**int, optional

Number of rows to read in this chunk. Defaults to the `chunksize` passed when the reader was created.

Returns:

DataFrame

The next chunk of parsed rows.

Raises:

StopIteration

If `nrows` was set and has already been reached.

See also

[`TextFileReader.read`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas.io.parsers.TextFileReader.read "pandas.io.parsers.TextFileReader.read")

Read rows from the file into a DataFrame.

`read_csv`

Read a comma-separated values (csv) file into a DataFrame.

Examples

\>>> with pd.read\_csv("data.csv", iterator\=True) as reader:
...     first\_five \= reader.get\_chunk(5)

Copy to clipboard

On this page