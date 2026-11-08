[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.skew[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html#pandas-dataframe-skew "Link to this heading")

===============================================================================================================================================

DataFrame.skew(_\*_, _axis\=0_, _skipna\=True_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L18598-L18686)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html#pandas.DataFrame.skew "Link to this definition")

Return unbiased skew over requested axis.

Normalized by N-1.

Parameters:

**axis**{index (0), columns (1)}, default 0

Axis for the function to be applied on. For Series this parameter is unused and defaults to 0.

For DataFrames, specifying `axis=None` will apply the aggregation across both axes.

Added in version 2.0.0.

**skipna**bool, default True

Exclude NA/null values when computing the result.

**numeric\_only**bool, default False

Include only float, int, boolean columns.

**\*\*kwargs**

Additional keyword arguments have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series or scalar

Unbiased skew over requested axis.

See also

[`DataFrame.kurt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurt.html#pandas.DataFrame.kurt "pandas.DataFrame.kurt")

Returns unbiased kurtosis over requested axis.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> s.skew()
0.0

Copy to clipboard

With a DataFrame

\>>> df \= pd.DataFrame(
...     {"a": \[1, 2, 3\], "b": \[2, 3, 4\], "c": \[1, 3, 5\]},
...     index\=\["tiger", "zebra", "cow"\],
... )
\>>> df
        a   b   c
tiger   1   2   1
zebra   2   3   3
cow     3   4   5
\>>> df.skew()
a   0.0
b   0.0
c   0.0
dtype: float64

Copy to clipboard

Using axis=1

\>>> df.skew(axis\=1)
tiger   1.732051
zebra  -1.732051
cow     0.000000
dtype: float64

Copy to clipboard

In this case, numeric\_only should be set to True to avoid getting an error.

\>>> df \= pd.DataFrame(
...     {"a": \[1, 2, 3\], "b": \["T", "Z", "X"\]}, index\=\["tiger", "zebra", "cow"\]
... )
\>>> df.skew(numeric\_only\=True)
a   0.0
dtype: float64

Copy to clipboard

On this page