[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.from\_codes[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas-categorical-from-codes "Link to this heading")

========================================================================================================================================================================

classmethod Categorical.from\_codes(_codes_, _categories\=None_, _ordered\=None_, _dtype\=None_, _validate\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L874-L946)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas.Categorical.from_codes "Link to this definition")

Make a Categorical type from codes and categories or dtype.

This constructor is useful if you already have codes and categories/dtype and so do not need the (computation intensive) factorization step, which is usually done on the constructor.

If your data does not follow this convention, please use the normal constructor.

Parameters:

**codes**array-like of int

An integer array, where each integer points to a category in categories or dtype.categories, or else is -1 for NaN.

**categories**index-like, optional

The categories for the categorical. Items need to be unique. If the categories are not given here, then they must be provided in dtype.

**ordered**bool, optional

Whether or not this categorical is treated as an ordered categorical. If not given here or in dtype, the resulting categorical will be unordered.

**dtype**CategoricalDtype or “category”, optional

If [`CategoricalDtype`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalDtype.html#pandas.CategoricalDtype "pandas.CategoricalDtype")
, cannot be used together with categories or ordered.

**validate**bool, default True

If True, validate that the codes are valid for the dtype. If False, don’t validate that the codes are valid. Be careful about skipping validation, as invalid codes can lead to severe problems, such as segfaults.

Added in version 2.1.0.

Returns:

Categorical

See also

[`codes`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.codes.html#pandas.Categorical.codes "pandas.Categorical.codes")

The category codes of the categorical.

[`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")

An Index with an underlying `Categorical`.

Examples

\>>> dtype \= pd.CategoricalDtype(\["a", "b"\], ordered\=True)
\>>> pd.Categorical.from\_codes(codes\=\[0, 1, 0, 1\], dtype\=dtype)
\['a', 'b', 'a', 'b'\]
Categories (2, str): \['a' < 'b'\]

Copy to clipboard

On this page