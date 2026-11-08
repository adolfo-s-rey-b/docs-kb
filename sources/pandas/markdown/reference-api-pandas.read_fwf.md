[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_fwf[#](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas-read-fwf "Link to this heading")

==============================================================================================================================

pandas.read\_fwf(_filepath\_or\_buffer_, _\*_, _colspecs\='infer'_, _widths\=None_, _infer\_nrows\=100_, _iterator\=False_, _chunksize\=None_, _\*\*kwds_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/parsers/readers.py#L2505-L2628)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_fwf.html#pandas.read_fwf "Link to this definition")

Read a table of fixed-width formatted lines into DataFrame.

Also supports optionally iterating or breaking of the file into chunks.

Additional help can be found in the [online docs for IO Tools](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html)
.

Parameters:

**filepath\_or\_buffer**str, path object, or file-like object

Any valid string path is acceptable. The string could be a URL. Valid URL schemes include http, ftp, s3, and file. For file URLs, a host is expected. A local file could be: `file://localhost/path/to/table.csv`.

Certain URL schemes may require additional packages. For example, S3 URLs require the `s3fs` library. See [Optional dependencies](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)
 for a full list.

If you want to pass in a path object, pandas accepts any `os.PathLike`.

By file-like object, we refer to objects with a `read()` method that accepts an optional size argument, such as a file handle (e.g. via builtin `open` function) or `StringIO`.

**colspecs**list of tuple (int, int) or ‘infer’. optional

A list of tuples giving the extents of the fixed-width fields of each line as half-open intervals (i.e., \[from, to\] ). String value ‘infer’ can be used to instruct the parser to try detecting the column specifications from the first 100 rows of the data which are not being skipped via skiprows (default=’infer’).

**widths**list of int, optional

A list of field widths which can be used instead of ‘colspecs’ if the intervals are contiguous.

**infer\_nrows**int, default 100

The number of rows to consider when letting the parser determine the `colspecs`. Pass `np.inf` to infer column specifications from the entire file, which is useful when columns vary in width and a value wider than anything in the first `infer_nrows` rows would otherwise be truncated.

**iterator**bool, default False

Return `TextFileReader` object for iteration or getting chunks with `get_chunk()`.

**chunksize**int, optional

Number of lines to read from the file per chunk.

**\*\*kwds**optional

Optional keyword arguments can be passed to `TextFileReader`.

Returns:

DataFrame or TextFileReader

A comma-separated values (csv) file is returned as two-dimensional data structure with labeled axes.

See also

[`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")

Write DataFrame to a comma-separated values (csv) file.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

Examples

\>>> pd.read\_fwf("data.csv")

Copy to clipboard

On this page