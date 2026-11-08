[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.unstack.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.unstack.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.unstack.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.unstack.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.unstack.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.unstack.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.unstack.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.unstack.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.unstack.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.unstack.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.unstack.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.unstack.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.unstack[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html#pandas-series-unstack "Link to this heading")

===============================================================================================================================================

Series.unstack(_level\=\-1_, _fill\_value\=None_, _sort\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L4952-L5013)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html#pandas.Series.unstack "Link to this definition")

Unstack, also known as pivot, Series with MultiIndex to produce DataFrame.

This method pivots a level of the MultiIndex labels, reshaping the Series into a DataFrame where the unstacked level becomes the columns.

Parameters:

**level**int, str, or list of these, default last level

Level(s) to unstack, can pass level name.

**fill\_value**scalar value, default None

Value to use when replacing NaN values.

**sort**bool, default True

Sort the level(s) in the resulting MultiIndex columns. This also orders the rows of the result: sorted by the remaining levels if `True`, in order of first appearance if `False`.

Returns:

DataFrame

Unstacked Series.

See also

[`DataFrame.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")

Pivot the MultiIndex of a DataFrame.

Notes

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-stacking)
 for more examples.

Examples

\>>> s \= pd.Series(
...     \[1, 2, 3, 4\],
...     index\=pd.MultiIndex.from\_product(\[\["one", "two"\], \["a", "b"\]\]),
... )
\>>> s
one  a    1
     b    2
two  a    3
     b    4
dtype: int64

Copy to clipboard

\>>> s.unstack(level\=-1)
     a  b
one  1  2
two  3  4

Copy to clipboard

\>>> s.unstack(level\=0)
   one  two
a    1    3
b    2    4

Copy to clipboard

On this page