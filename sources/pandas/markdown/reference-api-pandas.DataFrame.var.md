[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.var.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.var.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.var.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.var.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.var.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.var.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.var.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.var.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.var.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.var.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.var.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.var.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.var[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html#pandas-dataframe-var "Link to this heading")

============================================================================================================================================

DataFrame.var(_\*_, _axis\=0_, _skipna\=True_, _ddof\=1_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L18353-L18437)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html#pandas.DataFrame.var "Link to this definition")

Return unbiased variance over requested axis.

Normalized by N-1 by default. This can be changed using the ddof argument.

Parameters:

**axis**{index (0), columns (1)}, default 0

Axis for the function to be applied on. For Series this parameter is unused and defaults to 0.

Warning

The behavior of DataFrame.var with `axis=None` is deprecated, in a future version this will reduce over both axes and return a scalar To retain the old behavior, pass axis=0 (or do not pass axis).

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

**numeric\_only**bool, default False

Include only float, int, boolean columns. Not implemented for Series.

**\*\*kwargs**

Additional keywords passed.

Returns:

Series or scalar

Unbiased variance over requested axis.

See also

[`numpy.var`](https://numpy.org/doc/stable/reference/generated/numpy.var.html#numpy.var "(in NumPy v2.5)")

Equivalent function in NumPy.

[`Series.var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")

Return unbiased variance over Series values.

[`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")

Return standard deviation over Series values.

[`DataFrame.std`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std "pandas.DataFrame.std")

Return standard deviation of the values over the requested axis.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "person\_id": \[0, 1, 2, 3\],
...         "age": \[21, 25, 62, 43\],
...         "height": \[1.61, 1.87, 1.49, 2.01\],
...     }
... ).set\_index("person\_id")
\>>> df
           age  height
person\_id
0           21    1.61
1           25    1.87
2           62    1.49
3           43    2.01

Copy to clipboard

\>>> df.var()
age       352.916667
height      0.056367
dtype: float64

Copy to clipboard

Alternatively, `ddof=0` can be set to normalize by N instead of N-1:

\>>> df.var(ddof\=0)
age       264.687500
height      0.042275
dtype: float64

Copy to clipboard

On this page