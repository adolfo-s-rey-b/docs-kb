[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_typst.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.to\_typst[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_typst.html#pandas-io-formats-style-styler-to-typst "Link to this heading")

======================================================================================================================================================================================================

Styler.to\_typst(_buf\=None_, _\*_, _encoding\=None_, _sparse\_index\=None_, _sparse\_columns\=None_, _max\_rows\=None_, _max\_columns\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L1320-L1403)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_typst.html#pandas.io.formats.style.Styler.to_typst "Link to this definition")

Write Styler to a file, buffer or string in Typst format.

Added in version 3.0.0.

Parameters:

**buf**str, path object, file-like object, optional

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a string `write()` function. If `None`, the result is returned as a string.

**encoding**str, optional

Character encoding setting for file output (and meta tags if available). Defaults to `pandas.options.styler.render.encoding` value of “utf-8”.

**sparse\_index**bool, optional

Whether to sparsify the display of a hierarchical index. Setting to False will display each explicit level element in a hierarchical key for each row. Defaults to `pandas.options.styler.sparse.index` value.

**sparse\_columns**bool, optional

Whether to sparsify the display of a hierarchical index. Setting to False will display each explicit level element in a hierarchical key for each column. Defaults to `pandas.options.styler.sparse.columns` value.

**max\_rows**int, optional

The maximum number of rows that will be rendered. Defaults to `pandas.options.styler.render.max_rows`, which is None.

**max\_columns**int, optional

The maximum number of columns that will be rendered. Defaults to `pandas.options.styler.render.max_columns`, which is None.

Rows and columns may be reduced if the number of total elements is large. This value is set to `pandas.options.styler.render.max_elements`, which is 262144 (18 bit browser rendering).

Returns:

str or None

If buf is None, returns the result as a string. Otherwise returns None.

See also

`DataFrame.to_typst`

Write a DataFrame to a file, buffer or string in Typst format.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> df.style.to\_typst()

Copy to clipboard

#table(
  columns: 3,
  \[\], \[A\], \[B\],

  \[0\], \[1\], \[3\],
  \[1\], \[2\], \[4\],
)

Copy to clipboard

On this page