[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.round.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.round.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.round.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.round.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.round.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.round.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.round.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.round.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.round.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.round.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.round.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.round.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.round[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html#pandas-dataframe-round "Link to this heading")

==================================================================================================================================================

DataFrame.round(_decimals\=0_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L16207-L16351)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html#pandas.DataFrame.round "Link to this definition")

Round numeric columns in a DataFrame to a variable number of decimal places.

Each column can be rounded to a different number of decimal places by passing a dict or Series mapping column names to the desired precision. Non-numeric columns are left unchanged.

Parameters:

**decimals**int, dict, Series

Number of decimal places to round each column to. If an int is given, round each column to the same number of places. Otherwise dict and Series round to variable numbers of places. Column names should be in the keys if decimals is a dict-like, or in the index if decimals is a Series. Any columns not included in decimals will be left as is. Elements of decimals which are not columns of the input will be ignored.

**\*args**

Additional keyword arguments have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

**\*\*kwargs**

Additional keyword arguments have no effect but might be accepted for compatibility with NumPy. See [NumPy compatibility kwargs](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-numpy-kwargs)
 for more.

Returns:

DataFrame

A DataFrame with the affected columns rounded to the specified number of decimal places.

See also

[`numpy.around`](https://numpy.org/doc/stable/reference/generated/numpy.around.html#numpy.around "(in NumPy v2.5)")

Round a numpy array to the given number of decimals.

[`Series.round`](https://pandas.pydata.org/docs/reference/api/pandas.Series.round.html#pandas.Series.round "pandas.Series.round")

Round a Series to the given number of decimals.

Notes

For values exactly halfway between rounded decimal values, pandas rounds to the nearest even value (e.g. -0.5 and 0.5 round to 0.0, 1.5 and 2.5 round to 2.0, etc.).

Examples

\>>> df \= pd.DataFrame(
...     \[(0.21, 0.32), (0.01, 0.67), (0.66, 0.03), (0.21, 0.18)\],
...     columns\=\["dogs", "cats"\],
... )
\>>> df
    dogs  cats
0  0.21  0.32
1  0.01  0.67
2  0.66  0.03
3  0.21  0.18

Copy to clipboard

By providing an integer each column is rounded to the same number of decimal places

\>>> df.round(1)
    dogs  cats
0   0.2   0.3
1   0.0   0.7
2   0.7   0.0
3   0.2   0.2

Copy to clipboard

With a dict, the number of places for specific columns can be specified with the column names as key and the number of decimal places as value

\>>> df.round({"dogs": 1, "cats": 0})
    dogs  cats
0   0.2   0.0
1   0.0   1.0
2   0.7   0.0
3   0.2   0.0

Copy to clipboard

Using a Series, the number of places for specific columns can be specified with the column names as index and the number of decimal places as value

\>>> decimals \= pd.Series(\[0, 1\], index\=\["cats", "dogs"\])
\>>> df.round(decimals)
    dogs  cats
0   0.2   0.0
1   0.0   1.0
2   0.7   0.0
3   0.2   0.0

Copy to clipboard

On this page