[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.unstack[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas-dataframe-unstack "Link to this heading")

========================================================================================================================================================

DataFrame.unstack(_level\=\-1_, _fill\_value\=None_, _sort\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L14526-L14600)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "Link to this definition")

Pivot a level of the (necessarily hierarchical) index labels.

Returns a DataFrame having a new level of column labels whose inner-most level consists of the pivoted index labels.

If the index is not a MultiIndex, the output will be a Series (the analogue of stack when the columns are not a MultiIndex).

Parameters:

**level**int, str, or list of these, default -1 (last level)

Level(s) of index to unstack, can pass level name.

**fill\_value**scalar

Replace NaN with this value if the unstack produces missing values.

**sort**bool, default True

Sort the level(s) in the resulting MultiIndex columns. This also orders the rows of the result: sorted by the remaining levels if `True`, in order of first appearance if `False`.

Returns:

Series or DataFrame

If index is a MultiIndex: DataFrame with pivoted index labels as new inner-most level column labels, else Series.

See also

[`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")

Pivot a table based on column values.

[`DataFrame.stack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "pandas.DataFrame.stack")

Pivot a level of the column labels (inverse operation from unstack).

Notes

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-stacking)
 for more examples.

Examples

\>>> index \= pd.MultiIndex.from\_tuples(
...     \[("one", "a"), ("one", "b"), ("two", "a"), ("two", "b")\]
... )
\>>> s \= pd.Series(np.arange(1.0, 5.0), index\=index)
\>>> s
one  a   1.0
     b   2.0
two  a   3.0
     b   4.0
dtype: float64

Copy to clipboard

\>>> s.unstack(level\=-1)
     a   b
one  1.0  2.0
two  3.0  4.0

Copy to clipboard

\>>> s.unstack(level\=0)
   one  two
a  1.0   3.0
b  2.0   4.0

Copy to clipboard

\>>> df \= s.unstack(level\=0)
\>>> df.unstack()
one  a  1.0
     b  2.0
two  a  3.0
     b  4.0
dtype: float64

Copy to clipboard

On this page