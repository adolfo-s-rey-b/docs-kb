[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_caption.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_caption.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_caption[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html#pandas-io-formats-style-styler-set-caption "Link to this heading")

===============================================================================================================================================================================================================

Styler.set\_caption(_caption_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2555-L2602)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html#pandas.io.formats.style.Styler.set_caption "Link to this definition")

Set the text added to a `<caption>` HTML element.

This method sets the table caption that is rendered as a `<caption>` element in HTML output or as a `\caption` command in LaTeX output. For LaTeX, a tuple of two strings can be provided to specify both a full caption and a short caption.

Parameters:

**caption**str, tuple, list

For HTML output either the string input is used or the first element of the tuple. For LaTeX the string input provides a caption and the additional tuple input allows for full captions and short captions, in that order.

Returns:

Styler

Instance of class with text set for `<caption>` HTML element.

See also

[`Styler.set_td_classes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas.io.formats.style.Styler.set_td_classes "pandas.io.formats.style.Styler.set_td_classes")

Set the `class` attribute of `<td>` HTML elements.

[`Styler.set_tooltips`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html#pandas.io.formats.style.Styler.set_tooltips "pandas.io.formats.style.Styler.set_tooltips")

Set the DataFrame of strings on `Styler` generating `:hover` tooltips.

[`Styler.set_uuid`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_uuid.html#pandas.io.formats.style.Styler.set_uuid "pandas.io.formats.style.Styler.set_uuid")

Set the uuid applied to `id` attributes of HTML elements.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> df.style.set\_caption("test")

Copy to clipboard

Please see: [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page