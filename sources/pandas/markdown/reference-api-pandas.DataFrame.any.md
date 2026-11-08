[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.any.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.any.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.any.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.any.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.any.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.any.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.any.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.any.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.any.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.any.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.any.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.any.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.any[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#pandas-dataframe-any "Link to this heading")

============================================================================================================================================

DataFrame.any(_\*_, _axis\=0_, _bool\_only\=False_, _skipna\=True_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L17278-L17405)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#pandas.DataFrame.any "Link to this definition")

Return whether any element is True, potentially over an axis.

Returns False unless there is at least one element within a series or along a Dataframe axis that is True or equivalent (e.g. non-zero or non-empty).

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

Indicate which axis or axes should be reduced. For Series this parameter is unused and defaults to 0.

*   0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
    
*   1 / ‘columns’ : reduce the columns, return a Series whose index is the original index.
    
*   None : reduce all axes, return a scalar.
    

**bool\_only**bool, default False

Include only boolean columns. Not implemented for Series.

**skipna**bool, default True

Exclude NA/null values. If the entire row/column is NA and skipna is True, then the result will be False, as for an empty row/column. If skipna is False, NA values are treated as True for NumPy-backed dtypes (since they are not equal to zero). For nullable dtypes such as `boolean`, NA values propagate following [Kleene logic](https://pandas.pydata.org/docs/user_guide/boolean.html#boolean-kleene)
.

**\*\*kwargs**any, default None

Additional keywords have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series or scalar

If axis=None, then a scalar boolean is returned. Otherwise a Series is returned with index matching the index argument.

See also

[`numpy.any`](https://numpy.org/doc/stable/reference/generated/numpy.any.html#numpy.any "(in NumPy v2.5)")

Numpy version of this method.

[`Series.any`](https://pandas.pydata.org/docs/reference/api/pandas.Series.any.html#pandas.Series.any "pandas.Series.any")

Return whether any element is True.

[`Series.all`](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas.Series.all "pandas.Series.all")

Return whether all elements are True.

[`DataFrame.any`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#pandas.DataFrame.any "pandas.DataFrame.any")

Return whether any element is True over requested axis.

[`DataFrame.all`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html#pandas.DataFrame.all "pandas.DataFrame.all")

Return whether all elements are True over requested axis.

Examples

**Series**

For Series input, the output is a scalar indicating whether any element is True.

\>>> pd.Series(\[False, False\]).any()
False
\>>> pd.Series(\[True, False\]).any()
True
\>>> pd.Series(\[\], dtype\="float64").any()
False
\>>> pd.Series(\[np.nan\]).any()
False
\>>> pd.Series(\[np.nan\]).any(skipna\=False)
True

Copy to clipboard

**DataFrame**

Whether each column contains at least one True element (the default).

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[0, 2\], "C": \[0, 0\]})
\>>> df
   A  B  C
0  1  0  0
1  2  2  0

Copy to clipboard

\>>> df.any()
A     True
B     True
C    False
dtype: bool

Copy to clipboard

Aggregating over the columns.

\>>> df \= pd.DataFrame({"A": \[True, False\], "B": \[1, 2\]})
\>>> df
       A  B
0   True  1
1  False  2

Copy to clipboard

\>>> df.any(axis\="columns")
0    True
1    True
dtype: bool

Copy to clipboard

\>>> df \= pd.DataFrame({"A": \[True, False\], "B": \[1, 0\]})
\>>> df
       A  B
0   True  1
1  False  0

Copy to clipboard

\>>> df.any(axis\="columns")
0    True
1    False
dtype: bool

Copy to clipboard

Aggregating over the entire DataFrame with `axis=None`.

\>>> df.any(axis\=None)
True

Copy to clipboard

any for an empty DataFrame is an empty Series.

\>>> pd.DataFrame(\[\]).any()
Series(\[\], dtype: bool)

Copy to clipboard

On this page