[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.apply.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.apply.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.apply.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.apply.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.apply.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.apply.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.apply.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.apply.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.apply.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.apply.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.apply.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.apply.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.apply[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas-io-formats-style-styler-apply "Link to this heading")

============================================================================================================================================================================================

Styler.apply(_func_, _axis\=0_, _subset\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2009-L2098)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "Link to this definition")

Apply a CSS-styling function column-wise, row-wise, or table-wise.

Updates the HTML representation with the result.

Parameters:

**func**function

`func` should take a Series if `axis` in \[0,1\] and return a list-like object of same length, or a Series, not necessarily of same length, with valid index labels considering `subset`. `func` should take a DataFrame if `axis` is `None` and return either an ndarray with the same shape or a DataFrame, not necessarily of the same shape, with valid index and columns labels considering `subset`.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

Apply to each column (`axis=0` or `'index'`), to each row (`axis=1` or `'columns'`), or to the entire DataFrame at once with `axis=None`.

**subset**label, array-like, IndexSlice, optional

A valid 2d input to DataFrame.loc\[<subset>\], or, in the case of a 1d input or single key, to DataFrame.loc\[:, <subset>\] where the columns are prioritised, to limit `data` to _before_ applying the function.

**\*\*kwargs**dict

Pass along to `func`.

Returns:

Styler

Instance of class with CSS applied to its HTML representation.

See also

[`Styler.map_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map_index.html#pandas.io.formats.style.Styler.map_index "pandas.io.formats.style.Styler.map_index")

Apply a CSS-styling function to headers elementwise.

[`Styler.apply_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html#pandas.io.formats.style.Styler.apply_index "pandas.io.formats.style.Styler.apply_index")

Apply a CSS-styling function to headers level-wise.

[`Styler.map`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")

Apply a CSS-styling function elementwise.

Notes

The elements of the output of `func` should be CSS styles as strings, in the format ‘attribute: value; attribute2: value2; …’ or, if nothing is to be applied to that element, an empty string or `None`.

This is similar to `DataFrame.apply`, except that `axis=None` applies the function to the entire DataFrame at once, rather than column-wise or row-wise.

Examples

\>>> def highlight\_max(x, color):
...     return np.where(x \== np.nanmax(x.to\_numpy()), f"color: {color};", None)
\>>> df \= pd.DataFrame(np.random.randn(5, 2), columns\=\["A", "B"\])
\>>> df.style.apply(highlight\_max, color\="red")
\>>> df.style.apply(highlight\_max, color\="blue", axis\=1)
\>>> df.style.apply(highlight\_max, color\="green", axis\=None)

Copy to clipboard

Using `subset` to restrict application to a single column or multiple columns

\>>> df.style.apply(highlight\_max, color\="red", subset\="A")
...
\>>> df.style.apply(highlight\_max, color\="red", subset\=\["A", "B"\])
...

Copy to clipboard

Using a 2d input to `subset` to select rows in addition to columns

\>>> df.style.apply(highlight\_max, color\="red", subset\=(\[0, 1, 2\], slice(None)))
...
\>>> df.style.apply(highlight\_max, color\="red", subset\=(slice(0, 5, 2), "A"))
...

Copy to clipboard

Using a function which returns a Series / DataFrame of unequal length but containing valid index labels

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\], \[4, 6\]\], index\=\["A1", "A2", "Total"\])
\>>> total\_style \= pd.Series("font-weight: bold;", index\=\["Total"\])
\>>> df.style.apply(lambda s: total\_style)

Copy to clipboard

See [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 user guide for more details.

On this page