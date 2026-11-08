[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.map.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.map.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.map.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.map.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.map.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.map.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.map.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.map.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.map.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.map.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.map.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.map.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.map[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas-io-formats-style-styler-map "Link to this heading")

======================================================================================================================================================================================

Styler.map(_func_, _subset\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2284-L2344)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "Link to this definition")

Apply a CSS-styling function elementwise.

Updates the HTML representation with the result.

Parameters:

**func**function

`func` should take a scalar and return a string.

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**\*\*kwargs**dict

Pass along to `func`.

Returns:

Styler

Instance of class with CSS-styling function applied elementwise.

See also

[`Styler.map_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map_index.html#pandas.io.formats.style.Styler.map_index "pandas.io.formats.style.Styler.map_index")

Apply a CSS-styling function to headers elementwise.

[`Styler.apply_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html#pandas.io.formats.style.Styler.apply_index "pandas.io.formats.style.Styler.apply_index")

Apply a CSS-styling function to headers level-wise.

[`Styler.apply`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")

Apply a CSS-styling function column-wise, row-wise, or table-wise.

Notes

The elements of the output of `func` should be CSS styles as strings, in the format ‘attribute: value; attribute2: value2; …’ or, if nothing is to be applied to that element, an empty string or `None`.

Examples

\>>> def color\_negative(v, color):
...     return f"color: {color};" if v < 0 else None
\>>> df \= pd.DataFrame(np.random.randn(5, 2), columns\=\["A", "B"\])
\>>> df.style.map(color\_negative, color\="red")

Copy to clipboard

Using `subset` to restrict application to a single column or multiple columns

\>>> df.style.map(color\_negative, color\="red", subset\="A")
...
\>>> df.style.map(color\_negative, color\="red", subset\=\["A", "B"\])
...

Copy to clipboard

Using a 2d input to `subset` to select rows in addition to columns

\>>> df.style.map(
...     color\_negative, color\="red", subset\=(\[0, 1, 2\], slice(None))
... )
\>>> df.style.map(color\_negative, color\="red", subset\=(slice(0, 5, 2), "A"))
...

Copy to clipboard

See [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 user guide for more details.

On this page