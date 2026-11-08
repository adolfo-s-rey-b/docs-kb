[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.union_categoricals.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.union_categoricals.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.union_categoricals.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.union_categoricals.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.union_categoricals.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.union_categoricals.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.union_categoricals.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.union_categoricals.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.union_categoricals.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.union_categoricals.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.union_categoricals.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.union_categoricals.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.union_categoricals.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.union_categoricals.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.union\_categoricals[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.union_categoricals.html#pandas-api-types-union-categoricals "Link to this heading")

==========================================================================================================================================================================================

pandas.api.types.union\_categoricals(_to\_union_, _sort\_categories\=False_, _ignore\_order\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/dtypes/concat.py#L230-L400)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.union_categoricals.html#pandas.api.types.union_categoricals "Link to this definition")

Combine list-like of Categorical-like, unioning categories.

All categories must have the same dtype.

Parameters:

**to\_union**list-like

Categorical, CategoricalIndex, or Series with dtype=’category’.

**sort\_categories**bool, default False

If true, resulting categories will be lexsorted, otherwise they will be ordered as they appear in the data.

**ignore\_order**bool, default False

If true, the ordered attribute of the Categoricals will be ignored. Results in an unordered categorical.

Returns:

Categorical

The union of categories being combined.

Raises:

TypeError

*   all inputs do not have the same dtype
    
*   all inputs do not have the same ordered property
    
*   all inputs are ordered and their categories are not identical
    
*   sort\_categories=True and Categoricals are ordered
    

ValueError

Empty list of categoricals passed

See also

`CategoricalDtype`

Type for categorical data with the categories and orderedness.

`Categorical`

Represent a categorical variable in classic R / S-plus fashion.

Notes

To learn more about categories, see [link](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html#unioning)

Examples

If you want to combine categoricals that do not necessarily have the same categories, union\_categoricals will combine a list-like of categoricals. The new categories will be the union of the categories being combined.

\>>> a \= pd.Categorical(\["b", "c"\])
\>>> b \= pd.Categorical(\["a", "b"\])
\>>> pd.api.types.union\_categoricals(\[a, b\])
\['b', 'c', 'a', 'b'\]
Categories (3, str): \['b', 'c', 'a'\]

Copy to clipboard

By default, the resulting categories will be ordered as they appear in the categories of the data. If you want the categories to be lexsorted, use sort\_categories=True argument.

\>>> pd.api.types.union\_categoricals(\[a, b\], sort\_categories\=True)
\['b', 'c', 'a', 'b'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

union\_categoricals also works with the case of combining two categoricals of the same categories and order information (e.g. what you could also append for).

\>>> a \= pd.Categorical(\["a", "b"\], ordered\=True)
\>>> b \= pd.Categorical(\["a", "b", "a"\], ordered\=True)
\>>> pd.api.types.union\_categoricals(\[a, b\])
\['a', 'b', 'a', 'b', 'a'\]
Categories (2, str): \['a' < 'b'\]

Copy to clipboard

Raises TypeError because the categories are ordered and not identical.

\>>> a \= pd.Categorical(\["a", "b"\], ordered\=True)
\>>> b \= pd.Categorical(\["a", "b", "c"\], ordered\=True)
\>>> pd.api.types.union\_categoricals(\[a, b\])
Traceback (most recent call last):
    ...
TypeError: to union ordered Categoricals, all categories must be the same

Copy to clipboard

Ordered categoricals with different categories or orderings can be combined by using the ignore\_order=True argument.

\>>> a \= pd.Categorical(\["a", "b", "c"\], ordered\=True)
\>>> b \= pd.Categorical(\["c", "b", "a"\], ordered\=True)
\>>> pd.api.types.union\_categoricals(\[a, b\], ignore\_order\=True)
\['a', 'b', 'c', 'c', 'b', 'a'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

union\_categoricals also works with a CategoricalIndex, or Series containing categorical data, but note that the resulting array will always be a plain Categorical

\>>> a \= pd.Series(\["b", "c"\], dtype\="category")
\>>> b \= pd.Series(\["a", "b"\], dtype\="category")
\>>> pd.api.types.union\_categoricals(\[a, b\])
\['b', 'c', 'a', 'b'\]
Categories (3, str): \['b', 'c', 'a'\]

Copy to clipboard

On this page