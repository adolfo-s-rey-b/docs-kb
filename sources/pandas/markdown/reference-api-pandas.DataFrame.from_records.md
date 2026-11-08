[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.from_records.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.from_records.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.from_records.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.from_records.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.from_records.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.from_records.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.from_records.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.from_records.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.from_records.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.from_records.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.from_records.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.from_records.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.from\_records[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas-dataframe-from-records "Link to this heading")

========================================================================================================================================================================

classmethod DataFrame.from\_records(_data_, _index\=None_, _exclude\=None_, _columns\=None_, _coerce\_float\=False_, _nrows\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L2058-L2294)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "Link to this definition")

Convert structured or record ndarray to DataFrame.

Creates a DataFrame object from a structured ndarray, or iterable of tuples or dicts.

Parameters:

**data**structured ndarray, iterable of tuples or dicts, or dict

Structured input data.

Deprecated since version 3.1.0: Passing a dict is deprecated. Use the DataFrame constructor or [`DataFrame.from_dict()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "pandas.DataFrame.from_dict")
 instead.

**index**str, list of fields, array-like

Field of array to use as the index, alternately a specific set of input labels to use.

**exclude**sequence, default None

Columns or fields to exclude.

**columns**sequence, default None

Column names to use. If the passed data do not have names associated with them, this argument provides names for the columns. Otherwise, this argument indicates the order of the columns in the result (any names not found in the data will become all-NA columns) and limits the data to these columns if not all column names are provided.

**coerce\_float**bool, default False

Attempt to convert values of non-string, non-numeric objects (like decimal.Decimal) to floating point, useful for SQL result sets.

**nrows**int, default None

Number of rows to read if data is an iterator.

Returns:

DataFrame

See also

[`DataFrame.from_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "pandas.DataFrame.from_dict")

DataFrame from dict of array-like or dicts.

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

DataFrame object creation using constructor.

Examples

Data can be provided as a structured ndarray:

\>>> data \= np.array(
...     \[(3, "a"), (2, "b"), (1, "c"), (0, "d")\],
...     dtype\=\[("col\_1", "i4"), ("col\_2", "U1")\],
... )
\>>> pd.DataFrame.from\_records(data)
   col\_1 col\_2
0      3     a
1      2     b
2      1     c
3      0     d

Copy to clipboard

Data can be provided as a list of dicts:

\>>> data \= \[\
...     {"col\_1": 3, "col\_2": "a"},\
...     {"col\_1": 2, "col\_2": "b"},\
...     {"col\_1": 1, "col\_2": "c"},\
...     {"col\_1": 0, "col\_2": "d"},\
... \]
\>>> pd.DataFrame.from\_records(data)
   col\_1 col\_2
0      3     a
1      2     b
2      1     c
3      0     d

Copy to clipboard

Data can be provided as a list of tuples with corresponding columns:

\>>> data \= \[(3, "a"), (2, "b"), (1, "c"), (0, "d")\]
\>>> pd.DataFrame.from\_records(data, columns\=\["col\_1", "col\_2"\])
   col\_1 col\_2
0      3     a
1      2     b
2      1     c
3      0     d

Copy to clipboard

On this page