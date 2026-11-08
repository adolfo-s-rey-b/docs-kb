[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_records.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_records.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_records.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_records.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_records.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_records.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_records.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_records.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_records.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_records.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_records.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_records.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_records.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_records.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_records[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_records.html#pandas-dataframe-to-records "Link to this heading")

==================================================================================================================================================================

DataFrame.to\_records(_index\=True_, _column\_dtypes\=None_, _index\_dtypes\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L2296-L2457)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_records.html#pandas.DataFrame.to_records "Link to this definition")

Convert DataFrame to a NumPy record array.

Index will be included as the first field of the record array if requested.

Parameters:

**index**bool, default True

Include index in resulting record array, stored in ‘index’ field or using the index label, if set.

**column\_dtypes**str, type, dict, default None

If a string or type, the data type to store all columns. If a dictionary, a mapping of column names and indices (zero-indexed) to specific data types.

**index\_dtypes**str, type, dict, default None

If a string or type, the data type to store all index levels. If a dictionary, a mapping of index level names and indices (zero-indexed) to specific data types.

This mapping is applied only if index=True.

Returns:

numpy.rec.recarray

NumPy ndarray with the DataFrame labels as fields and each row of the DataFrame as entries.

See also

[`DataFrame.from_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "pandas.DataFrame.from_records")

Convert structured or record ndarray to DataFrame.

[`numpy.rec.recarray`](https://numpy.org/doc/stable/reference/generated/numpy.recarray.html#numpy.recarray "(in NumPy v2.5)")

An ndarray that allows field access using attributes, analogous to typed columns in a spreadsheet.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[0.5, 0.75\]}, index\=\["a", "b"\])
\>>> df
   A     B
a  1  0.50
b  2  0.75
\>>> df.to\_records()
rec.array(\[('a', 1, 0.5 ), ('b', 2, 0.75)\],
          dtype=\[('index', 'O'), ('A', '<i8'), ('B', '<f8')\])

Copy to clipboard

If the DataFrame index has no label then the recarray field name is set to ‘index’. If the index has a label then this is used as the field name:

\>>> df.index \= df.index.rename("I")
\>>> df.to\_records()
rec.array(\[('a', 1, 0.5 ), ('b', 2, 0.75)\],
          dtype=\[('I', 'O'), ('A', '<i8'), ('B', '<f8')\])

Copy to clipboard

The index can be excluded from the record array:

\>>> df.to\_records(index\=False)
rec.array(\[(1, 0.5 ), (2, 0.75)\],
          dtype=\[('A', '<i8'), ('B', '<f8')\])

Copy to clipboard

Data types can be specified for the columns:

\>>> df.to\_records(column\_dtypes\={"A": "int32"})
rec.array(\[('a', 1, 0.5 ), ('b', 2, 0.75)\],
          dtype=\[('I', 'O'), ('A', '<i4'), ('B', '<f8')\])

Copy to clipboard

As well as for the index:

\>>> df.to\_records(index\_dtypes\="<S2")
rec.array(\[(b'a', 1, 0.5 ), (b'b', 2, 0.75)\],
          dtype=\[('I', 'S2'), ('A', '<i8'), ('B', '<f8')\])

Copy to clipboard

\>>> index\_dtypes \= f"<S{df.index.str.len().max()}"
\>>> df.to\_records(index\_dtypes\=index\_dtypes)
rec.array(\[(b'a', 1, 0.5 ), (b'b', 2, 0.75)\],
          dtype=\[('I', 'S1'), ('A', '<i8'), ('B', '<f8')\])

Copy to clipboard

On this page