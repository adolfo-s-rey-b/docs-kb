[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sample.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.SeriesGroupBy.sample.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.SeriesGroupBy.sample[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sample.html#pandas-api-typing-seriesgroupby-sample "Link to this heading")

==================================================================================================================================================================================================

SeriesGroupBy.sample(_n\=None_, _frac\=None_, _replace\=False_, _weights\=None_, _random\_state\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/groupby/groupby.py#L5586-L5709)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sample.html#pandas.api.typing.SeriesGroupBy.sample "Link to this definition")

Return a random sample of items from each group.

You can use random\_state for reproducibility.

Parameters:

**n**int, optional

Number of items to return for each group. Cannot be used with frac and must be no larger than the smallest group unless replace is True. Default is one if frac is None.

**frac**float, optional

Fraction of items to return. Cannot be used with n.

**replace**bool, default False

Allow or disallow sampling of the same row more than once.

**weights**list-like, optional

Default None results in equal probability weighting. If passed a list-like then values must have the same length as the underlying DataFrame or Series object and will be used as sampling probabilities after normalization within each group. Values must be non-negative with at least one positive element within each group.

**random\_state**int, array-like, BitGenerator, np.random.RandomState, np.random.Generator, optional

If int, array-like, or BitGenerator, seed for random number generator. If np.random.RandomState or np.random.Generator, use as given. Default `None` results in sampling with the current state of np.random.

Returns:

Series or DataFrame

A new object of same type as caller containing items randomly sampled within each group from the caller object.

See also

`DataFrame.sample`

Generate random samples from a DataFrame object.

`Series.sample`

Generate random samples from a Series object.

[`numpy.random.choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html#numpy.random.choice "(in NumPy v2.5)")

Generate a random sample from a given 1-D numpy array.

Examples

\>>> df \= pd.DataFrame(
...     {"a": \["red"\] \* 2 + \["blue"\] \* 2 + \["black"\] \* 2, "b": range(6)}
... )
\>>> df
       a  b
0    red  0
1    red  1
2   blue  2
3   blue  3
4  black  4
5  black  5

Copy to clipboard

Select one row at random for each distinct value in column a. The random\_state argument can be used to guarantee reproducibility:

\>>> df.groupby("a").sample(n\=1, random\_state\=1)
       a  b
4  black  4
2   blue  2
1    red  1

Copy to clipboard

Set frac to sample fixed proportions rather than counts:

\>>> df.groupby("a")\["b"\].sample(frac\=0.5, random\_state\=2)
5    5
2    2
0    0
Name: b, dtype: int64

Copy to clipboard

Control sample probabilities within groups by setting weights:

\>>> df.groupby("a").sample(
...     n\=1,
...     weights\=\[1, 1, 1, 0, 0, 1\],
...     random\_state\=1,
... )
       a  b
5  black  5
2   blue  2
0    red  0

Copy to clipboard

On this page