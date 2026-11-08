[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.dot.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.dot.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.dot.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.dot.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.dot.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.dot.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.dot.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.dot.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.dot.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.dot.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.dot.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.dot.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.dot[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html#pandas-series-dot "Link to this heading")

===================================================================================================================================

Series.dot(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3401-L3479)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html#pandas.Series.dot "Link to this definition")

Compute the dot product between the Series and the columns of other.

This method computes the dot product between the Series and another one, or the Series and each columns of a DataFrame, or the Series and each columns of an array.

It can also be called using self @ other.

Parameters:

**other**Series, DataFrame or array-like

The other object to compute the dot product with its columns.

Returns:

scalar, Series or numpy.ndarray

Return the dot product of the Series and other if other is a Series, the Series of the dot product of Series and each rows of other if other is a DataFrame or a numpy.ndarray between the Series and each columns of the numpy array.

See also

[`DataFrame.dot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html#pandas.DataFrame.dot "pandas.DataFrame.dot")

Compute the matrix product with the DataFrame.

[`Series.mul`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mul.html#pandas.Series.mul "pandas.Series.mul")

Multiplication of series and other, element-wise.

Notes

The Series and other has to share the same index if other is a Series or a DataFrame.

Examples

\>>> s \= pd.Series(\[0, 1, 2, 3\])
\>>> other \= pd.Series(\[\-1, 2, \-3, 4\])
\>>> s.dot(other)
8
\>>> s @ other
8
\>>> df \= pd.DataFrame(\[\[0, 1\], \[\-2, 3\], \[4, \-5\], \[6, 7\]\])
\>>> s.dot(df)
0    24
1    14
dtype: int64
\>>> arr \= np.array(\[\[0, 1\], \[\-2, 3\], \[4, \-5\], \[6, 7\]\])
\>>> s.dot(arr)
array(\[24, 14\])

Copy to clipboard

On this page