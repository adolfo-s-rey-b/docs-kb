[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.dot[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html#pandas-dataframe-dot "Link to this heading")

============================================================================================================================================

DataFrame.dot(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L1482-L1598)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html#pandas.DataFrame.dot "Link to this definition")

Compute the matrix multiplication between the DataFrame and other.

This method computes the matrix product between the DataFrame and the values of an other Series, DataFrame or a numpy array.

It can also be called using `self @ other`.

Parameters:

**other**Series, DataFrame or array-like

The other object to compute the matrix product with.

Returns:

Series or DataFrame

If other is a Series, return the matrix product between self and other as a Series. If other is a DataFrame or a numpy.array, return the matrix product of self and other in a DataFrame of a np.array.

See also

[`Series.dot`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html#pandas.Series.dot "pandas.Series.dot")

Similar method for Series.

Notes

The dimensions of DataFrame and other must be compatible in order to compute the matrix multiplication. In addition, the column names of DataFrame and the index of other must contain the same values, as they will be aligned prior to the multiplication.

The dot method for Series computes the inner product, instead of the matrix product here.

Examples

Here we multiply a DataFrame with a Series.

\>>> df \= pd.DataFrame(\[\[0, 1, \-2, \-1\], \[1, 1, 1, 1\]\])
\>>> s \= pd.Series(\[1, 1, 2, 1\])
\>>> df.dot(s)
0    -4
1     5
dtype: int64

Copy to clipboard

Here we multiply a DataFrame with another DataFrame.

\>>> other \= pd.DataFrame(\[\[0, 1\], \[1, 2\], \[\-1, \-1\], \[2, 0\]\])
\>>> df.dot(other)
    0   1
0   1   4
1   2   2

Copy to clipboard

Note that the dot method give the same result as @

\>>> df @ other
    0   1
0   1   4
1   2   2

Copy to clipboard

The dot method works also if other is an np.array.

\>>> arr \= np.array(\[\[0, 1\], \[1, 2\], \[\-1, \-1\], \[2, 0\]\])
\>>> df.dot(arr)
    0   1
0   1   4
1   2   2

Copy to clipboard

Note how shuffling of the objects does not change the result.

\>>> s2 \= s.reindex(\[1, 0, 2, 3\])
\>>> df.dot(s2)
0    -4
1     5
dtype: int64

Copy to clipboard

On this page