[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.from_dict.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.from_dict.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.from_dict.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.from_dict.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.from_dict.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.from_dict.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.from_dict.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.from_dict.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.from_dict.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.from_dict.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.from_dict.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.from_dict.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.from\_dict[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas-dataframe-from-dict "Link to this heading")

===============================================================================================================================================================

classmethod DataFrame.from\_dict(_data_, _orient\='columns'_, _dtype\=None_, _columns\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1691-L1838)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "Link to this definition")

Construct DataFrame from dict of array-like or dicts.

Creates DataFrame object from dictionary by columns or by index allowing dtype specification.

Parameters:

**data**dict

Of the form {field : array-like} or {field : dict}.

Deprecated since version 3.1.0: Passing a non-dict to `from_dict` is deprecated. Use the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 constructor instead.

**orient**{‘columns’, ‘index’, ‘tight’}, default ‘columns’

The “orientation” of the data. If the keys of the passed dict should be the columns of the resulting DataFrame, pass ‘columns’ (default). Otherwise if the keys should be rows, pass ‘index’. If ‘tight’, assume a dict with keys \[‘index’, ‘columns’, ‘data’, ‘index\_names’, ‘column\_names’\].

**dtype**dtype, default None

Data type to force after DataFrame construction, otherwise infer.

**columns**list, default None

Column labels to use when `orient='index'`. Raises a ValueError if used with `orient='columns'` or `orient='tight'`.

Returns:

DataFrame

See also

[`DataFrame.from_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "pandas.DataFrame.from_records")

DataFrame from structured ndarray, sequence of tuples or dicts, or DataFrame.

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

DataFrame object creation using constructor.

[`DataFrame.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html#pandas.DataFrame.to_dict "pandas.DataFrame.to_dict")

Convert the DataFrame to a dictionary.

Examples

By default the keys of the dict become the DataFrame columns:

\>>> data \= {"col\_1": \[3, 2, 1, 0\], "col\_2": \["a", "b", "c", "d"\]}
\>>> pd.DataFrame.from\_dict(data)
   col\_1 col\_2
0      3     a
1      2     b
2      1     c
3      0     d

Copy to clipboard

Specify `orient='index'` to create the DataFrame using dictionary keys as rows:

\>>> data \= {"row\_1": \[3, 2, 1, 0\], "row\_2": \["a", "b", "c", "d"\]}
\>>> pd.DataFrame.from\_dict(data, orient\="index")
       0  1  2  3
row\_1  3  2  1  0
row\_2  a  b  c  d

Copy to clipboard

When using the ‘index’ orientation, the column names can be specified manually:

\>>> pd.DataFrame.from\_dict(data, orient\="index", columns\=\["A", "B", "C", "D"\])
       A  B  C  D
row\_1  3  2  1  0
row\_2  a  b  c  d

Copy to clipboard

Specify `orient='tight'` to create the DataFrame using a ‘tight’ format:

\>>> data \= {
...     "index": \[("a", "b"), ("a", "c")\],
...     "columns": \[("x", 1), ("y", 2)\],
...     "data": \[\[1, 3\], \[2, 4\]\],
...     "index\_names": \["n1", "n2"\],
...     "column\_names": \["z1", "z2"\],
... }
\>>> pd.DataFrame.from\_dict(data, orient\="tight")
z1     x  y
z2     1  2
n1 n2
a  b   1  3
   c   2  4

Copy to clipboard

On this page