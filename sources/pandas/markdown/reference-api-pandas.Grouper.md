[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Grouper.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Grouper.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Grouper.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Grouper.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Grouper.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Grouper.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Grouper.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Grouper.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Grouper.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Grouper.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Grouper.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Grouper.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Grouper[#](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html#pandas-grouper "Link to this heading")

==========================================================================================================================

class pandas.Grouper(_\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/grouper.py#L75-L415)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html#pandas.Grouper "Link to this definition")

A Grouper allows the user to specify a groupby instruction for an object.

This specification will select a column via the key parameter, or if the level parameter is given, a level of the index of the target object.

If `level` is passed as a keyword to both Grouper and groupby, the values passed to Grouper take precedence.

Parameters:

**\*args**

Currently unused, reserved for future use.

**\*\*kwargs**

Dictionary of the keyword arguments to pass to Grouper.

Attributes

|     |     |
| --- | --- |
| **key** | (str, defaults to None) Groupby key, which selects the grouping column of the target. |
| **level** | (name/number, defaults to None) The level for the target index. |
| **freq** | (str / frequency object, defaults to None) This will groupby the specified frequency if the target selection (via key or level) is a datetime-like object. For full specification of available frequencies, please see [here](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)<br>. |
| **sort** | (bool, default False) Whether to sort the resulting labels. |
| **closed** | ({‘left’ or ‘right’}) Closed end of interval. Only when freq parameter is passed. |
| **label** | ({‘left’ or ‘right’}) Interval boundary to use for labeling. Only when freq parameter is passed. |
| **convention** | ({‘start’, ‘end’, ‘e’, ‘s’}) If grouper is PeriodIndex and freq parameter is passed. |
| **origin** | (Timestamp or str, default ‘start\_day’) The timestamp on which to adjust the grouping. The timezone of origin must match the timezone of the index. If string, must be one of the following: - ‘epoch’: origin is 1970-01-01 - ‘start’: origin is the first value of the timeseries - ‘start\_day’: origin is the first day at midnight of the timeseries - ‘end’: origin is the last value of the timeseries - ‘end\_day’: origin is the ceiling midnight of the last day |
| **offset** | (Timedelta or str, default None) An offset timedelta added to the origin. |
| **dropna** | (bool, default True) If True, and if group keys contain NA values, NA values together with row/column will be dropped. If False, NA values will also be treated as the key in groups. |

Returns:

Grouper or pandas.api.typing.TimeGrouper

A TimeGrouper is returned if `freq` is not `None`. Otherwise, a Grouper is returned.

See also

[`Series.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html#pandas.Series.groupby "pandas.Series.groupby")

Apply a function groupby to a Series.

[`DataFrame.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")

Apply a function groupby.

Examples

`df.groupby(pd.Grouper(key="Animal"))` is equivalent to `df.groupby('Animal')`

\>>> df \= pd.DataFrame(
...     {
...         "Animal": \["Falcon", "Parrot", "Falcon", "Falcon", "Parrot"\],
...         "Speed": \[100, 5, 200, 300, 15\],
...     }
... )
\>>> df
   Animal  Speed
0  Falcon    100
1  Parrot      5
2  Falcon    200
3  Falcon    300
4  Parrot     15
\>>> df.groupby(pd.Grouper(key\="Animal")).mean()
        Speed
Animal
Falcon  200.0
Parrot   10.0

Copy to clipboard

Specify a resample operation on the column ‘Publish date’

\>>> df \= pd.DataFrame(
...     {
...         "Publish date": \[\
...             pd.Timestamp("2000-01-02"),\
...             pd.Timestamp("2000-01-02"),\
...             pd.Timestamp("2000-01-09"),\
...             pd.Timestamp("2000-01-16"),\
...         \],
...         "ID": \[0, 1, 2, 3\],
...         "Price": \[10, 20, 30, 40\],
...     }
... )
\>>> df
  Publish date  ID  Price
0   2000-01-02   0     10
1   2000-01-02   1     20
2   2000-01-09   2     30
3   2000-01-16   3     40
\>>> df.groupby(pd.Grouper(key\="Publish date", freq\="1W")).mean()
               ID  Price
Publish date
2000-01-02    0.5   15.0
2000-01-09    2.0   30.0
2000-01-16    3.0   40.0

Copy to clipboard

If you want to adjust the start of the bins based on a fixed timestamp:

\>>> start, end \= "2000-10-01 23:30:00", "2000-10-02 00:30:00"
\>>> rng \= pd.date\_range(start, end, freq\="7min")
\>>> ts \= pd.Series(np.arange(len(rng)) \* 3, index\=rng)
\>>> ts
2000-10-01 23:30:00     0
2000-10-01 23:37:00     3
2000-10-01 23:44:00     6
2000-10-01 23:51:00     9
2000-10-01 23:58:00    12
2000-10-02 00:05:00    15
2000-10-02 00:12:00    18
2000-10-02 00:19:00    21
2000-10-02 00:26:00    24
Freq: 7min, dtype: int64

Copy to clipboard

\>>> ts.groupby(pd.Grouper(freq\="17min")).sum()
2000-10-01 23:14:00     0
2000-10-01 23:31:00     9
2000-10-01 23:48:00    21
2000-10-02 00:05:00    54
2000-10-02 00:22:00    24
Freq: 17min, dtype: int64

Copy to clipboard

\>>> ts.groupby(pd.Grouper(freq\="17min", origin\="epoch")).sum()
2000-10-01 23:18:00     0
2000-10-01 23:35:00    18
2000-10-01 23:52:00    27
2000-10-02 00:09:00    39
2000-10-02 00:26:00    24
Freq: 17min, dtype: int64

Copy to clipboard

\>>> ts.groupby(pd.Grouper(freq\="17min", origin\="2000-01-01")).sum()
2000-10-01 23:24:00     3
2000-10-01 23:41:00    15
2000-10-01 23:58:00    45
2000-10-02 00:15:00    45
Freq: 17min, dtype: int64

Copy to clipboard

If you want to adjust the start of the bins with an offset Timedelta, the two following lines are equivalent:

\>>> ts.groupby(pd.Grouper(freq\="17min", origin\="start")).sum()
2000-10-01 23:30:00     9
2000-10-01 23:47:00    21
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64

Copy to clipboard

\>>> ts.groupby(pd.Grouper(freq\="17min", offset\="23h30min")).sum()
2000-10-01 23:30:00     9
2000-10-01 23:47:00    21
2000-10-02 00:04:00    54
2000-10-02 00:21:00    24
Freq: 17min, dtype: int64

Copy to clipboard

To replace the use of the deprecated base argument, you can now use offset, in this example it is equivalent to have base=2:

\>>> ts.groupby(pd.Grouper(freq\="17min", offset\="2min")).sum()
2000-10-01 23:16:00     0
2000-10-01 23:33:00     9
2000-10-01 23:50:00    36
2000-10-02 00:07:00    39
2000-10-02 00:24:00    24
Freq: 17min, dtype: int64

Copy to clipboard

On this page