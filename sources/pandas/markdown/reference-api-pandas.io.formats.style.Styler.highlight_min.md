[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.highlight\_min[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#pandas-io-formats-style-styler-highlight-min "Link to this heading")

=====================================================================================================================================================================================================================

Styler.highlight\_min(_subset\=None_, _color\='yellow'_, _axis\=0_, _props\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L3715-L3772)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#pandas.io.formats.style.Styler.highlight_min "Link to this definition")

Highlight the minimum with a style.

Applies a background color or custom CSS properties to cells containing the minimum value along the specified axis.

Parameters:

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**color**str, default ‘yellow’

Background color to use for highlighting.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

Apply to each column (`axis=0` or `'index'`), to each row (`axis=1` or `'columns'`), or to the entire DataFrame at once with `axis=None`.

**props**str, default None

CSS properties to use for highlighting. If `props` is given, `color` is not used.

Returns:

Styler

Instance of class where min value is highlighted in given style.

See also

[`Styler.highlight_null`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#pandas.io.formats.style.Styler.highlight_null "pandas.io.formats.style.Styler.highlight_null")

Highlight missing values with a style.

[`Styler.highlight_max`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_max.html#pandas.io.formats.style.Styler.highlight_max "pandas.io.formats.style.Styler.highlight_max")

Highlight the maximum with a style.

[`Styler.highlight_between`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas.io.formats.style.Styler.highlight_between "pandas.io.formats.style.Styler.highlight_between")

Highlight a defined range with a style.

[`Styler.highlight_quantile`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#pandas.io.formats.style.Styler.highlight_quantile "pandas.io.formats.style.Styler.highlight_quantile")

Highlight values defined by a quantile with a style.

Examples

\>>> df \= pd.DataFrame({"A": \[2, 1\], "B": \[3, 4\]})
\>>> df.style.highlight\_min(color\="yellow")

Copy to clipboard

Please see: [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page