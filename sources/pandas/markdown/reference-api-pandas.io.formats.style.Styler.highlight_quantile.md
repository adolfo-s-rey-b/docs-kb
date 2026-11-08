[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.highlight\_quantile[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#pandas-io-formats-style-styler-highlight-quantile "Link to this heading")

====================================================================================================================================================================================================================================

Styler.highlight\_quantile(_subset\=None_, _color\='yellow'_, _axis\=0_, _q\_left\=0.0_, _q\_right\=1.0_, _interpolation\='linear'_, _inclusive\='both'_, _props\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L3893-L4008)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#pandas.io.formats.style.Styler.highlight_quantile "Link to this definition")

Highlight values defined by a quantile with a style.

Applies a background color or custom CSS properties to cells whose values fall within the quantile range specified by `q_left` and `q_right`.

Parameters:

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**color**str, default ‘yellow’

Background color to use for highlighting.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

Axis along which to determine and highlight quantiles. If `None` quantiles are measured over the entire DataFrame. See examples.

**q\_left**float, default 0

Left bound, in \[0, q\_right), for the target quantile range.\
\
**q\_right**float, default 1\
\
Right bound, in (q\_left, 1\], for the target quantile range.

**interpolation**{‘linear’, ‘lower’, ‘higher’, ‘midpoint’, ‘nearest’}

Argument passed to `Series.quantile` or `DataFrame.quantile` for quantile estimation.

**inclusive**{‘both’, ‘neither’, ‘left’, ‘right’}

Identify whether quantile bounds are closed or open.

**props**str, default None

CSS properties to use for highlighting. If `props` is given, `color` is not used.

Returns:

Styler

Instance of class where values in quantile highlighted with given style.

See also

[`Styler.highlight_null`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#pandas.io.formats.style.Styler.highlight_null "pandas.io.formats.style.Styler.highlight_null")

Highlight missing values with a style.

[`Styler.highlight_max`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_max.html#pandas.io.formats.style.Styler.highlight_max "pandas.io.formats.style.Styler.highlight_max")

Highlight the maximum with a style.

[`Styler.highlight_min`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#pandas.io.formats.style.Styler.highlight_min "pandas.io.formats.style.Styler.highlight_min")

Highlight the minimum with a style.

[`Styler.highlight_between`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas.io.formats.style.Styler.highlight_between "pandas.io.formats.style.Styler.highlight_between")

Highlight a defined range with a style.

Notes

This function does not work with `str` dtypes.

Examples

Using `axis=None` and apply a quantile to all collective data

\>>> df \= pd.DataFrame(np.arange(10).reshape(2, 5) + 1)
\>>> df.style.highlight\_quantile(axis\=None, q\_left\=0.8, color\="#fffd75")
...

Copy to clipboard

![../../_images/hq_axNone.png](https://pandas.pydata.org/docs/_images/hq_axNone.png)

Or highlight quantiles row-wise or column-wise, in this case by row-wise

\>>> df.style.highlight\_quantile(axis\=1, q\_left\=0.8, color\="#fffd75")
...

Copy to clipboard

![../../_images/hq_ax1.png](https://pandas.pydata.org/docs/_images/hq_ax1.png)

Use `props` instead of default background coloring

\>>> df.style.highlight\_quantile(
...     axis\=None,
...     q\_left\=0.2,
...     q\_right\=0.8,
...     props\="font-weight:bold;color:#e83e8c",
... )

Copy to clipboard

![../../_images/hq_props.png](https://pandas.pydata.org/docs/_images/hq_props.png)

On this page