[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.str.cat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.str.cat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.str.cat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.str.cat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.str.cat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.str.cat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.str.cat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.str.cat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.str.cat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.str.cat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.str.cat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.str.cat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.str.cat[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html#pandas-series-str-cat "Link to this heading")

===============================================================================================================================================

Series.str.cat(_others\=None_, _sep\=None_, _na\_rep\=None_, _join\='left'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/strings/accessor.py#L492-L740)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html#pandas.Series.str.cat "Link to this definition")

Concatenate strings in the Series/Index with given separator.

If others is specified, this function concatenates the Series/Index and elements of others element-wise. If others is not passed, then all values in the Series/Index are concatenated into a single string with a given sep.

Parameters:

**others**Series, Index, DataFrame, np.ndarray or list-like

Series, Index, DataFrame, np.ndarray (one- or two-dimensional) and other list-likes of strings must have the same length as the calling Series/Index, with the exception of indexed objects (i.e. Series/Index/DataFrame) if join is not None.

If others is a list-like that contains a combination of Series, Index or np.ndarray (1-dim), then all elements will be unpacked and must satisfy the above criteria individually.

If others is None, the method returns the concatenation of all strings in the calling Series/Index.

**sep**str, default ‘’

The separator between the different elements/columns. By default the empty string ‘’ is used.

**na\_rep**str or None, default None

Representation that is inserted for all missing values:

*   If na\_rep is None, and others is None, missing values in the Series/Index are omitted from the result.
    
*   If na\_rep is None, and others is not None, a row containing a missing value in any of the columns (before concatenation) will have a missing value in the result.
    

**join**{‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘left’

Determines the join-style between the calling Series/Index and any Series/Index/DataFrame in others (objects without an index need to match the length of the calling Series/Index). To disable alignment, use .values on any Series/Index/DataFrame in others. Note: when the caller is an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
, its _values_ are used as the index for alignment, so a `Series` or `DataFrame` in others is aligned against those values rather than positionally. An `Index` or `np.ndarray` in others has no index of its own and is always used positionally.

Returns:

str, Series or Index

If others is None, str is returned, otherwise a Series/Index (same type as caller) of objects is returned.

See also

[`split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html#pandas.Series.str.split "pandas.Series.str.split")

Split each string in the Series/Index.

[`join`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html#pandas.Series.str.join "pandas.Series.str.join")

Join lists contained as elements in the Series/Index.

Examples

When not passing others, all values are concatenated into a single string:

\>>> s \= pd.Series(\["a", "b", np.nan, "d"\])
\>>> s.str.cat(sep\=" ")
'a b d'

Copy to clipboard

By default, NA values in the Series are ignored. Using na\_rep, they can be given a representation:

\>>> s.str.cat(sep\=" ", na\_rep\="?")
'a b ? d'

Copy to clipboard

If others is specified, corresponding values are concatenated with the separator. Result will be a Series of strings.

\>>> s.str.cat(\["A", "B", "C", "D"\], sep\=",")
0    a,A
1    b,B
2    NaN
3    d,D
dtype: str

Copy to clipboard

Missing values will remain missing in the result, but can again be represented using na\_rep

\>>> s.str.cat(\["A", "B", "C", "D"\], sep\=",", na\_rep\="-")
0    a,A
1    b,B
2    -,C
3    d,D
dtype: str

Copy to clipboard

If sep is not specified, the values are concatenated without separation.

\>>> s.str.cat(\["A", "B", "C", "D"\], na\_rep\="-")
0    aA
1    bB
2    -C
3    dD
dtype: str

Copy to clipboard

Series with different indexes can be aligned before concatenation. The join\-keyword works as in other methods.

\>>> t \= pd.Series(\["d", "a", "e", "c"\], index\=\[3, 0, 4, 2\])
\>>> s.str.cat(t, join\="left", na\_rep\="-")
0    aa
1    b-
2    -c
3    dd
dtype: str
\>>>
\>>> s.str.cat(t, join\="outer", na\_rep\="-")
0    aa
1    b-
2    -c
3    dd
4    -e
dtype: str
\>>>
\>>> s.str.cat(t, join\="inner", na\_rep\="-")
0    aa
2    -c
3    dd
dtype: str
\>>>
\>>> s.str.cat(t, join\="right", na\_rep\="-")
3    dd
0    aa
4    -e
2    -c
dtype: str

Copy to clipboard

When the caller is an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
, alignment uses the values of that `Index`, so concatenating with a `Series` whose index is unrelated gives missing values:

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> idx.str.cat(pd.Series(\["x", "y", "z"\]))
Index(\[nan, nan, nan\], dtype='object')

Copy to clipboard

Use `.to_numpy()` (or `.values`) to concatenate positionally:

\>>> idx.str.cat(pd.Series(\["x", "y", "z"\]).to\_numpy())
Index(\['ax', 'by', 'cz'\], dtype='str')

Copy to clipboard

For more examples, see [here](https://pandas.pydata.org/docs/user_guide/text.html#text-concatenate)
.

On this page