[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.__invert__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.__invert__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.__invert__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.__invert__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.__invert__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.__invert__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.__invert__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.__invert__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.__invert__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.__invert__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.__invert__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.__invert__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.__invert__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.__invert__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.\_\_invert\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.__invert__.html#pandas-series-invert "Link to this heading")

========================================================================================================================================================

Series.\_\_invert\_\_()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L1388-L1441)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.__invert__.html#pandas.Series.__invert__ "Link to this definition")

Return the bitwise inverse of the Series/DataFrame, element-wise.

Equivalent to applying the `~` (tilde) operator element-wise. For boolean data this returns the logical NOT; for integer data it returns the bitwise NOT (ones complement).

Returns:

Series or DataFrame

A new object of the same type and shape with every element bitwise inverted.

See also

[`numpy.invert`](https://numpy.org/doc/stable/reference/generated/numpy.invert.html#numpy.invert "(in NumPy v2.5)")

Compute bitwise inversion element-wise.

Examples

**Boolean Series:**

\>>> s \= pd.Series(\[True, False, True\])
\>>> ~s
0    False
1     True
2    False
dtype: bool

Copy to clipboard

**Integer Series:**

\>>> s \= pd.Series(\[1, 0, 3\], dtype\="int8")
\>>> ~s
0   -2
1   -1
2   -4
dtype: int8

Copy to clipboard

**Boolean DataFrame:**

\>>> df \= pd.DataFrame({"a": \[True, False\], "b": \[False, True\]})
\>>> ~df
       a      b
0  False   True
1   True  False

Copy to clipboard

On this page