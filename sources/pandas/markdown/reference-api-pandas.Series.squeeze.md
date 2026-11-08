[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.squeeze.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.squeeze.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.squeeze.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.squeeze.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.squeeze.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.squeeze.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.squeeze.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.squeeze.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.squeeze.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.squeeze.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.squeeze.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.squeeze.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.squeeze.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.squeeze.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.squeeze[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.squeeze.html#pandas-series-squeeze "Link to this heading")

===============================================================================================================================================

Series.squeeze(_axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L850-L963)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.squeeze.html#pandas.Series.squeeze "Link to this definition")

Squeeze 1 dimensional axis objects into scalars.

Series or DataFrames with a single element are squeezed to a scalar. DataFrames with a single column or a single row are squeezed to a Series. Otherwise the object is unchanged.

This method is most useful when you don’t know if your object is a Series or DataFrame, but you do know it has just a single column. In that case you can safely call squeeze to ensure you have a Series.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

A specific axis to squeeze. By default, all length-1 axes are squeezed. For Series this parameter is unused and defaults to None.

Returns:

DataFrame, Series, or scalar

The projection after squeezing axis or all the axes.

See also

[`Series.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc "pandas.Series.iloc")

Integer-location based indexing for selecting scalars.

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Integer-location based indexing for selecting Series.

[`Series.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")

Inverse of DataFrame.squeeze for a single-column DataFrame.

Examples

\>>> primes \= pd.Series(\[2, 3, 5, 7\])

Copy to clipboard

Slicing might produce a Series with a single value:

\>>> even\_primes \= primes\[primes % 2 \== 0\]
\>>> even\_primes
0    2
dtype: int64

Copy to clipboard

\>>> even\_primes.squeeze()
2

Copy to clipboard

Squeezing objects with more than one value in every axis does nothing:

\>>> odd\_primes \= primes\[primes % 2 \== 1\]
\>>> odd\_primes
1    3
2    5
3    7
dtype: int64

Copy to clipboard

\>>> odd\_primes.squeeze()
1    3
2    5
3    7
dtype: int64

Copy to clipboard

Squeezing is even more effective when used with DataFrames.

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], columns\=\["a", "b"\])
\>>> df
   a  b
0  1  2
1  3  4

Copy to clipboard

Slicing a single column will produce a DataFrame with the columns having only one value:

\>>> df\_a \= df\[\["a"\]\]
\>>> df\_a
   a
0  1
1  3

Copy to clipboard

So the columns can be squeezed down, resulting in a Series:

\>>> df\_a.squeeze("columns")
0    1
1    3
Name: a, dtype: int64

Copy to clipboard

Slicing a single row from a single column will produce a single scalar DataFrame:

\>>> df\_0a \= df.loc\[df.index < 1, \["a"\]\]
\>>> df\_0a
   a
0  1

Copy to clipboard

Squeezing the rows produces a single scalar Series:

\>>> df\_0a.squeeze("rows")
a    1
Name: 0, dtype: int64

Copy to clipboard

Squeezing all axes will project directly into a scalar:

\>>> df\_0a.squeeze()
1

Copy to clipboard

On this page