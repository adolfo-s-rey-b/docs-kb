[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.map.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.map.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.map.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.map.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.map.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.map.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.map.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.map.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.map.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.map.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.map.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.map.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.map[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas-dataframe-map "Link to this heading")

============================================================================================================================================

DataFrame.map(_func_, _na\_action\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L15486-L15576)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map "Link to this definition")

Apply a function to a Dataframe elementwise.

Added in version 2.1.0: DataFrame.applymap was deprecated and renamed to DataFrame.map.

This method applies a function that accepts and returns a scalar to every element of a DataFrame.

Parameters:

**func**callable

Python function, returns a single value from a single value.

**na\_action**{None, ‘ignore’}, default None

If ‘ignore’, propagate NaN values, without passing them to func.

**\*\*kwargs**

Additional keyword arguments to pass as keywords arguments to func.

Returns:

DataFrame

Transformed DataFrame.

See also

[`DataFrame.apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")

Apply a function along input axis of DataFrame.

[`DataFrame.replace`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace "pandas.DataFrame.replace")

Replace values given in to\_replace with value.

[`Series.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "pandas.Series.map")

Apply a function elementwise on a Series.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2.12\], \[3.356, 4.567\]\])
\>>> df
       0      1
0  1.000  2.120
1  3.356  4.567

Copy to clipboard

\>>> df.map(lambda x: len(str(x)))
   0  1
0  3  4
1  5  5

Copy to clipboard

Like Series.map, NA values can be ignored:

\>>> df\_copy \= df.copy()
\>>> df\_copy.iloc\[0, 0\] \= pd.NA
\>>> df\_copy.map(lambda x: len(str(x)), na\_action\="ignore")
     0  1
0  NaN  4
1  5.0  5

Copy to clipboard

It is also possible to use map with functions that are not lambda functions:

\>>> df.map(round, ndigits\=1)
     0    1
0  1.0  2.1
1  3.4  4.6

Copy to clipboard

Note that a vectorized version of func often exists, which will be much faster. You could square each number elementwise.

\>>> df.map(lambda x: x\*\*2)
           0          1
0   1.000000   4.494400
1  11.262736  20.857489

Copy to clipboard

But it’s better to avoid map in that case.

\>>> df\*\*2
           0          1
0   1.000000   4.494400
1  11.262736  20.857489

Copy to clipboard

On this page