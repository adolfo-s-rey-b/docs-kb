[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.sample.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.sample.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.sample.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.sample.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.sample.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.sample.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.sample.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.sample.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.sample.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.sample.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.sample.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.sample.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.sample.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.sample.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.sample[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sample.html#pandas-series-sample "Link to this heading")

============================================================================================================================================

Series.sample(_n\=None_, _frac\=None_, _replace\=False_, _weights\=None_, _random\_state\=None_, _axis\=None_, _ignore\_index\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L6077-L6230)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.sample.html#pandas.Series.sample "Link to this definition")

Return a random sample of items from an axis of object.

You can use random\_state for reproducibility.

Parameters:

**n**int, optional

Number of items from axis to return. Cannot be used with frac. Default = 1 if frac = None.

**frac**float, optional

Fraction of axis items to return. Cannot be used with n.

**replace**bool, default False

Allow or disallow sampling of the same row more than once.

**weights**str or ndarray-like, optional

Default `None` results in equal probability weighting. If passed a Series, will align with target object on index. Index values in weights not found in sampled object will be ignored and index values in sampled object not in weights will be assigned weights of zero. If called on a DataFrame, will accept the name of a column when axis = 0. Unless weights are a Series, weights must be same length as axis being sampled. If weights do not sum to 1, they will be normalized to sum to 1. Missing values in the weights column will be treated as zero. Infinite values not allowed. When replace = False will not allow `(n * max(weights) / sum(weights)) > 1` in order to avoid biased results. See the Notes below for more details.

**random\_state**int, array-like, BitGenerator, np.random.RandomState, np.random.Generator, optional

If int, array-like, or BitGenerator, seed for random number generator. If np.random.RandomState or np.random.Generator, use as given. Default `None` results in sampling with the current state of np.random.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

Axis to sample. Accepts axis number or name. Default is stat axis for given data type. For Series this parameter is unused and defaults to None.

**ignore\_index**bool, default False

If True, the resulting index will be labeled 0, 1, …, n - 1.

Returns:

Series or DataFrame

A new object of same type as caller containing n items randomly sampled from the caller object.

See also

`DataFrameGroupBy.sample`

Generates random samples from each group of a DataFrame object.

`SeriesGroupBy.sample`

Generates random samples from each group of a Series object.

[`numpy.random.choice`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html#numpy.random.choice "(in NumPy v2.5)")

Generates a random sample from a given 1-D numpy array.

Notes

If frac > 1, replacement should be set to True.

When replace = False will not allow `(n * max(weights) / sum(weights)) > 1`, since that would cause results to be biased. E.g. sampling 2 items without replacement with weights \[100, 1, 1\] would yield two last items in 1/2 of cases, instead of 1/102. This is similar to specifying n=4 without replacement on a Series with 3 elements.

Examples

\>>> df \= pd.DataFrame(
...     {
...         "num\_legs": \[2, 4, 8, 0\],
...         "num\_wings": \[2, 0, 0, 0\],
...         "num\_specimen\_seen": \[10, 2, 1, 8\],
...     },
...     index\=\["falcon", "dog", "spider", "fish"\],
... )
\>>> df
        num\_legs  num\_wings  num\_specimen\_seen
falcon         2          2                 10
dog            4          0                  2
spider         8          0                  1
fish           0          0                  8

Copy to clipboard

Extract 3 random elements from the `Series` `df['num_legs']`: Note that we use random\_state to ensure the reproducibility of the examples.

\>>> df\["num\_legs"\].sample(n\=3, random\_state\=1)
fish      0
spider    8
falcon    2
Name: num\_legs, dtype: int64

Copy to clipboard

A random 50% sample of the `DataFrame` with replacement:

\>>> df.sample(frac\=0.5, replace\=True, random\_state\=1)
      num\_legs  num\_wings  num\_specimen\_seen
dog          4          0                  2
fish         0          0                  8

Copy to clipboard

An upsample sample of the `DataFrame` with replacement: Note that replace parameter has to be True for frac parameter > 1.

\>>> df.sample(frac\=2, replace\=True, random\_state\=1)
        num\_legs  num\_wings  num\_specimen\_seen
dog            4          0                  2
fish           0          0                  8
falcon         2          2                 10
falcon         2          2                 10
fish           0          0                  8
dog            4          0                  2
fish           0          0                  8
dog            4          0                  2

Copy to clipboard

Using a DataFrame column as weights. Rows with larger value in the num\_specimen\_seen column are more likely to be sampled.

\>>> df.sample(n\=2, weights\="num\_specimen\_seen", random\_state\=1)
        num\_legs  num\_wings  num\_specimen\_seen
falcon         2          2                 10
fish           0          0                  8

Copy to clipboard

On this page