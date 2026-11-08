[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.sem[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html#pandas-dataframe-sem "Link to this heading")

============================================================================================================================================

DataFrame.sem(_\*_, _axis\=0_, _skipna\=True_, _ddof\=1_, _numeric\_only\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L18232-L18317)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html#pandas.DataFrame.sem "Link to this definition")

Return unbiased standard error of the mean over requested axis.

Normalized by N-1 by default. This can be changed using the ddof argument

Parameters:

**axis**{index (0), columns (1)}, default 0

Axis for the function to be applied on. For Series this parameter is unused and defaults to 0.

Warning

The behavior of DataFrame.sem with `axis=None` is deprecated, in a future version this will reduce over both axes and return a scalar To retain the old behavior, pass axis=0 (or do not pass axis).

**skipna**bool, default True

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

**ddof**int, default 1

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

**numeric\_only**bool, default False

Include only float, int, boolean columns. Not implemented for Series.

**\*\*kwargs**

Additional keywords passed.

Returns:

Series

Unbiased standard error of the mean over requested axis.

See also

[`DataFrame.var`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html#pandas.DataFrame.var "pandas.DataFrame.var")

Return unbiased variance over requested axis.

[`DataFrame.std`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std "pandas.DataFrame.std")

Returns sample standard deviation over requested axis.

Examples

\>>> s \= pd.Series(\[1, 2, 3\])
\>>> round(s.sem(), 6)
0.57735

Copy to clipboard

With a DataFrame

\>>> df \= pd.DataFrame({"a": \[1, 2\], "b": \[2, 3\]}, index\=\["tiger", "zebra"\])
\>>> df
       a   b
tiger  1   2
zebra  2   3
\>>> df.sem()
a   0.5
b   0.5
dtype: float64

Copy to clipboard

Using axis=1

\>>> df.sem(axis\=1)
tiger   0.5
zebra   0.5
dtype: float64

Copy to clipboard

In this case, numeric\_only should be set to True to avoid getting an error.

\>>> df \= pd.DataFrame({"a": \[1, 2\], "b": \["T", "Z"\]}, index\=\["tiger", "zebra"\])
\>>> df.sem(numeric\_only\=True)
a   0.5
dtype: float64

Copy to clipboard

On this page