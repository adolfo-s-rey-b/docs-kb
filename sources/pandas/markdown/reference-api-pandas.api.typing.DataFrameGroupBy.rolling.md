[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.DataFrameGroupBy.rolling[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html#pandas-api-typing-dataframegroupby-rolling "Link to this heading")

==============================================================================================================================================================================================================

DataFrameGroupBy.rolling(_window_, _min\_periods\=None_, _center\=False_, _win\_type\=None_, _on\=None_, _closed\=None_, _method\='single'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L3666-L3833)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html#pandas.api.typing.DataFrameGroupBy.rolling "Link to this definition")

Return a rolling grouper, providing rolling functionality per group.

Allows the application of rolling window operations (e.g., moving averages) independently within each group defined by the groupby keys.

Parameters:

**window**int, timedelta, str, offset, or BaseIndexer subclass

Interval of the moving window.

If an integer, the delta between the start and end of each window. The number of points in the window depends on the `closed` argument.

If a timedelta, str, or offset, the time period of each window. Each window will be a variable sized based on the observations included in the time-period. This is only valid for datetimelike indexes. The offset must correspond to a fixed frequency (for example, `'2D'` or `'1h'`); non-fixed frequencies such as `'B'` (business day) or `'ME'` (month end) are not supported and raise `ValueError`. To learn more about the offsets & frequency strings, please see [this link](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
.

If a BaseIndexer subclass, the window boundaries based on the defined `get_window_bounds` method. Additional rolling keyword arguments, namely `min_periods`, `center`, `closed` and `step` will be passed to `get_window_bounds`.

**min\_periods**int, default None

Minimum number of observations in window required to have a value; otherwise, result is `np.nan`.

For a window that is specified by an offset, `min_periods` will default to 1.

For a window that is specified by an integer, `min_periods` will default to the size of the window.

**center**bool, default False

If False, set the window labels as the right edge of the window index.

If True, set the window labels as the center of the window index.

**win\_type**str, default None

If `None`, all points are evenly weighted.

If a string, it must be a valid [scipy.signal window function](https://docs.scipy.org/doc/scipy/reference/signal.windows.html#module-scipy.signal.windows)
.

Certain Scipy window types require additional parameters to be passed in the aggregation function. The additional parameters must match the keywords specified in the Scipy window type method signature.

**on**str, optional

For a DataFrame, a column label or Index level on which to calculate the rolling window, rather than the DataFrame’s index.

For integer `window` values, the window bounds are based on the number of observations and are not calculated using the values of the `on` column. The `on` column is excluded from the aggregation, but is included in the result when its values differ from the object’s index.

**closed**str, default None

Determines the inclusivity of points in the window

If `'right'`, uses the window (first, last\] meaning the last point is included in the calculations.

If `'left'`, uses the window \[first, last) meaning the first point is included in the calculations.\
\
If `'both'`, uses the window \[first, last\] meaning all points in the window are included in the calculations.\
\
If `'neither'`, uses the window (first, last) meaning the first and last points in the window are excluded from calculations.\
\
() and \[\] are referencing open and closed set notation respetively.\
\
Default `None` (`'right'`).\
\
**method**str {‘single’, ‘table’}, default ‘single’\
\
Execute the rolling operation per single column or row (`'single'`) or over the entire object (`'table'`).\
\
This argument is only implemented when specifying `engine='numba'` in the method call.\
\
Returns:\
\
pandas.api.typing.RollingGroupBy\
\
Return a new grouper with our rolling appended.\
\
See also\
\
`Series.rolling`\
\
Calling object with Series data.\
\
`DataFrame.rolling`\
\
Calling object with DataFrames.\
\
`Series.groupby`\
\
Apply a function groupby to a Series.\
\
`DataFrame.groupby`\
\
Apply a function groupby.\
\
Examples\
\
\>>> df \= pd.DataFrame(\
...     {\
...         "A": \[1, 1, 2, 2\],\
...         "B": \[1, 2, 3, 4\],\
...         "C": \[0.362, 0.227, 1.267, \-0.562\],\
...     }\
... )\
\>>> df\
      A  B      C\
0     1  1  0.362\
1     1  2  0.227\
2     2  3  1.267\
3     2  4 -0.562\
\
Copy to clipboard\
\
\>>> df.groupby("A").rolling(2).sum()\
    B      C\
A\
1 0  NaN    NaN\
  1  3.0  0.589\
2 2  NaN    NaN\
  3  7.0  0.705\
\
Copy to clipboard\
\
\>>> df.groupby("A").rolling(2, min\_periods\=1).sum()\
    B      C\
A\
1 0  1.0  0.362\
  1  3.0  0.589\
2 2  3.0  1.267\
  3  7.0  0.705\
\
Copy to clipboard\
\
\>>> df.groupby("A").rolling(2, on\="B").sum()\
    B      C\
A\
1 0  1    NaN\
  1  2  0.589\
2 2  3    NaN\
  3  4  0.705\
\
Copy to clipboard\
\
On this page