[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.stack.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.stack.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.stack.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.stack.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.stack.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.stack.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.stack.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.stack.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.stack.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.stack.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.stack.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.stack.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.stack[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas-dataframe-stack "Link to this heading")

==================================================================================================================================================

DataFrame.stack(_level\=\-1_, _dropna\=<no\_default>_, _sort\=<no\_default>_, _future\_stack\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L14177-L14392)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "Link to this definition")

Stack the prescribed level(s) from columns to index.

Return a reshaped DataFrame or Series having a multi-level index with one or more new inner-most levels compared to the current DataFrame. The new inner-most levels are created by pivoting the columns of the current dataframe:

*   if the columns have a single level, the output is a Series;
    
*   if the columns have multiple levels, the new index level(s) is (are) taken from the prescribed level(s) and the output is a DataFrame.
    

Parameters:

**level**int, str, list, default -1

Level(s) to stack from the column axis onto the index axis, defined as one index or label, or a list of indices or labels.

**dropna**bool, default True

Whether to drop rows in the resulting Frame/Series with missing values. Stacking a column level onto the index axis can create combinations of index and column values that are missing from the original dataframe. See Examples section.

Deprecated since version 3.0: This parameter is deprecated and will be removed in a future version of pandas.

**sort**bool, default True

Whether to sort the levels of the resulting MultiIndex.

Deprecated since version 3.0: This parameter is deprecated and will be removed in a future version of pandas.

**future\_stack**bool, default True

Whether to use the new stack implementation. This is the default as of pandas 3.0. When True, dropna and sort have no impact on the result and must remain unspecified. See [pandas 2.1.0 Release notes](https://pandas.pydata.org/docs/whatsnew/v2.1.0.html#whatsnew-210-enhancements-new-stack)
 for more details.

Deprecated since version 3.0: This parameter is deprecated and will be removed in a future version of pandas.

Returns:

DataFrame or Series

Stacked dataframe or series.

See also

[`DataFrame.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")

Unstack prescribed level(s) from index axis onto column axis.

[`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")

Reshape dataframe from long format to wide format.

[`DataFrame.pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")

Create a spreadsheet-style pivot table as a DataFrame.

Notes

The function is named by analogy with a collection of books being reorganized from being side-by-side horizontally (the columns of the DataFrame) to being stacked vertically on top of each other (in the index of the DataFrame).

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-stacking)
 for more examples.

Examples

**Single level columns**

\>>> df\_single\_level\_cols \= pd.DataFrame(
...     \[\[0, 1\], \[2, 3\]\], index\=\["cat", "dog"\], columns\=\["weight", "height"\]
... )

Copy to clipboard

Stacking a dataframe with a single level column axis returns a Series:

\>>> df\_single\_level\_cols
     weight height
cat       0      1
dog       2      3
\>>> df\_single\_level\_cols.stack()
cat  weight    0
     height    1
dog  weight    2
     height    3
dtype: int64

Copy to clipboard

**Multi level columns: simple case**

\>>> multicol1 \= pd.MultiIndex.from\_tuples(
...     \[("weight", "kg"), ("weight", "pounds")\]
... )
\>>> df\_multi\_level\_cols1 \= pd.DataFrame(
...     \[\[1, 2\], \[2, 4\]\], index\=\["cat", "dog"\], columns\=multicol1
... )

Copy to clipboard

Stacking a dataframe with a multi-level column axis:

\>>> df\_multi\_level\_cols1
     weight
         kg    pounds
cat       1        2
dog       2        4
\>>> df\_multi\_level\_cols1.stack()
            weight
cat kg           1
    pounds       2
dog kg           2
    pounds       4

Copy to clipboard

**Missing values**

\>>> multicol2 \= pd.MultiIndex.from\_tuples(\[("weight", "kg"), ("height", "m")\])
\>>> df\_multi\_level\_cols2 \= pd.DataFrame(
...     \[\[1.0, 2.0\], \[3.0, 4.0\]\], index\=\["cat", "dog"\], columns\=multicol2
... )

Copy to clipboard

It is common to have missing values when stacking a dataframe with multi-level columns, as the stacked dataframe typically has more values than the original dataframe. Missing values are filled with NaNs:

\>>> df\_multi\_level\_cols2
    weight height
        kg      m
cat    1.0    2.0
dog    3.0    4.0
\>>> df\_multi\_level\_cols2.stack()
        weight  height
cat kg     1.0     NaN
    m      NaN     2.0
dog kg     3.0     NaN
    m      NaN     4.0

Copy to clipboard

**Prescribing the level(s) to be stacked**

The first parameter controls which level or levels are stacked:

\>>> df\_multi\_level\_cols2.stack(0)
             kg    m
cat weight  1.0  NaN
    height  NaN  2.0
dog weight  3.0  NaN
    height  NaN  4.0
\>>> df\_multi\_level\_cols2.stack(\[0, 1\])
cat  weight  kg    1.0
     height  m     2.0
dog  weight  kg    3.0
     height  m     4.0
dtype: float64

Copy to clipboard

On this page