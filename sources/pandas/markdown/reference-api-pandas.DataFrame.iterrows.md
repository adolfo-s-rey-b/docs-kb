[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.iterrows.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.iterrows.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.iterrows.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.iterrows.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.iterrows.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.iterrows.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.iterrows.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.iterrows.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.iterrows.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.iterrows.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.iterrows.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.iterrows.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.iterrows[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas-dataframe-iterrows "Link to this heading")

===========================================================================================================================================================

DataFrame.iterrows()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1318-L1374)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows "Link to this definition")

Iterate over DataFrame rows as (index, Series) pairs.

Each row is yielded as a (index, Series) tuple; the Series has the same index as the DataFrame columns. Note that dtypes may not be preserved across rows. Prefer [`itertuples()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "pandas.DataFrame.itertuples")
 for speed and type consistency.

Yields:

**index**label or tuple of label

The index of the row. A tuple for a MultiIndex.

**data**Series

The data of the row as a Series.

See also

[`DataFrame.itertuples`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "pandas.DataFrame.itertuples")

Iterate over DataFrame rows as namedtuples of the values.

[`DataFrame.items`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#pandas.DataFrame.items "pandas.DataFrame.items")

Iterate over (column name, Series) pairs.

Notes

1.  Because `iterrows` returns a Series for each row, it does **not** preserve dtypes across the rows (dtypes are preserved across columns for DataFrames).
    
    To preserve dtypes while iterating over the rows, it is better to use [`itertuples()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "pandas.DataFrame.itertuples")
     which returns namedtuples of the values and which is generally faster than `iterrows`.
    
2.  You should **never modify** something you are iterating over. This is not guaranteed to work in all cases. Depending on the data types, the iterator returns a copy and not a view, and writing to it will have no effect.
    

Examples

\>>> df \= pd.DataFrame(\[\[1, 1.5\]\], columns\=\["int", "float"\])
\>>> row \= next(df.iterrows())\[1\]
\>>> row
int      1.0
float    1.5
Name: 0, dtype: float64
\>>> print(row.dtype)
float64
\>>> print(df\["int"\].dtype)
int64

Copy to clipboard

On this page