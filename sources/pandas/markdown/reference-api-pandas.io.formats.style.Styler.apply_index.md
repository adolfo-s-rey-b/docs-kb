[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.apply_index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.apply_index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.apply\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html#pandas-io-formats-style-styler-apply-index "Link to this heading")

===============================================================================================================================================================================================================

Styler.apply\_index(_func_, _axis\=0_, _level\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2122-L2197)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html#pandas.io.formats.style.Styler.apply_index "Link to this definition")

Apply a CSS-styling function to the index or column headers, level-wise.

Updates the HTML representation with the result.

Added in version 2.1.0: Styler.applymap\_index was deprecated and renamed to Styler.map\_index.

Parameters:

**func**function

`func` should take a Series and return a string array of the same length.

**axis**{0, 1, “index”, “columns”}

The headers over which to apply the function.

**level**int, str, list, optional

If index is MultiIndex the level(s) over which to apply the function.

**\*\*kwargs**dict

Pass along to `func`.

Returns:

Styler

Instance of class with CSS applied to its HTML representation.

See also

[`Styler.map_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map_index.html#pandas.io.formats.style.Styler.map_index "pandas.io.formats.style.Styler.map_index")

Apply a CSS-styling function to headers elementwise.

[`Styler.apply`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")

Apply a CSS-styling function column-wise, row-wise, or table-wise.

[`Styler.map`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")

Apply a CSS-styling function elementwise.

Notes

Each input to `func` will be the index as a Series, if an Index, or a level of a MultiIndex. The output of `func` should be an identically sized array of CSS styles as strings, in the format ‘attribute: value; attribute2: value2; …’ or, if nothing is to be applied to that element, an empty string or `None`.

Examples

Basic usage to conditionally highlight values in the index.

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], index\=\["A", "B"\])
\>>> def color\_b(label):
...     return np.where(label \== "B", "background-color: yellow;", "")
\>>> df.style.apply\_index(color\_b)

Copy to clipboard

![../../_images/appmaphead1.png](https://pandas.pydata.org/docs/_images/appmaphead1.png)

Selectively applying to specific levels of MultiIndex columns.

\>>> midx \= pd.MultiIndex.from\_product(\[\["ix", "jy"\], \[0, 1\], \["x3", "z4"\]\])
\>>> df \= pd.DataFrame(\[np.arange(8)\], columns\=midx)
\>>> def highlight\_x(label):
...     return \["background-color: yellow;" if "x" in v else "" for v in label\]
\>>> df.style.apply\_index(
...     highlight\_x, axis\="columns", level\=\[0, 2\]
... )

Copy to clipboard

![../../_images/appmaphead2.png](https://pandas.pydata.org/docs/_images/appmaphead2.png)

On this page