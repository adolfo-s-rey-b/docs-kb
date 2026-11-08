[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.cat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.cat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.cat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.cat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.cat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.cat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.cat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.cat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.cat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.cat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.cat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.cat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.cat[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.html#pandas-series-cat "Link to this heading")

===================================================================================================================================

Series.cat()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L3068-L3255)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.html#pandas.Series.cat "Link to this definition")

Accessor object for categorical properties of the Series values.

This accessor provides methods and properties to interact with the underlying categorical data, such as accessing categories, renaming them, reordering, or adding and removing categories.

Parameters:

**data**Series or CategoricalIndex

The object to which the categorical accessor is attached.

See also

[`Series.dt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html#pandas.Series.dt "pandas.Series.dt")

Accessor object for datetimelike properties of the Series values.

[`Series.sparse`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.html#pandas.Series.sparse "pandas.Series.sparse")

Accessor for sparse matrix data types.

Examples

\>>> s \= pd.Series(list("abbccc")).astype("category")
\>>> s
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

\>>> s.cat.categories
Index(\['a', 'b', 'c'\], dtype='str')

Copy to clipboard

\>>> s.cat.rename\_categories(list("cba"))
0    c
1    b
2    b
3    a
4    a
5    a
dtype: category
Categories (3, str): \['c', 'b', 'a'\]

Copy to clipboard

\>>> s.cat.reorder\_categories(list("cba"))
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, str): \['c', 'b', 'a'\]

Copy to clipboard

\>>> s.cat.add\_categories(\["d", "e"\])
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (5, str): \['a', 'b', 'c', 'd', 'e'\]

Copy to clipboard

\>>> s.cat.remove\_categories(\["a", "c"\])
0    NaN
1      b
2      b
3    NaN
4    NaN
5    NaN
dtype: category
Categories (1, str): \['b'\]

Copy to clipboard

\>>> s1 \= s.cat.add\_categories(\["d", "e"\])
\>>> s1.cat.remove\_unused\_categories()
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

\>>> s.cat.set\_categories(list("abcde"))
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (5, str): \['a', 'b', 'c', 'd', 'e'\]

Copy to clipboard

\>>> s.cat.as\_ordered()
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, str): \['a' < 'b' < 'c'\]

Copy to clipboard

\>>> s.cat.as\_unordered()
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

On this page