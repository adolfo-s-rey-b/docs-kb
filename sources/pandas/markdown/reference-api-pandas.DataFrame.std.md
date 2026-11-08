[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.std.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.std.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.std.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.std.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.std.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.std.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.std.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.std.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.std.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.std.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.std.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.std.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.std[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas-dataframe-std "Link to this heading")

============================================================================================================================================

DataFrame.std(_\*_, _axis\=0_, _skipna\=True_, _ddof\=1_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L18473-L18565)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std "Link to this definition")

Return sample standard deviation over requested axis.

Normalized by N-1 by default. This can be changed using the ddof argument.

Parameters:

**axis**{index (0), columns (1)}, default 0

Axis for the function to be applied on. For Series this parameter is unused and defaults to 0.

Warning

The behavior of DataFrame.std with `axis=None` is deprecated, in a future version this will reduce over both axes and return a scalar To retain the old behavior, pass axis=0 (or do not pass axis).

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

**numeric\_only**bool, default False

Include only float, int, boolean columns. Not implemented for Series.

**\*\*kwargs**dict

Additional keyword arguments have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

Series or scalar

Standard deviation over requested axis.

See also

[`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")

Return standard deviation over Series values.

[`DataFrame.mean`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html#pandas.DataFrame.mean "pandas.DataFrame.mean")

Return the mean of the values over the requested axis.

[`DataFrame.median`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html#pandas.DataFrame.median "pandas.DataFrame.median")

Return the median of the values over the requested axis.

[`DataFrame.mode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#pandas.DataFrame.mode "pandas.DataFrame.mode")

Get the mode(s) of each element along the requested axis.

[`DataFrame.sum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#pandas.DataFrame.sum "pandas.DataFrame.sum")

Return the sum of the values over the requested axis.

Notes

To have the same behaviour as `numpy.std`, use `ddof=0` (instead of the default `ddof=1`) and `skipna=False`.

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

The standard deviation of the columns can be found as follows:

\>>> df.std()
age       18.786076
height     0.237417
dtype: float64

Copy to clipboard

Alternatively, ddof=0 can be set to normalize by N instead of N-1:

\>>> df.std(ddof\=0)
age       16.269219
height     0.205609
dtype: float64

Copy to clipboard

On this page