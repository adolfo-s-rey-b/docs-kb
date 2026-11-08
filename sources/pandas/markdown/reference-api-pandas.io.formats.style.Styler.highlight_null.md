[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.highlight_null.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.highlight\_null[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#pandas-io-formats-style-styler-highlight-null "Link to this heading")

========================================================================================================================================================================================================================

Styler.highlight\_null(_color\='red'_, _subset\=None_, _props\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L3604-L3654)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#pandas.io.formats.style.Styler.highlight_null "Link to this definition")

Highlight missing values with a style.

Applies a background color or custom CSS properties to cells containing missing (NaN) values in the DataFrame.

Parameters:

**color**str, default ‘red’

Background color to use for highlighting.

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**props**str, default None

CSS properties to use for highlighting. If `props` is given, `color` is not used.

Returns:

Styler

Instance of class where null values are highlighted with given style.

See also

[`Styler.highlight_max`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_max.html#pandas.io.formats.style.Styler.highlight_max "pandas.io.formats.style.Styler.highlight_max")

Highlight the maximum with a style.

[`Styler.highlight_min`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#pandas.io.formats.style.Styler.highlight_min "pandas.io.formats.style.Styler.highlight_min")

Highlight the minimum with a style.

[`Styler.highlight_between`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas.io.formats.style.Styler.highlight_between "pandas.io.formats.style.Styler.highlight_between")

Highlight a defined range with a style.

[`Styler.highlight_quantile`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#pandas.io.formats.style.Styler.highlight_quantile "pandas.io.formats.style.Styler.highlight_quantile")

Highlight values defined by a quantile with a style.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, np.nan\]})
\>>> df.style.highlight\_null(color\="yellow")

Copy to clipboard

Please see: [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page