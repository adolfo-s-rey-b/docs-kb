[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.abs.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.abs.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.abs.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.abs.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.abs.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.abs.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.abs.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.abs.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.abs.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.abs.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.abs.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.abs.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.abs[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html#pandas-dataframe-abs "Link to this heading")

============================================================================================================================================

DataFrame.abs()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L1450-L1519)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html#pandas.DataFrame.abs "Link to this definition")

Return a Series/DataFrame with absolute numeric value of each element.

This function only applies to elements that are all numeric.

Returns:

abs

Series/DataFrame containing the absolute value of each element.

See also

[`numpy.absolute`](https://numpy.org/doc/stable/reference/generated/numpy.absolute.html#numpy.absolute "(in NumPy v2.5)")

Calculate the absolute value element-wise.

Notes

For `complex` inputs, `1.2 + 1j`, the absolute value is √𝑎2+𝑏2.

Examples

Absolute numeric values in a Series.

\>>> s \= pd.Series(\[\-1.10, 2, \-3.33, 4\])
\>>> s.abs()
0    1.10
1    2.00
2    3.33
3    4.00
dtype: float64

Copy to clipboard

Absolute numeric values in a Series with complex numbers.

\>>> s \= pd.Series(\[1.2 + 1j\])
\>>> s.abs()
0    1.56205
dtype: float64

Copy to clipboard

Absolute numeric values in a Series with a Timedelta element.

\>>> s \= pd.Series(\[pd.Timedelta("1 days")\])
\>>> s.abs()
0   1 days
dtype: timedelta64\[us\]

Copy to clipboard

Select rows with data closest to certain value using argsort (from [StackOverflow](https://stackoverflow.com/a/17758115)
).

\>>> df \= pd.DataFrame(
...     {"a": \[4, 5, 6, 7\], "b": \[10, 20, 30, 40\], "c": \[100, 50, \-30, \-50\]}
... )
\>>> df
     a    b    c
0    4   10  100
1    5   20   50
2    6   30  -30
3    7   40  -50
\>>> df.loc\[(df.c \- 43).abs().argsort()\]
     a    b    c
1    5   20   50
0    4   10  100
2    6   30  -30
3    7   40  -50

Copy to clipboard

On this page