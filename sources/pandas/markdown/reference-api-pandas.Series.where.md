[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.where.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.where.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.where.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.where.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.where.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.where.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.where.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.where.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.where.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.where.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.where.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.where.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.where[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#pandas-series-where "Link to this heading")

=========================================================================================================================================

Series.where(_cond_, _other\=<no\_default>_, _\*_, _inplace\=False_, _axis\=None_, _level\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L10557-L10727)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#pandas.Series.where "Link to this definition")

Replace values where the condition is False.

This method allows conditional replacement of values. Where the condition evaluates to True, the original values are retained; where it evaluates to False, values are replaced with corresponding entries from `other`.

Parameters:

**cond**bool Series/DataFrame, array-like, or callable

Where cond is True, keep the original value. Where False, replace with corresponding value from other. If cond is callable, it is computed on the Series/DataFrame and should return boolean Series/DataFrame or array. The callable must not change input Series/DataFrame (though pandas doesn’t check it).

**other**scalar, array-like, Series/DataFrame, Index, or callable

Entries where cond is False are replaced with corresponding value from other. If other is callable, it is computed on the Series/DataFrame and should return scalar or Series/DataFrame. The callable must not change input Series/DataFrame (though pandas doesn’t check it). If not specified, entries will be filled with the corresponding NULL value (`np.nan` for numpy dtypes, `pd.NA` for extension dtypes).

**inplace**bool, default False

Whether to perform the operation in place on the data.

**axis**int, default None

Alignment axis, used only when aligning other with the calling object; it has no effect on the alignment of cond, which is always aligned on the calling object’s labels. For Series this parameter is unused and defaults to 0.

**level**int, default None

Alignment level, used only when aligning other with the calling object; it has no effect on the alignment of cond.

Returns:

Series or DataFrame

When applied to a Series, the function will return a Series, and when applied to a DataFrame, it will return a DataFrame.

See also

[`DataFrame.mask()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html#pandas.DataFrame.mask "pandas.DataFrame.mask")

Return an object of same shape as caller.

[`Series.mask()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mask.html#pandas.Series.mask "pandas.Series.mask")

Return an object of same shape as caller.

Notes

The where method is an application of the if-then idiom. For each element in the caller, if `cond` is `True` the element is used; otherwise the corresponding element from `other` is used. If the axis of `cond` does not align with the caller Series/DataFrame, the values of `cond` on misaligned index positions will be filled with False.

The signature for [`Series.where()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#pandas.Series.where "pandas.Series.where")
 or [`DataFrame.where()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where")
 differs from [`numpy.where()`](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where "(in NumPy v2.5)")
. Roughly `df1.where(m, df2)` is equivalent to `np.where(m, df1, df2)`.

For further details and examples see the `where` documentation in [indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-where-mask)
.

The dtype of the object takes precedence. The fill value is casted to the object’s dtype, if this can be done losslessly.

Examples

\>>> s \= pd.Series(range(5))
\>>> s.where(s \> 0)
0    NaN
1    1.0
2    2.0
3    3.0
4    4.0
dtype: float64
\>>> s.mask(s \> 0)
0    0.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64

Copy to clipboard

\>>> s \= pd.Series(range(5))
\>>> t \= pd.Series(\[True, False\])
\>>> s.where(t, 99)
0     0
1    99
2    99
3    99
4    99
dtype: int64
\>>> s.mask(t, 99)
0    99
1     1
2    99
3    99
4    99
dtype: int64

Copy to clipboard

\>>> s.where(s \> 1, 10)
0    10
1    10
2    2
3    3
4    4
dtype: int64
\>>> s.mask(s \> 1, 10)
0     0
1     1
2    10
3    10
4    10
dtype: int64

Copy to clipboard

\>>> df \= pd.DataFrame(np.arange(10).reshape(\-1, 2), columns\=\["A", "B"\])
\>>> df
   A  B
0  0  1
1  2  3
2  4  5
3  6  7
4  8  9
\>>> m \= df % 3 \== 0
\>>> df.where(m, \-df)
   A  B
0  0 -1
1 -2  3
2 -4 -5
3  6 -7
4 -8  9
\>>> df.where(m, \-df) \== np.where(m, df, \-df)
      A     B
0  True  True
1  True  True
2  True  True
3  True  True
4  True  True
\>>> df.where(m, \-df) \== df.mask(~m, \-df)
      A     B
0  True  True
1  True  True
2  True  True
3  True  True
4  True  True

Copy to clipboard

On this page