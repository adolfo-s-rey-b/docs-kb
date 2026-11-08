[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.highlight_between.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.highlight\_between[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas-io-formats-style-styler-highlight-between "Link to this heading")

=================================================================================================================================================================================================================================

Styler.highlight\_between(_subset\=None_, _color\='yellow'_, _axis\=0_, _left\=None_, _right\=None_, _inclusive\='both'_, _props\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L3774-L3891)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas.io.formats.style.Styler.highlight_between "Link to this definition")

Highlight a defined range with a style.

Applies a background color or custom CSS properties to cells whose values fall within the range defined by `left` and `right` bounds.

Parameters:

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**color**str, default ‘yellow’

Background color to use for highlighting.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

If `left` or `right` given as sequence, axis along which to apply those boundaries. See examples.

**left**scalar or datetime-like, or sequence or array-like, default None

Left bound for defining the range.

**right**scalar or datetime-like, or sequence or array-like, default None

Right bound for defining the range.

**inclusive**{‘both’, ‘neither’, ‘left’, ‘right’}

Identify whether bounds are closed or open.

**props**str, default None

CSS properties to use for highlighting. If `props` is given, `color` is not used.

Returns:

Styler

Instance of class with range highlighted in given style.

See also

[`Styler.highlight_null`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#pandas.io.formats.style.Styler.highlight_null "pandas.io.formats.style.Styler.highlight_null")

Highlight missing values with a style.

[`Styler.highlight_max`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_max.html#pandas.io.formats.style.Styler.highlight_max "pandas.io.formats.style.Styler.highlight_max")

Highlight the maximum with a style.

[`Styler.highlight_min`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#pandas.io.formats.style.Styler.highlight_min "pandas.io.formats.style.Styler.highlight_min")

Highlight the minimum with a style.

[`Styler.highlight_quantile`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#pandas.io.formats.style.Styler.highlight_quantile "pandas.io.formats.style.Styler.highlight_quantile")

Highlight values defined by a quantile with a style.

Notes

If `left` is `None` only the right bound is applied. If `right` is `None` only the left bound is applied. If both are `None` all values are highlighted.

`axis` is only needed if `left` or `right` are provided as a sequence or an array-like object for aligning the shapes. If `left` and `right` are both scalars then all `axis` inputs will give the same result.

This function only works with compatible `dtypes`. For example a datetime-like region can only use equivalent datetime-like `left` and `right` arguments. Use `subset` to control regions which have multiple `dtypes`.

Examples

Basic usage

\>>> df \= pd.DataFrame(
...     {
...         "One": \[1.2, 1.6, 1.5\],
...         "Two": \[2.9, 2.1, 2.5\],
...         "Three": \[3.1, 3.2, 3.8\],
...     }
... )
\>>> df.style.highlight\_between(left\=2.1, right\=2.9)

Copy to clipboard

![../../_images/hbetw_basic.png](https://pandas.pydata.org/docs/_images/hbetw_basic.png)

Using a range input sequence along an `axis`, in this case setting a `left` and `right` for each column individually

\>>> df.style.highlight\_between(
...     left\=\[1.4, 2.4, 3.4\], right\=\[1.6, 2.6, 3.6\], axis\=1, color\="#fffd75"
... )

Copy to clipboard

![../../_images/hbetw_seq.png](https://pandas.pydata.org/docs/_images/hbetw_seq.png)

Using `axis=None` and providing the `left` argument as an array that matches the input DataFrame, with a constant `right`

\>>> df.style.highlight\_between(
...     left\=\[\[2, 2, 3\], \[2, 2, 3\], \[3, 3, 3\]\],
...     right\=3.5,
...     axis\=None,
...     color\="#fffd75",
... )

Copy to clipboard

![../../_images/hbetw_axNone.png](https://pandas.pydata.org/docs/_images/hbetw_axNone.png)

Using `props` instead of default background coloring

\>>> df.style.highlight\_between(
...     left\=1.5, right\=3.5, props\="font-weight:bold;color:#e83e8c"
... )

Copy to clipboard

![../../_images/hbetw_props.png](https://pandas.pydata.org/docs/_images/hbetw_props.png)

On this page