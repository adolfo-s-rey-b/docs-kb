[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.merge_asof.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.merge_asof.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.merge_asof.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.merge_asof.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.merge_asof.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.merge_asof.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.merge_asof.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.merge_asof.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.merge_asof.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.merge_asof.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.merge_asof.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.merge_asof.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.merge\_asof[#](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html#pandas-merge-asof "Link to this heading")

====================================================================================================================================

pandas.merge\_asof(_left_, _right_, _on\=None_, _left\_on\=None_, _right\_on\=None_, _left\_index\=False_, _right\_index\=False_, _by\=None_, _left\_by\=None_, _right\_by\=None_, _suffixes\=('\_x', '\_y')_, _tolerance\=None_, _allow\_exact\_matches\=True_, _direction\='backward'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/merge.py#L646-L930)
[#](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html#pandas.merge_asof "Link to this definition")

Perform a merge by key distance.

This is similar to a left-join except that we match on nearest key rather than equal keys. Both DataFrames must be first sorted by the merge key in ascending order before calling this function. Sorting by any additional ‘by’ grouping columns is not required.

For each row in the left DataFrame:

> *   A “backward” search selects the last row in the right DataFrame whose ‘on’ key is less than or equal to the left’s key.
>     
> *   A “forward” search selects the first row in the right DataFrame whose ‘on’ key is greater than or equal to the left’s key.
>     
> *   A “nearest” search selects the row in the right DataFrame whose ‘on’ key is closest in absolute distance to the left’s key.
>     

Optionally match on equivalent keys with ‘by’ before searching with ‘on’.

Parameters:

**left**DataFrame or named Series

First pandas object to merge.

**right**DataFrame or named Series

Second pandas object to merge.

**on**label

Field name to join on. Must be found in both DataFrames. The data MUST be in ascending order. Furthermore this must be a numeric column, such as datetimelike, integer, or float. `on` or `left_on` / `right_on` must be given.

**left\_on**label or array-like

Field name to join on in left DataFrame. Can also be an array of the length of the left DataFrame, which is treated as if it were a column. If specified, sort the left DataFrame by this key in ascending order before merging.

**right\_on**label or array-like

Field name to join on in right DataFrame. Can also be an array of the length of the right DataFrame, which is treated as if it were a column. If specified, sort the right DataFrame by this key in ascending order before merging.

**left\_index**bool

Use the index of the left DataFrame as the join key.

**right\_index**bool

Use the index of the right DataFrame as the join key.

**by**column name or list of column names

Match on these columns before performing merge operation. It is not required to sort by these columns.

**left\_by**column name

Field names to match on in the left DataFrame.

**right\_by**column name

Field names to match on in the right DataFrame.

**suffixes**2-length sequence (tuple, list, …)

Suffix to apply to overlapping column names in the left and right side, respectively.

**tolerance**int or timedelta, optional, default None

Select asof tolerance within this range; must be compatible with the merge index.

**allow\_exact\_matches**bool, default True

*   If True, allow matching with the same ‘on’ value (i.e. less-than-or-equal-to / greater-than-or-equal-to)
    
*   If False, don’t match the same ‘on’ value (i.e., strictly less-than / strictly greater-than).
    

**direction**‘backward’ (default), ‘forward’, or ‘nearest’

Whether to search for prior, subsequent, or closest matches.

Returns:

DataFrame

A DataFrame of the two merged objects, containing all rows from the left DataFrame and the nearest matches from the right DataFrame. The key column holds the left DataFrame’s values; the right DataFrame’s key column is retained only if it has a different name.

See also

[`merge`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge "pandas.merge")

Merge with a database-style join.

[`merge_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html#pandas.merge_ordered "pandas.merge_ordered")

Merge with optional filling/interpolation.

Examples

\>>> left \= pd.DataFrame({"a": \[1, 5, 10\], "left\_val": \["a", "b", "c"\]})
\>>> left
    a left\_val
0   1        a
1   5        b
2  10        c

Copy to clipboard

\>>> right \= pd.DataFrame({"a": \[1, 2, 3, 6, 7\], "right\_val": \[1, 2, 3, 6, 7\]})
\>>> right
   a  right\_val
0  1          1
1  2          2
2  3          3
3  6          6
4  7          7

Copy to clipboard

\>>> pd.merge\_asof(left, right, on\="a")
    a left\_val  right\_val
0   1        a          1
1   5        b          3
2  10        c          7

Copy to clipboard

\>>> pd.merge\_asof(left, right, on\="a", allow\_exact\_matches\=False)
    a left\_val  right\_val
0   1        a        NaN
1   5        b        3.0
2  10        c        7.0

Copy to clipboard

\>>> pd.merge\_asof(left, right, on\="a", direction\="forward")
    a left\_val  right\_val
0   1        a        1.0
1   5        b        6.0
2  10        c        NaN

Copy to clipboard

\>>> pd.merge\_asof(left, right, on\="a", direction\="nearest")
    a left\_val  right\_val
0   1        a          1
1   5        b          6
2  10        c          7

Copy to clipboard

We can use indexed DataFrames as well.

\>>> left \= pd.DataFrame({"left\_val": \["a", "b", "c"\]}, index\=\[1, 5, 10\])
\>>> left
   left\_val
1         a
5         b
10        c

Copy to clipboard

\>>> right \= pd.DataFrame({"right\_val": \[1, 2, 3, 6, 7\]}, index\=\[1, 2, 3, 6, 7\])
\>>> right
   right\_val
1          1
2          2
3          3
6          6
7          7

Copy to clipboard

\>>> pd.merge\_asof(left, right, left\_index\=True, right\_index\=True)
   left\_val  right\_val
1         a          1
5         b          3
10        c          7

Copy to clipboard

Here is a real-world times-series example

\>>> quotes \= pd.DataFrame(
...     {
...         "time": \[\
...             pd.Timestamp("2016-05-25 13:30:00.023"),\
...             pd.Timestamp("2016-05-25 13:30:00.023"),\
...             pd.Timestamp("2016-05-25 13:30:00.030"),\
...             pd.Timestamp("2016-05-25 13:30:00.041"),\
...             pd.Timestamp("2016-05-25 13:30:00.048"),\
...             pd.Timestamp("2016-05-25 13:30:00.049"),\
...             pd.Timestamp("2016-05-25 13:30:00.072"),\
...             pd.Timestamp("2016-05-25 13:30:00.075"),\
...         \],
...         "ticker": \[\
...             "GOOG",\
...             "MSFT",\
...             "MSFT",\
...             "MSFT",\
...             "GOOG",\
...             "AAPL",\
...             "GOOG",\
...             "MSFT",\
...         \],
...         "bid": \[720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01\],
...         "ask": \[720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03\],
...     }
... )
\>>> quotes
                     time ticker     bid     ask
0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
7 2016-05-25 13:30:00.075   MSFT   52.01   52.03

Copy to clipboard

\>>> trades \= pd.DataFrame(
...     {
...         "time": \[\
...             pd.Timestamp("2016-05-25 13:30:00.023"),\
...             pd.Timestamp("2016-05-25 13:30:00.038"),\
...             pd.Timestamp("2016-05-25 13:30:00.048"),\
...             pd.Timestamp("2016-05-25 13:30:00.048"),\
...             pd.Timestamp("2016-05-25 13:30:00.048"),\
...         \],
...         "ticker": \["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"\],
...         "price": \[51.95, 51.95, 720.77, 720.92, 98.0\],
...         "quantity": \[75, 155, 100, 100, 100\],
...     }
... )
\>>> trades
                     time ticker   price  quantity
0 2016-05-25 13:30:00.023   MSFT   51.95        75
1 2016-05-25 13:30:00.038   MSFT   51.95       155
2 2016-05-25 13:30:00.048   GOOG  720.77       100
3 2016-05-25 13:30:00.048   GOOG  720.92       100
4 2016-05-25 13:30:00.048   AAPL   98.00       100

Copy to clipboard

By default we are taking the asof of the quotes

\>>> pd.merge\_asof(trades, quotes, on\="time", by\="ticker")
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

Copy to clipboard

We only asof within 2ms between the quote time and the trade time

\>>> pd.merge\_asof(
...     trades, quotes, on\="time", by\="ticker", tolerance\=pd.Timedelta("2ms")
... )
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
2 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
3 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

Copy to clipboard

We only asof within 10ms between the quote time and the trade time and we exclude exact matches on time. However _prior_ data will propagate forward

\>>> pd.merge\_asof(
...     trades,
...     quotes,
...     on\="time",
...     by\="ticker",
...     tolerance\=pd.Timedelta("10ms"),
...     allow\_exact\_matches\=False,
... )
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75     NaN     NaN
1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
2 2016-05-25 13:30:00.048   GOOG  720.77       100     NaN     NaN
3 2016-05-25 13:30:00.048   GOOG  720.92       100     NaN     NaN
4 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN

Copy to clipboard

On this page