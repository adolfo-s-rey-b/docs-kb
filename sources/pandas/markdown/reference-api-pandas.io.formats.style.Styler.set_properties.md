[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_properties.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_properties.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_properties[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html#pandas-io-formats-style-styler-set-properties "Link to this heading")

========================================================================================================================================================================================================================

Styler.set\_properties(_subset\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L3427-L3471)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html#pandas.io.formats.style.Styler.set_properties "Link to this definition")

Set defined CSS-properties to each `<td>` HTML element for the given subset.

This is a convenience method that applies one or more CSS property-value pairs uniformly to every `<td>` element in the specified subset. It wraps [`Styler.map()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")
 with a function that returns the given CSS properties regardless of the cell data.

Parameters:

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**\*\*kwargs**dict

A dictionary of property, value pairs to be set for each cell.

Returns:

Styler

Instance of class with CSS-properties set for each `<td>` HTML element

in the given subset

See also

[`Styler.set_sticky`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html#pandas.io.formats.style.Styler.set_sticky "pandas.io.formats.style.Styler.set_sticky")

Add CSS to permanently display the index or column headers in a scrolling frame.

Notes

This is a convenience methods which wraps the [`Styler.map()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")
 calling a function returning the CSS-properties independently of the data.

Examples

\>>> df \= pd.DataFrame(np.random.randn(10, 4))
\>>> df.style.set\_properties(color\="white", align\="right")
\>>> df.style.set\_properties(\*\*{"background-color": "yellow"})

Copy to clipboard

See [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 user guide for more details.

On this page