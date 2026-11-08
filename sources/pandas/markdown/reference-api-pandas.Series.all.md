[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.all.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.all.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.all.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.all.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.all.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.all.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.all.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.all.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.all.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.all.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.all.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.all.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.all[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas-series-all "Link to this heading")

===================================================================================================================================

Series.all(_\*_, _axis\=0_, _bool\_only\=False_, _skipna\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L9199-L9303)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas.Series.all "Link to this definition")

Return whether all elements are True, potentially over an axis.

Returns True unless there at least one element within a series or along a Dataframe axis that is False or equivalent (e.g. zero or empty).

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

Indicate which axis or axes should be reduced. For Series this parameter is unused and defaults to 0.

*   0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
    
*   1 / ‘columns’ : reduce the columns, return a Series whose index is the original index.
    
*   None : reduce all axes, return a scalar.
    

**bool\_only**bool, default False

Include only boolean columns. Not implemented for Series.

**skipna**bool, default True

Exclude NA/null values. If the entire row/column is NA and skipna is True, then the result will be True, as for an empty row/column. If skipna is False, NA values are treated as True for NumPy-backed dtypes (since they are not equal to zero). For nullable dtypes such as `boolean`, NA values propagate following [Kleene logic](https://pandas.pydata.org/docs/user_guide/boolean.html#boolean-kleene)
.

**\*\*kwargs**any, default None

Additional keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series or scalar

If axis=None, then a scalar boolean is returned. Otherwise a Series is returned with index matching the index argument.

See also

[`Series.all`](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas.Series.all "pandas.Series.all")

Return True if all elements are True.

[`DataFrame.any`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#pandas.DataFrame.any "pandas.DataFrame.any")

Return True if one (or more) elements are True.

Examples

**Series**

\>>> pd.Series(\[True, True\]).all()
True
\>>> pd.Series(\[True, False\]).all()
False
\>>> pd.Series(\[\], dtype\="float64").all()
True
\>>> pd.Series(\[np.nan\]).all()
True
\>>> pd.Series(\[np.nan\]).all(skipna\=False)
True

Copy to clipboard

**DataFrames**

Create a DataFrame from a dictionary.

\>>> df \= pd.DataFrame({"col1": \[True, True\], "col2": \[True, False\]})
\>>> df
   col1   col2
0  True   True
1  True  False

Copy to clipboard

Default behaviour checks if values in each column all return True.

\>>> df.all()
col1     True
col2    False
dtype: bool

Copy to clipboard

Specify `axis='columns'` to check if values in each row all return True.

\>>> df.all(axis\="columns")
0     True
1    False
dtype: bool

Copy to clipboard

Or `axis=None` for whether every value is True.

\>>> df.all(axis\=None)
False

Copy to clipboard

On this page