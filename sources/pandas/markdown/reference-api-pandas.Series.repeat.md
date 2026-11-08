[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.repeat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.repeat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.repeat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.repeat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.repeat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.repeat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.repeat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.repeat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.repeat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.repeat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.repeat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.repeat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.repeat[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html#pandas-series-repeat "Link to this heading")

============================================================================================================================================

Series.repeat(_repeats_, _axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L1357-L1413)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html#pandas.Series.repeat "Link to this definition")

Repeat elements of a Series.

Returns a new Series where each element of the current Series is repeated consecutively a given number of times.

Parameters:

**repeats**int or array of ints

The number of repetitions for each element. This should be a non-negative integer. Repeating 0 times will return an empty Series.

**axis**None

Unused. Parameter needed for compatibility with DataFrame.

Returns:

Series

Newly created Series with repeated elements.

See also

[`Index.repeat`](https://pandas.pydata.org/docs/reference/api/pandas.Index.repeat.html#pandas.Index.repeat "pandas.Index.repeat")

Equivalent function for Index.

[`numpy.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "(in NumPy v2.5)")

Similar method for [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
.

Examples

\>>> s \= pd.Series(\["a", "b", "c"\])
\>>> s
0    a
1    b
2    c
dtype: str
\>>> s.repeat(2)
0    a
0    a
1    b
1    b
2    c
2    c
dtype: str
\>>> s.repeat(\[1, 2, 3\])
0    a
1    b
1    b
2    c
2    c
2    c
dtype: str

Copy to clipboard

On this page