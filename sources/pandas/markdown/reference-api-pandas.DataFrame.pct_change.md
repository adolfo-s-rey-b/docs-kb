[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.pct_change.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.pct_change.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.pct_change.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.pct_change.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.pct_change.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.pct_change.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.pct_change.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.pct_change.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.pct_change.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.pct_change.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.pct_change.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.pct_change.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.pct\_change[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html#pandas-dataframe-pct-change "Link to this heading")

==================================================================================================================================================================

DataFrame.pct\_change(_periods\=1_, _fill\_method\=None_, _freq\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L11616-L11762)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html#pandas.DataFrame.pct_change "Link to this definition")

Fractional change between the current and a prior element.

Computes the fractional change from the immediately previous row by default. This is useful in comparing the fraction of change in a time series of elements.

Note

Despite the name of this method, it calculates fractional change (also known as per unit change or relative change) and not percentage change. If you need the percentage change, multiply these values by 100.

Parameters:

**periods**int, default 1

Periods to shift for forming percent change.

**fill\_method**None

Must be None. This argument will be removed in a future version of pandas.

**freq**DateOffset, timedelta, or str, optional

Increment to use from time series API (e.g. ‘ME’ or BDay()).

**\*\*kwargs**

Additional keyword arguments are passed into DataFrame.shift or Series.shift.

Returns:

Series or DataFrame

The same type as the calling object.

See also

[`Series.diff`](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html#pandas.Series.diff "pandas.Series.diff")

Compute the difference of two elements in a Series.

[`DataFrame.diff`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html#pandas.DataFrame.diff "pandas.DataFrame.diff")

Compute the difference of two elements in a DataFrame.

[`Series.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html#pandas.Series.shift "pandas.Series.shift")

Shift the index by some number of periods.

[`DataFrame.shift`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html#pandas.DataFrame.shift "pandas.DataFrame.shift")

Shift the index by some number of periods.

Examples

**Series**

\>>> s \= pd.Series(\[90, 91, 85\])
\>>> s
0    90
1    91
2    85
dtype: int64

Copy to clipboard

\>>> s.pct\_change()
0         NaN
1    0.011111
2   -0.065934
dtype: float64

Copy to clipboard

\>>> s.pct\_change(periods\=2)
0         NaN
1         NaN
2   -0.055556
dtype: float64

Copy to clipboard

See the percentage change in a Series where filling NAs with last valid observation forward to next valid.

\>>> s \= pd.Series(\[90, 91, None, 85\])
\>>> s
0    90.0
1    91.0
2     NaN
3    85.0
dtype: float64

Copy to clipboard

\>>> s.ffill().pct\_change()
0         NaN
1    0.011111
2    0.000000
3   -0.065934
dtype: float64

Copy to clipboard

**DataFrame**

Percentage change in French franc, Deutsche Mark, and Italian lira from 1980-01-01 to 1980-03-01.

\>>> df \= pd.DataFrame(
...     {
...         "FR": \[4.0405, 4.0963, 4.3149\],
...         "GR": \[1.7246, 1.7482, 1.8519\],
...         "IT": \[804.74, 810.01, 860.13\],
...     },
...     index\=\["1980-01-01", "1980-02-01", "1980-03-01"\],
... )
\>>> df
                FR      GR      IT
1980-01-01  4.0405  1.7246  804.74
1980-02-01  4.0963  1.7482  810.01
1980-03-01  4.3149  1.8519  860.13

Copy to clipboard

\>>> df.pct\_change()
                  FR        GR        IT
1980-01-01       NaN       NaN       NaN
1980-02-01  0.013810  0.013684  0.006549
1980-03-01  0.053365  0.059318  0.061876

Copy to clipboard

Percentage of change in GOOG and APPL stock volume. Shows computing the percentage change between columns.

\>>> df \= pd.DataFrame(
...     {
...         "2016": \[1769950, 30586265\],
...         "2015": \[1500923, 40912316\],
...         "2014": \[1371819, 41403351\],
...     },
...     index\=\["GOOG", "APPL"\],
... )
\>>> df
          2016      2015      2014
GOOG   1769950   1500923   1371819
APPL  30586265  40912316  41403351

Copy to clipboard

\>>> df.pct\_change(axis\="columns", periods\=-1)
          2016      2015  2014
GOOG  0.179241  0.094112   NaN
APPL -0.252395 -0.011860   NaN

Copy to clipboard

On this page