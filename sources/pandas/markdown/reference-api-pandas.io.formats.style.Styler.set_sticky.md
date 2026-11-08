[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_sticky.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_sticky[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html#pandas-io-formats-style-styler-set-sticky "Link to this heading")

============================================================================================================================================================================================================

Styler.set\_sticky(_axis\=0_, _pixel\_size\=None_, _levels\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2604-L2754)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html#pandas.io.formats.style.Styler.set_sticky "Link to this definition")

Add CSS to permanently display the index or column headers in a scrolling frame.

This method applies CSS `position: sticky` rules so that the index or column headers remain visible while scrolling through large tables. It supports both regular and MultiIndex axes, with configurable pixel sizes for header cell dimensions.

Parameters:

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Whether to make the index or column headers sticky.

**pixel\_size**int, optional

Required to configure the width of index cells or the height of column header cells when sticking a MultiIndex (or with a named Index). Defaults to 75 and 25 respectively.

**levels**int, str, list, optional

If `axis` is a MultiIndex the specific levels to stick. If `None` will stick all levels.

Returns:

Styler

Instance of class with CSS set for permanently displaying headers

in scrolling frame.

See also

[`Styler.set_properties`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html#pandas.io.formats.style.Styler.set_properties "pandas.io.formats.style.Styler.set_properties")

Set defined CSS-properties to each `<td>` HTML element for the given subset.

Notes

This method uses the CSS ‘position: sticky;’ property to display. It is designed to work with visible axes, therefore both:

> *   styler.set\_sticky(axis=”index”).hide(axis=”index”)
>     
> *   styler.set\_sticky(axis=”columns”).hide(axis=”columns”)
>     

may produce strange behaviour due to CSS controls with missing elements.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> df.style.set\_sticky(axis\="index")

Copy to clipboard

Please see: [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page