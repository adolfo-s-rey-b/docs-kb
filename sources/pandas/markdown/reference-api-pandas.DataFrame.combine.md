[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.combine.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.combine.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.combine.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.combine.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.combine.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.combine.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.combine.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.combine.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.combine.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.combine.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.combine.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.combine.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.combine[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html#pandas-dataframe-combine "Link to this heading")

========================================================================================================================================================

DataFrame.combine(_other_, _func_, _fill\_value\=None_, _overwrite\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L13133-L13316)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html#pandas.DataFrame.combine "Link to this definition")

Perform column-wise combine with another DataFrame.

Combines a DataFrame with other DataFrame using func to element-wise combine columns. The row and column indexes of the resulting DataFrame will be the union of the two.

Parameters:

**other**DataFrame

The DataFrame to merge column-wise.

**func**function

Function that takes two series as inputs and return a Series or a scalar. Used to merge the two dataframes column by columns.

**fill\_value**scalar value, default None

The value to fill NaNs with prior to passing any column to the merge func.

**overwrite**bool, default True

If True, columns in self that do not exist in other will be overwritten with NaNs.

Returns:

DataFrame

Combination of the provided DataFrames.

See also

[`DataFrame.combine_first`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first "pandas.DataFrame.combine_first")

Combine two DataFrame objects and default to non-null values in frame calling the method.

Examples

Combine using a simple function that chooses the smaller column.

\>>> df1 \= pd.DataFrame({"A": \[0, 0\], "B": \[4, 4\]})
\>>> df2 \= pd.DataFrame({"A": \[1, 1\], "B": \[3, 3\]})
\>>> take\_smaller \= lambda s1, s2: s1 if s1.sum() < s2.sum() else s2
\>>> df1.combine(df2, take\_smaller)
   A  B
0  0  3
1  0  3

Copy to clipboard

Example using a true element-wise combine function.

\>>> df1 \= pd.DataFrame({"A": \[5, 0\], "B": \[2, 4\]})
\>>> df2 \= pd.DataFrame({"A": \[1, 1\], "B": \[3, 3\]})
\>>> df1.combine(df2, np.minimum)
   A  B
0  1  2
1  0  3

Copy to clipboard

Using fill\_value fills Nones prior to passing the column to the merge function.

\>>> df1 \= pd.DataFrame({"A": \[0, 0\], "B": \[None, 4\]})
\>>> df2 \= pd.DataFrame({"A": \[1, 1\], "B": \[3, 3\]})
\>>> df1.combine(df2, take\_smaller, fill\_value\=-5)
   A    B
0  0 -5.0
1  0  4.0

Copy to clipboard

Example that demonstrates the use of overwrite and behavior when the axis differ between the dataframes.

\>>> df1 \= pd.DataFrame({"A": \[0, 0\], "B": \[4, 4\]})
\>>> df2 \= pd.DataFrame(
...     {
...         "B": \[3, 3\],
...         "C": \[\-10, 1\],
...     },
...     index\=\[1, 2\],
... )
\>>> df1.combine(df2, take\_smaller)
     A    B     C
0  NaN  NaN   NaN
1  NaN  3.0 -10.0
2  NaN  3.0   1.0

Copy to clipboard

\>>> df1.combine(df2, take\_smaller, overwrite\=False)
     A    B     C
0  0.0  NaN   NaN
1  0.0  3.0 -10.0
2  NaN  3.0   1.0

Copy to clipboard

Demonstrating the preference of the passed in dataframe.

\>>> df2 \= pd.DataFrame(
...     {
...         "B": \[3, 3\],
...         "C": \[1, 1\],
...     },
...     index\=\[1, 2\],
... )
\>>> df2.combine(df1, take\_smaller)
     B    C   A
0  NaN  NaN 0.0
1  3.0  NaN 0.0
2  3.0  NaN NaN

Copy to clipboard

\>>> df2.combine(df1, take\_smaller, overwrite\=False)
     B    C   A
0  NaN  NaN 0.0
1  3.0  1.0 0.0
2  3.0  1.0 NaN

Copy to clipboard

On this page