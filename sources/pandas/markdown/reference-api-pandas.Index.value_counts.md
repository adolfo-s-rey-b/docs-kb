[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.value_counts.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.value\_counts[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.value_counts.html#pandas-index-value-counts "Link to this heading")

============================================================================================================================================================

Index.value\_counts(_normalize\=False_, _sort\=True_, _ascending\=False_, _bins\=None_, _dropna\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/base.py#L1080-L1207)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.value_counts.html#pandas.Index.value_counts "Link to this definition")

Return a Series containing counts of unique values.

The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.

Parameters:

**normalize**bool, default False

If True then the object returned will contain the relative frequencies of the unique values.

**sort**bool, default True

Stable sort by frequencies when True. Preserve the order of the data when False.

Changed in version 3.0.0: Prior to 3.0.0, the sort was unstable.

**ascending**bool, default False

Sort in ascending order.

**bins**int, optional

Rather than count values, group them into half-open bins, a convenience for `pd.cut`, only works with numeric data.

**dropna**bool, default True

Don’t include counts of NaN.

Returns:

Series

Series containing counts of unique values.

See also

[`Series.count`](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas.Series.count "pandas.Series.count")

Number of non-NA elements in a Series.

[`DataFrame.count`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count "pandas.DataFrame.count")

Number of non-NA elements in a DataFrame.

[`DataFrame.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas.DataFrame.value_counts "pandas.DataFrame.value_counts")

Equivalent method on DataFrames.

Examples

\>>> index \= pd.Index(\[3, 1, 2, 3, 4, np.nan\])
\>>> index.value\_counts()
3.0    2
1.0    1
2.0    1
4.0    1
Name: count, dtype: int64

Copy to clipboard

With normalize set to True, returns the relative frequency by dividing all values by the sum of values.

\>>> s \= pd.Series(\[3, 1, 2, 3, 4, np.nan\])
\>>> s.value\_counts(normalize\=True)
3.0    0.4
1.0    0.2
2.0    0.2
4.0    0.2
Name: proportion, dtype: float64

Copy to clipboard

**bins**

Bins can be useful for going from a continuous variable to a categorical variable; instead of counting unique apparitions of values, divide the index in the specified number of half-open bins.

\>>> s.value\_counts(bins\=3)
(0.996, 2.0\]    2
(2.0, 3.0\]      2
(3.0, 4.0\]      1
Name: count, dtype: int64

Copy to clipboard

**dropna**

With dropna set to False we can also see NaN index values.

\>>> s.value\_counts(dropna\=False)
3.0    2
1.0    1
2.0    1
4.0    1
NaN    1
Name: count, dtype: int64

Copy to clipboard

**Categorical Dtypes**

Rows with categorical type will be counted as one group if they have same categories and order. In the example below, even though `a`, `c`, and `d` all have the same data types of `category`, only `c` and `d` will be counted as one group since `a` doesn’t have the same categories.

\>>> df \= pd.DataFrame({"a": \[1\], "b": \["2"\], "c": \[3\], "d": \[3\]})
\>>> df \= df.astype({"a": "category", "c": "category", "d": "category"})
\>>> df
   a  b  c  d
0  1  2  3  3

Copy to clipboard

\>>> df.dtypes
a    category
b      str
c    category
d    category
dtype: object

Copy to clipboard

\>>> df.dtypes.value\_counts()
category    2
category    1
str         1
Name: count, dtype: int64

Copy to clipboard

On this page