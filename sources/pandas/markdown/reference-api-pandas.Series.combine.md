[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.combine.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.combine.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.combine.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.combine.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.combine.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.combine.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.combine.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.combine.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.combine.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.combine.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.combine.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.combine.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.combine[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html#pandas-series-combine "Link to this heading")

===============================================================================================================================================

Series.combine(_other_, _func_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L3702-L3839)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html#pandas.Series.combine "Link to this definition")

Combine the Series with a Series or scalar according to func.

Combine the Series and other using func to perform elementwise selection for combined Series. fill\_value is assumed when value is not present at some index from one of the two Series being combined. The result index is the union of the two indexes. If a label is duplicated, its occurrences are paired in order: the first occurrence in the Series with the first in other, the second with the second, and so on; an occurrence with no counterpart is paired with fill\_value.

Parameters:

**other**Series or scalar

The value(s) to be combined with the Series.

**func**function

Function that takes two scalars as inputs and returns an element.

**fill\_value**scalar, optional

The value to assume when an index is missing from one Series or the other. The default specifies to use the appropriate NA value for the underlying dtype of the Series.

Returns:

Series

The result of combining the Series with the other object.

See also

[`Series.combine_first`](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html#pandas.Series.combine_first "pandas.Series.combine_first")

Combine Series values, choosing the calling Series’ values first.

Examples

Consider 2 Datasets `s1` and `s2` containing highest clocked speeds of different birds.

\>>> s1 \= pd.Series({"falcon": 330.0, "eagle": 160.0})
\>>> s1
falcon    330.0
eagle     160.0
dtype: float64
\>>> s2 \= pd.Series({"falcon": 345.0, "eagle": 200.0, "duck": 30.0})
\>>> s2
falcon    345.0
eagle     200.0
duck       30.0
dtype: float64

Copy to clipboard

Now, to combine the two datasets and view the highest speeds of the birds across the two datasets

\>>> s1.combine(s2, max)
duck        NaN
eagle     200.0
falcon    345.0
dtype: float64

Copy to clipboard

In the previous example, the resulting value for duck is missing, because the maximum of a NaN and a float is a NaN. So, in the example, we set `fill_value=0`, so the maximum value returned will be the value from some dataset.

\>>> s1.combine(s2, max, fill\_value\=0)
duck       30.0
eagle     200.0
falcon    345.0
dtype: float64

Copy to clipboard

Occurrences of a duplicated label are paired in order. Below, the first `"a"` in `s3` is combined with the `"a"` in `s4`, while the second has no counterpart and is paired with `fill_value`.

\>>> s3 \= pd.Series(\[1, 2, 3\], index\=\["a", "a", "b"\])
\>>> s4 \= pd.Series(\[10, 20\], index\=\["a", "b"\])
\>>> s3.combine(s4, lambda x, y: x + y, fill\_value\=0)
a    11
a     2
b    23
dtype: int64

Copy to clipboard

On this page