[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.to_frame.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.to_frame.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.to_frame.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.to_frame.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.to_frame.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.to_frame.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.to_frame.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.to_frame.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.to_frame.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.to_frame.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.to_frame.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.to_frame.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.to\_frame[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html#pandas-multiindex-to-frame "Link to this heading")

===============================================================================================================================================================

MultiIndex.to\_frame(_index\=True_, _name\=<no\_default>_, _allow\_duplicates\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L2189-L2276)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html#pandas.MultiIndex.to_frame "Link to this definition")

Create a DataFrame with the levels of the MultiIndex as columns.

Column ordering is determined by the DataFrame constructor with data as a dict.

Parameters:

**index**bool, default True

Set the index of the returned DataFrame as the original MultiIndex.

**name**list / sequence of str, optional

The passed names should substitute index level names.

**allow\_duplicates**bool, optional default False

Allow duplicate column labels to be created.

Returns:

DataFrame

DataFrame representation of the MultiIndex, with levels as columns.

See also

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

Examples

\>>> mi \= pd.MultiIndex.from\_arrays(\[\["a", "b"\], \["c", "d"\]\])
\>>> mi
MultiIndex(\[('a', 'c'),\
            ('b', 'd')\],
           )

Copy to clipboard

\>>> df \= mi.to\_frame()
\>>> df
     0  1
a c  a  c
b d  b  d

Copy to clipboard

\>>> df \= mi.to\_frame(index\=False)
\>>> df
   0  1
0  a  c
1  b  d

Copy to clipboard

\>>> df \= mi.to\_frame(name\=\["x", "y"\])
\>>> df
     x  y
a c  a  c
b d  b  d

Copy to clipboard

On this page