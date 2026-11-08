[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.parsers.TextFileReader[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.html#pandas-io-parsers-textfilereader "Link to this heading")

================================================================================================================================================================================

class pandas.io.parsers.TextFileReader(_f_, _engine\=None_, _\*\*kwds_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/parsers/readers.py#L2631-L3171)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.html#pandas.io.parsers.TextFileReader "Link to this definition")

Iterator over chunks of a delimited text file.

Returned by `read_csv()`, `read_table()`, and `read_fwf()` when `iterator=True` or `chunksize` is given. Not intended to be constructed directly by users.

A `TextFileReader` can be iterated over to yield successive chunks as `DataFrame` objects, used as a context manager to ensure the underlying file handle is closed, or queried explicitly via [`read()`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas.io.parsers.TextFileReader.read "pandas.io.parsers.TextFileReader.read")
 and [`get_chunk()`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#pandas.io.parsers.TextFileReader.get_chunk "pandas.io.parsers.TextFileReader.get_chunk")
.

Passed `dialect` overrides any of the related parser options.

Parameters:

**f**str, path object, or file-like object

Source to read from. Accepts the same inputs as `read_csv()`.

**engine**{‘c’, ‘python’, ‘pyarrow’, ‘python-fwf’}, optional

Parser engine to use. If not specified, defaults to `'python'`.

**\*\*kwds**

Any keyword argument accepted by `read_csv()`, `read_table()`, or `read_fwf()`.

See also

`read_csv`

Read a comma-separated values (csv) file into a DataFrame.

`read_table`

Read general delimited file into a DataFrame.

`read_fwf`

Read a table of fixed-width formatted lines into a DataFrame.

Examples

\>>> with pd.read\_csv("data.csv", chunksize\=1000) as reader:
...     for chunk in reader:
...         process(chunk)

Copy to clipboard

\>>> with pd.read\_csv("data.csv", iterator\=True) as reader:
...     first \= reader.get\_chunk(5)

Copy to clipboard

Methods

|     |     |
| --- | --- |
| [`close`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.close.html#pandas.io.parsers.TextFileReader.close "pandas.io.parsers.TextFileReader.close")<br>() | Close the underlying file handle and parser engine. |
| [`get_chunk`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.get_chunk.html#pandas.io.parsers.TextFileReader.get_chunk "pandas.io.parsers.TextFileReader.get_chunk")<br>(\[size\]) | Read the next chunk of rows from the file. |
| [`read`](https://pandas.pydata.org/docs/reference/api/pandas.io.parsers.TextFileReader.read.html#pandas.io.parsers.TextFileReader.read "pandas.io.parsers.TextFileReader.read")<br>(\[nrows\]) | Read rows from the file into a `DataFrame`. |

On this page