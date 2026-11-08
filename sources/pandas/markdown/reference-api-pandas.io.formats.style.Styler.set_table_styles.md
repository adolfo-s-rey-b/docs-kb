[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_table\_styles[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#pandas-io-formats-style-styler-set-table-styles "Link to this heading")

===============================================================================================================================================================================================================================

Styler.set\_table\_styles(_table\_styles\=None_, _axis\=0_, _overwrite\=True_, _css\_class\_names\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2756-L2902)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#pandas.io.formats.style.Styler.set_table_styles "Link to this definition")

Set the table styles included within the `<style>` HTML element.

This function can be used to style the entire table, columns, rows or specific HTML selectors.

Parameters:

**table\_styles**list or dict

If supplying a list, each individual table\_style should be a dictionary with `selector` and `props` keys. `selector` should be a CSS selector that the style will be applied to (automatically prefixed by the table’s UUID) and `props` should be a list of tuples with `(attribute, value)`. If supplying a dict, the dict keys should correspond to column names or index values, depending upon the specified axis argument. These will be mapped to row or col CSS selectors. MultiIndex values as dict keys should be in their respective tuple form. The dict values should be a list as specified in the form with CSS selectors and props that will be applied to the specified row or column.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

Apply to each column (`axis=0` or `'index'`), to each row (`axis=1` or `'columns'`). Only used if table\_styles is dict.

**overwrite**bool, default True

Styles are replaced if True, or extended if False. CSS rules are preserved so most recent styles set will dominate if selectors intersect.

**css\_class\_names**dict, optional

A dict of strings used to replace the default CSS classes described below.

Returns:

Styler

Instance of class with specified table styles set.

See also

[`Styler.set_td_classes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas.io.formats.style.Styler.set_td_classes "pandas.io.formats.style.Styler.set_td_classes")

Set the DataFrame of strings added to the `class` attribute of `<td>` HTML elements.

[`Styler.set_table_attributes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#pandas.io.formats.style.Styler.set_table_attributes "pandas.io.formats.style.Styler.set_table_attributes")

Set the table attributes added to the `<table>` HTML element.

Notes

The default CSS classes dict, whose values can be replaced is as follows:

css\_class\_names \= {
    "row\_heading": "row\_heading",
    "col\_heading": "col\_heading",
    "index\_name": "index\_name",
    "col": "col",
    "row": "row",
    "col\_trim": "col\_trim",
    "row\_trim": "row\_trim",
    "level": "level",
    "data": "data",
    "blank": "blank",
    "foot": "foot",
}

Copy to clipboard

Examples

\>>> df \= pd.DataFrame(np.random.randn(10, 4), columns\=\["A", "B", "C", "D"\])
\>>> df.style.set\_table\_styles(
...     \[{"selector": "tr:hover", "props": \[("background-color", "yellow")\]}\]
... )

Copy to clipboard

Or with CSS strings

\>>> df.style.set\_table\_styles(
...     \[\
...         {\
...             "selector": "tr:hover",\
...             "props": "background-color: yellow; font-size: 1em;",\
...         }\
...     \]
... )

Copy to clipboard

Adding column styling by name

\>>> df.style.set\_table\_styles(
...     {
...         "A": \[{"selector": "", "props": \[("color", "red")\]}\],
...         "B": \[{"selector": "td", "props": "color: blue;"}\],
...     },
...     overwrite\=False,
... )

Copy to clipboard

Adding row styling

\>>> df.style.set\_table\_styles(
...     {0: \[{"selector": "td:hover", "props": \[("font-size", "25px")\]}\]},
...     axis\=1,
...     overwrite\=False,
... )

Copy to clipboard

See [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 user guide for more details.

On this page