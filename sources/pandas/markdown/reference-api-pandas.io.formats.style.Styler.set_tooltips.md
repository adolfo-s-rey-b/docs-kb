[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_tooltips[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html#pandas-io-formats-style-styler-set-tooltips "Link to this heading")

==================================================================================================================================================================================================================

Styler.set\_tooltips(_ttips_, _props\=None_, _css\_class\=None_, _as\_title\_attribute\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L388-L514)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html#pandas.io.formats.style.Styler.set_tooltips "Link to this definition")

Set the DataFrame of strings on `Styler` generating `:hover` tooltips.

These string based tooltips are only applicable to `<td>` HTML elements, and cannot be used for column or index headers.

Parameters:

**ttips**DataFrame

DataFrame containing strings that will be translated to tooltips, mapped by identical column and index values that must exist on the underlying Styler data. None, NaN values, and empty strings will be ignored and not affect the rendered HTML.

**props**list-like or str, optional

List of (attr, value) tuples or a valid CSS string. If `None` adopts the internal default values described in notes.

**css\_class**str, optional

Name of the tooltip class used in CSS, should conform to HTML standards. Only useful if integrating tooltips with external CSS. If `None` uses the internal default value ‘pd-t’.

**as\_title\_attribute**bool, default False

Add the tooltip text as title attribute to resultant <td> element. If True then props and css\_class arguments are ignored.

Returns:

Styler

Instance of class with DataFrame set for strings on `Styler`

generating `:hover` tooltips.

See also

[`Styler.set_table_attributes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#pandas.io.formats.style.Styler.set_table_attributes "pandas.io.formats.style.Styler.set_table_attributes")

Set the table attributes added to the `<table>` HTML element.

[`Styler.set_table_styles`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#pandas.io.formats.style.Styler.set_table_styles "pandas.io.formats.style.Styler.set_table_styles")

Set the table styles included within the `<style>` HTML element.

Notes

Tooltips are created by adding <span class=”pd-t”></span> to each data cell and then manipulating the table level CSS to attach pseudo hover and pseudo after selectors to produce the required the results.

The default properties for the tooltip CSS class are:

*   visibility: hidden
    
*   position: absolute
    
*   z-index: 1
    
*   background-color: black
    
*   color: white
    
*   transform: translate(-20px, -20px)
    

The property ‘visibility: hidden;’ is a key prerequisite to the hover functionality, and should always be included in any manual properties specification, using the `props` argument.

Tooltips are not designed to be efficient, and can add large amounts of additional HTML for larger tables, since they also require that `cell_ids` is forced to True.

If multiline tooltips are required, or if styling is not required and/or space is of concern, then utilizing as\_title\_attribute as True will store the tooltip on the <td> title attribute. This will cause no CSS to be generated nor will the <span> elements. Storing tooltips through the title attribute will mean that tooltip styling effects do not apply.

Examples

Basic application

\>>> df \= pd.DataFrame(data\=\[\[0, 1\], \[2, 3\]\])
\>>> ttips \= pd.DataFrame(
...     data\=\[\["Min", ""\], \[np.nan, "Max"\]\], columns\=df.columns, index\=df.index
... )
\>>> s \= df.style.set\_tooltips(ttips).to\_html()

Copy to clipboard

Optionally controlling the tooltip visual display

\>>> df.style.set\_tooltips(
...     ttips,
...     css\_class\="tt-add",
...     props\=\[\
...         ("visibility", "hidden"),\
...         ("position", "absolute"),\
...         ("z-index", 1),\
...     \],
... )
\>>> df.style.set\_tooltips(
...     ttips,
...     css\_class\="tt-add",
...     props\="visibility:hidden; position:absolute; z-index:1;",
... )
...

Copy to clipboard

Multiline tooltips with smaller size footprint

\>>> df.style.set\_tooltips(ttips, as\_title\_attribute\=True)

Copy to clipboard

On this page