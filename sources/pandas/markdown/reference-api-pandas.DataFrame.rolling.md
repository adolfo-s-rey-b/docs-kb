[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.rolling.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.rolling.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.rolling.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.rolling.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.rolling.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.rolling.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.rolling.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.rolling.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.rolling.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.rolling.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.rolling.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.rolling.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.rolling[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas-dataframe-rolling "Link to this heading")

========================================================================================================================================================

DataFrame.rolling(_window_, _min\_periods\=None_, _center\=False_, _win\_type\=None_, _on\=None_, _closed\=None_, _step\=None_, _method\='single'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L12136-L12451)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling "Link to this definition")

Provide rolling window calculations.

This method returns a rolling window object, enabling aggregation, transformation, and other operations over a sliding window of a specified size.

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

When `on` is specified, the values of that column also become the index of the [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 passed to `Rolling.apply()` when `raw=False`, in place of the original [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 index.

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
**step**int, default None\
\
Evaluate the window at every `step` result, equivalent to slicing as `[::step]`. `window` must be an integer. Using a step argument other than None or 1 will produce a result with a different shape than the input.\
\
**method**str {‘single’, ‘table’}, default ‘single’\
\
Execute the rolling operation per single column or row (`'single'`) or over the entire object (`'table'`).\
\
This argument is only implemented when specifying `engine='numba'` in the method call.\
\
Returns:\
\
pandas.api.typing.Window or pandas.api.typing.Rolling\
\
An instance of Window is returned if `win_type` is passed. Otherwise, an instance of Rolling is returned.\
\
See also\
\
[`expanding`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#pandas.DataFrame.expanding "pandas.DataFrame.expanding")\
\
Provides expanding transformations.\
\
[`ewm`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html#pandas.DataFrame.ewm "pandas.DataFrame.ewm")\
\
Provides exponential weighted functions.\
\
Notes\
\
See [Windowing Operations](https://pandas.pydata.org/docs/user_guide/window.html#window-generic)\
 for further usage details and examples.\
\
Examples\
\
\>>> df \= pd.DataFrame({"B": \[0, 1, 2, np.nan, 4\]})\
\>>> df\
     B\
0  0.0\
1  1.0\
2  2.0\
3  NaN\
4  4.0\
\
Copy to clipboard\
\
**window**\
\
Rolling sum with a window length of 2 observations.\
\
\>>> df.rolling(2).sum()\
     B\
0  NaN\
1  1.0\
2  3.0\
3  NaN\
4  NaN\
\
Copy to clipboard\
\
Rolling sum with a window span of 2 seconds.\
\
\>>> df\_time \= pd.DataFrame(\
...     {"B": \[0, 1, 2, np.nan, 4\]},\
...     index\=\[\
...         pd.Timestamp("20130101 09:00:00"),\
...         pd.Timestamp("20130101 09:00:02"),\
...         pd.Timestamp("20130101 09:00:03"),\
...         pd.Timestamp("20130101 09:00:05"),\
...         pd.Timestamp("20130101 09:00:06"),\
...     \],\
... )\
\
Copy to clipboard\
\
\>>> df\_time\
                       B\
2013-01-01 09:00:00  0.0\
2013-01-01 09:00:02  1.0\
2013-01-01 09:00:03  2.0\
2013-01-01 09:00:05  NaN\
2013-01-01 09:00:06  4.0\
\
Copy to clipboard\
\
\>>> df\_time.rolling("2s").sum()\
                       B\
2013-01-01 09:00:00  0.0\
2013-01-01 09:00:02  1.0\
2013-01-01 09:00:03  3.0\
2013-01-01 09:00:05  NaN\
2013-01-01 09:00:06  4.0\
\
Copy to clipboard\
\
Rolling sum with forward-looking windows with 3 seconds.\
\
\>>> df\_time.iloc\[::\-1\].rolling("3s").sum().iloc\[::\-1\]\
                       B\
2013-01-01 09:00:00  1.0\
2013-01-01 09:00:02  3.0\
2013-01-01 09:00:03  2.0\
2013-01-01 09:00:05  4.0\
2013-01-01 09:00:06  4.0\
\
Copy to clipboard\
\
Note\
\
Negative offset strings (e.g., `"-5h"`) do not create forward-looking windows and should be avoided. They collapse to single-element windows.\
\
Rolling sum with forward looking windows with 2 observations.\
\
\>>> indexer \= pd.api.indexers.FixedForwardWindowIndexer(window\_size\=2)\
\>>> df.rolling(window\=indexer, min\_periods\=1).sum()\
     B\
0  1.0\
1  3.0\
2  2.0\
3  4.0\
4  4.0\
\
Copy to clipboard\
\
**min\_periods**\
\
Rolling sum with a window length of 2 observations, but only needs a minimum of 1 observation to calculate a value.\
\
\>>> df.rolling(2, min\_periods\=1).sum()\
     B\
0  0.0\
1  1.0\
2  3.0\
3  2.0\
4  4.0\
\
Copy to clipboard\
\
**center**\
\
Rolling sum with the result assigned to the center of the window index.\
\
\>>> df.rolling(3, min\_periods\=1, center\=True).sum()\
     B\
0  1.0\
1  3.0\
2  3.0\
3  6.0\
4  4.0\
\
Copy to clipboard\
\
\>>> df.rolling(3, min\_periods\=1, center\=False).sum()\
     B\
0  0.0\
1  1.0\
2  3.0\
3  3.0\
4  6.0\
\
Copy to clipboard\
\
**step**\
\
Rolling sum with a window length of 2 observations, minimum of 1 observation to calculate a value, and a step of 2.\
\
\>>> df.rolling(2, min\_periods\=1, step\=2).sum()\
     B\
0  0.0\
2  3.0\
4  4.0\
\
Copy to clipboard\
\
**win\_type**\
\
Rolling sum with a window length of 2, using the Scipy `'gaussian'` window type. `std` is required in the aggregation function.\
\
\>>> df.rolling(2, win\_type\="gaussian").sum(std\=3)\
          B\
0        NaN\
1   0.986207\
2   2.958621\
3        NaN\
4        NaN\
\
Copy to clipboard\
\
**on**\
\
Rolling sum with a window length of 2 days.\
\
\>>> df \= pd.DataFrame(\
...     {\
...         "A": \[\
...             pd.to\_datetime("2020-01-01"),\
...             pd.to\_datetime("2020-01-01"),\
...             pd.to\_datetime("2020-01-02"),\
...         \],\
...         "B": \[1, 2, 3\],\
...     },\
...     index\=pd.date\_range("2020", periods\=3),\
... )\
\
Copy to clipboard\
\
\>>> df\
                    A  B\
2020-01-01 2020-01-01  1\
2020-01-02 2020-01-01  2\
2020-01-03 2020-01-02  3\
\
Copy to clipboard\
\
\>>> df.rolling("2D", on\="A").sum()\
                    A    B\
2020-01-01 2020-01-01  1.0\
2020-01-02 2020-01-01  3.0\
2020-01-03 2020-01-02  6.0\
\
Copy to clipboard\
\
On this page