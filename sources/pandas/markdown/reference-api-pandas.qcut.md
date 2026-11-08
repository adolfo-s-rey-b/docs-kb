[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.qcut.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.qcut.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.qcut.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.qcut.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.qcut.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.qcut.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.qcut.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.qcut.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.qcut.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.qcut.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.qcut.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.qcut.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.qcut[#](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas-qcut "Link to this heading")

=================================================================================================================

pandas.qcut(_x_, _q_, _labels\=None_, _retbins\=False_, _precision\=3_, _duplicates\='raise'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/tile.py#L302-L405)
[#](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut "Link to this definition")

Quantile-based discretization function.

Discretize variable into equal-sized buckets based on rank or based on sample quantiles. For example 1000 values for 10 quantiles would produce a Categorical object indicating quantile membership for each data point.

Parameters:

**x**1d ndarray or Series

Input Numpy array or pandas Series object to be discretized.

**q**int or list-like of float

Number of quantiles. 10 for deciles, 4 for quartiles, etc. Alternately array of quantiles, e.g. \[0, .25, .5, .75, 1.\] for quartiles.

**labels**array or False, default None

Used as labels for the resulting bins. Must be of the same length as the resulting bins. If False, return only integer indicators of the bins. If True, raises an error.

**retbins**bool, optional

Whether to return the (bins, labels) or not. Can be useful if bins is given as a scalar.

**precision**int, optional

The precision at which to store and display the bins labels.

**duplicates**{default ‘raise’, ‘drop’}, optional

If bin edges are not unique, raise ValueError or drop non-uniques.

Returns:

**out**Categorical or Series or array of integers if labels is False

The return type (Categorical or Series) depends on the input: a Series of type category if input is a Series else Categorical. Bins are represented as categories when categorical data is returned.

**bins**ndarray of floats

Returned only if retbins is True.

See also

[`cut`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")

Bin values into discrete intervals.

[`Series.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html#pandas.Series.quantile "pandas.Series.quantile")

Return value at the given quantile.

Notes

Out of bounds values will be NA in the resulting Categorical object. See [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-tile)
 for more examples.

Examples

\>>> pd.qcut(range(5), 4)
...
\[(-0.001, 1.0\], (-0.001, 1.0\], (1.0, 2.0\], (2.0, 3.0\], (3.0, 4.0\]\]
Categories (4, interval\[float64, right\]): \[(-0.001, 1.0\] < (1.0, 2.0\] ...

Copy to clipboard

\>>> pd.qcut(range(5), 3, labels\=\["good", "medium", "bad"\])
...
\[good, good, medium, bad, bad\]
Categories (3, str): \[good < medium < bad\]

Copy to clipboard

\>>> pd.qcut(range(5), 4, labels\=False)
array(\[0, 0, 1, 2, 3\])

Copy to clipboard

On this page