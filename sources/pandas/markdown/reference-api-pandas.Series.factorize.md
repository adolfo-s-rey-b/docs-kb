[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.factorize.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.factorize.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.factorize.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.factorize.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.factorize.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.factorize.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.factorize.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.factorize.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.factorize.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.factorize.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.factorize.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.factorize.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.factorize[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html#pandas-series-factorize "Link to this heading")

=====================================================================================================================================================

Series.factorize(_sort\=False_, _use\_na\_sentinel\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1396-L1543)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html#pandas.Series.factorize "Link to this definition")

Encode the object as an enumerated type or categorical variable.

This method is useful for obtaining a numeric representation of an array when all that matters is identifying distinct values. factorize is available as both a top-level function [`pandas.factorize()`](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html#pandas.factorize "pandas.factorize")
, and as a method [`Series.factorize()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html#pandas.Series.factorize "pandas.Series.factorize")
 and [`Index.factorize()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.factorize.html#pandas.Index.factorize "pandas.Index.factorize")
.

Parameters:

**sort**bool, default False

Sort uniques and shuffle codes to maintain the relationship.

**use\_na\_sentinel**bool, default True

If True, the sentinel -1 will be used for NaN values. If False, NaN values will be encoded as non-negative integers and will not drop the NaN from the uniques of the values.

Returns:

**codes**ndarray

An integer ndarray that’s an indexer into uniques. `uniques.take(codes)` will have the same values as values.

**uniques**ndarray, Index, or Categorical

The unique valid values. When values is Categorical, uniques is a Categorical. When values is some other pandas object, an Index is returned. Otherwise, a 1-D ndarray is returned.

Note

Even if there’s a missing value in values, uniques will _not_ contain an entry for it.

See also

[`cut`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")

Discretize continuous-valued array.

[`unique`](https://pandas.pydata.org/docs/reference/api/pandas.unique.html#pandas.unique "pandas.unique")

Find the unique value in an array.

Notes

Reference [the user guide](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-factorize)
 for more examples.

Examples

These examples all show factorize as a top-level method like `pd.factorize(values)`. The results are identical for methods like [`Series.factorize()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html#pandas.Series.factorize "pandas.Series.factorize")
.

\>>> codes, uniques \= pd.factorize(
...     np.array(\["b", "b", "a", "c", "b"\], dtype\="O")
... )
\>>> codes
array(\[0, 0, 1, 2, 0\])
\>>> uniques
array(\['b', 'a', 'c'\], dtype=object)

Copy to clipboard

With `sort=True`, the uniques will be sorted, and codes will be shuffled so that the relationship is the maintained.

\>>> codes, uniques \= pd.factorize(
...     np.array(\["b", "b", "a", "c", "b"\], dtype\="O"), sort\=True
... )
\>>> codes
array(\[1, 1, 0, 2, 1\])
\>>> uniques
array(\['a', 'b', 'c'\], dtype=object)

Copy to clipboard

When `use_na_sentinel=True` (the default), missing values are indicated in the codes with the sentinel value `-1` and missing values are not included in uniques.

\>>> codes, uniques \= pd.factorize(
...     np.array(\["b", None, "a", "c", "b"\], dtype\="O")
... )
\>>> codes
array(\[ 0, -1,  1,  2,  0\])
\>>> uniques
array(\['b', 'a', 'c'\], dtype=object)

Copy to clipboard

Thus far, we’ve only factorized lists (which are internally coerced to NumPy arrays). When factorizing pandas objects, the type of uniques will differ. For Categoricals, a Categorical is returned.

\>>> cat \= pd.Categorical(\["a", "a", "c"\], categories\=\["a", "b", "c"\])
\>>> codes, uniques \= pd.factorize(cat)
\>>> codes
array(\[0, 0, 1\])
\>>> uniques
\['a', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

Notice that `'b'` is in `uniques.categories`, despite not being present in `cat.values`.

For all other pandas objects, an Index of the appropriate type is returned.

\>>> cat \= pd.Series(\["a", "a", "c"\])
\>>> codes, uniques \= pd.factorize(cat)
\>>> codes
array(\[0, 0, 1\])
\>>> uniques
Index(\['a', 'c'\], dtype='str')

Copy to clipboard

If NaN is in the values, and we want to include NaN in the uniques of the values, it can be achieved by setting `use_na_sentinel=False`.

\>>> values \= np.array(\[1, 2, 1, np.nan\])
\>>> codes, uniques \= pd.factorize(values)  \# default: use\_na\_sentinel=True
\>>> codes
array(\[ 0,  1,  0, -1\])
\>>> uniques
array(\[1., 2.\])

Copy to clipboard

\>>> codes, uniques \= pd.factorize(values, use\_na\_sentinel\=False)
\>>> codes
array(\[0, 1, 0, 2\])
\>>> uniques
array(\[ 1.,  2., nan\])

Copy to clipboard

On this page