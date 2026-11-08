[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_td\_classes[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas-io-formats-style-styler-set-td-classes "Link to this heading")

=========================================================================================================================================================================================================================

Styler.set\_td\_classes(_classes_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L1690-L1777)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas.io.formats.style.Styler.set_td_classes "Link to this definition")

Set the `class` attribute of `<td>` HTML elements.

This method accepts a DataFrame of CSS class names and maps them to the corresponding `<td>` elements in the rendered HTML table using matching index and column keys. It can be used in combination with `Styler.set_table_styles` to build a self-contained CSS styling solution.

Parameters:

**classes**DataFrame

DataFrame containing strings that will be translated to CSS classes, mapped by identical column and index key values that must exist on the underlying Styler data. None, NaN values, and empty strings will be ignored and not affect the rendered HTML.

Returns:

Styler

Instance of class with `class` attribute set for `<td>`

HTML elements.

See also

[`Styler.set_table_styles`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#pandas.io.formats.style.Styler.set_table_styles "pandas.io.formats.style.Styler.set_table_styles")

Set the table styles included within the `<style>` HTML element.

[`Styler.set_table_attributes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#pandas.io.formats.style.Styler.set_table_attributes "pandas.io.formats.style.Styler.set_table_attributes")

Set the table attributes added to the `<table>` HTML element.

Notes

Can be used in combination with `Styler.set_table_styles` to define an internal CSS solution without reference to external CSS files.

Examples

\>>> df \= pd.DataFrame(data\=\[\[1, 2, 3\], \[4, 5, 6\]\], columns\=\["A", "B", "C"\])
\>>> classes \= pd.DataFrame(
...     \[\["min-val red", "", "blue"\], \["red", None, "blue max-val"\]\],
...     index\=df.index,
...     columns\=df.columns,
... )
\>>> df.style.set\_td\_classes(classes)

Copy to clipboard

Using MultiIndex columns and a classes DataFrame as a subset of the underlying,

\>>> df \= pd.DataFrame(
...     \[\[1, 2\], \[3, 4\]\],
...     index\=\["a", "b"\],
...     columns\=\[\["level0", "level0"\], \["level1a", "level1b"\]\],
... )
\>>> classes \= pd.DataFrame(
...     \["min-val"\], index\=\["a"\], columns\=\[\["level0"\], \["level1a"\]\]
... )
\>>> df.style.set\_td\_classes(classes)

Copy to clipboard

Form of the output with new additional css classes,

\>>> from pandas.io.formats.style import Styler
\>>> df \= pd.DataFrame(\[\[1\]\])
\>>> css \= pd.DataFrame(\[\["other-class"\]\])
\>>> s \= Styler(df, uuid\="\_", cell\_ids\=False).set\_td\_classes(css)
\>>> s.hide(axis\=0).to\_html()
'<style type="text/css"></style>'
'<table id="T\_\_">'
'  <thead>'
'    <tr><th class="col\_heading level0 col0" >0</th></tr>'
'  </thead>'
'  <tbody>'
'    <tr><td class="data row0 col0 other-class" >1</td></tr>'
'  </tbody>'
'</table>'

Copy to clipboard

On this page