[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html#pandas-io-formats-style-styler "Link to this heading")

==========================================================================================================================================================================

class pandas.io.formats.style.Styler(_data_, _precision\=None_, _table\_styles\=None_, _uuid\=None_, _caption\=None_, _table\_attributes\=None_, _cell\_ids\=True_, _na\_rep\=None_, _uuid\_len\=5_, _decimal\=None_, _thousands\=None_, _escape\=None_, _formatter\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L82-L4209)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html#pandas.io.formats.style.Styler "Link to this definition")

Helps style a DataFrame or Series according to the data with HTML and CSS.

This class provides methods for styling and formatting a Pandas DataFrame or Series. The styled output can be rendered as HTML or LaTeX, and it supports CSS-based styling, allowing users to control colors, font styles, and other visual aspects of tabular data. It is particularly useful for presenting DataFrame objects in a Jupyter Notebook environment or when exporting styled tables for reports or other human-readable documents.

Parameters:

**data**Series or DataFrame

Data to be styled - either a Series or DataFrame.

**precision**int, optional

Precision to round floats to. If not given defaults to `pandas.options.styler.format.precision`.

**table\_styles**list-like, default None

List of {selector: (attr, value)} dicts; see Notes.

**uuid**str, default None

A unique identifier to avoid CSS collisions; generated automatically.

**caption**str, tuple, default None

String caption to attach to the table. Tuple only used for LaTeX dual captions.

**table\_attributes**str, default None

Items that show up in the opening `<table>` tag in addition to automatic (by default) id.

**cell\_ids**bool, default True

If True, each cell will have an `id` attribute in their HTML tag. The `id` takes the form `T_<uuid>_row<num_row>_col<num_col>` where `<uuid>` is the unique identifier, `<num_row>` is the row number and `<num_col>` is the column number.

**na\_rep**str, optional

Representation for missing values. If `na_rep` is None, no special formatting is applied, and falls back to `pandas.options.styler.format.na_rep`.

**uuid\_len**int, default 5

If `uuid` is not specified, the length of the `uuid` to randomly generate expressed in hex characters, in range \[0, 32\].

**decimal**str, optional

Character used as decimal separator for floats, complex and integers. If not given uses `pandas.options.styler.format.decimal`.

**thousands**str, optional, default None

Character used as thousands separator for floats, complex and integers. If not given uses `pandas.options.styler.format.thousands`.

**escape**str, optional

Use ‘html’ to replace the characters `&`, `<`, `>`, `'`, and `"` in cell display string with HTML-safe sequences.

Use ‘latex’ to replace the characters `&`, `%`, `$`, `#`, `_`, `{`, `}`, `~`, `^`, and `\` in the cell display string with LaTeX-safe sequences. Use ‘latex-math’ to replace the characters the same way as in ‘latex’ mode, except for math substrings, which either are surrounded by two characters `$` or start with the character `\(` and end with `\)`. If not given uses `pandas.options.styler.format.escape`.

**formatter**str, callable, dict, optional

Object to define how values are displayed. See `Styler.format`. If not given uses `pandas.options.styler.format.formatter`.

Attributes

|     |     |
| --- | --- |
| **index** | (data.index Index) |
| **columns** | (data.columns Index) |
| **env** | (Jinja2 jinja2.Environment) |
| **template\_html** | (Jinja2 Template) |
| **template\_html\_table** | (Jinja2 Template) |
| **template\_html\_style** | (Jinja2 Template) |
| **template\_latex** | (Jinja2 Template) |
| **loader** | (Jinja2 Loader) |

See also

`DataFrame.style`

Return a Styler object containing methods for building a styled HTML representation for the DataFrame.

Notes

Warning

`Styler` is primarily intended for use on safe input that you control. When using `Styler` on untrusted, user-provided input to serve HTML, you should set `escape="html"` to prevent security vulnerabilities. See the Jinja2 documentation on escaping HTML for more.

Most styling will be done by passing style functions into `Styler.apply` or `Styler.map`. Style functions should return values with strings containing CSS `'attr: value'` that will be applied to the indicated cells.

If using in the Jupyter notebook, Styler has defined a `_repr_html_` to automatically render itself. Otherwise call Styler.to\_html to get the generated HTML.

CSS classes are attached to the generated HTML

*   Index and Column names include `index_name` and `level<k>` where k is its level in a MultiIndex
    
*   Index label cells include
    
    *   `row_heading`
        
    *   `row<n>` where n is the numeric position of the row
        
    *   `level<k>` where k is the level in a MultiIndex
        
*   Column label cells include
    
    *   `col_heading`
        
    *   `col<n>` where n is the numeric position of the column
        
    *   `level<k>` where k is the level in a MultiIndex
        
*   Blank cells include `blank`
    
*   Data cells include `data`
    
*   Trimmed cells include `col_trim` or `row_trim`.
    

Any, or all, or these classes can be renamed by using the `css_class_names` argument in `Styler.set_table_styles`, giving a value such as _{“row”: “MY\_ROW\_CLASS”, “col\_trim”: “”, “row\_trim”: “”}_.

Examples

\>>> df \= pd.DataFrame(
...     \[\[1.0, 2.0, 3.0\], \[4, 5, 6\]\], index\=\["a", "b"\], columns\=\["A", "B", "C"\]
... )
\>>> pd.io.formats.style.Styler(
...     df, precision\=2, caption\="My table"
... )

Copy to clipboard

Please see: [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

Attributes

|     |     |
| --- | --- |
| [`env`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.env.html#pandas.io.formats.style.Styler.env "pandas.io.formats.style.Styler.env") |     |
| [`loader`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.loader.html#pandas.io.formats.style.Styler.loader "pandas.io.formats.style.Styler.loader") |     |
| `template_dir` |     |
| [`template_html`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_html.html#pandas.io.formats.style.Styler.template_html "pandas.io.formats.style.Styler.template_html") |     |
| [`template_html_style`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_html_style.html#pandas.io.formats.style.Styler.template_html_style "pandas.io.formats.style.Styler.template_html_style") |     |
| [`template_html_table`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_html_table.html#pandas.io.formats.style.Styler.template_html_table "pandas.io.formats.style.Styler.template_html_table") |     |
| [`template_latex`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_latex.html#pandas.io.formats.style.Styler.template_latex "pandas.io.formats.style.Styler.template_latex") |     |
| [`template_string`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_string.html#pandas.io.formats.style.Styler.template_string "pandas.io.formats.style.Styler.template_string") |     |
| [`template_typst`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_typst.html#pandas.io.formats.style.Styler.template_typst "pandas.io.formats.style.Styler.template_typst") |     |
| `this_dir` |     |

Methods

|     |     |
| --- | --- |
| [`apply`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")<br>(func\[, axis, subset\]) | Apply a CSS-styling function column-wise, row-wise, or table-wise. |
| [`apply_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html#pandas.io.formats.style.Styler.apply_index "pandas.io.formats.style.Styler.apply_index")<br>(func\[, axis, level\]) | Apply a CSS-styling function to the index or column headers, level-wise. |
| [`background_gradient`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.background_gradient.html#pandas.io.formats.style.Styler.background_gradient "pandas.io.formats.style.Styler.background_gradient")<br>(\[cmap, low, high, axis, ...\]) | Color the background in a gradient style. |
| [`bar`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.bar.html#pandas.io.formats.style.Styler.bar "pandas.io.formats.style.Styler.bar")<br>(\[subset, axis, color, cmap, width, ...\]) | Draw bar chart in the cell backgrounds. |
| [`clear`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.clear.html#pandas.io.formats.style.Styler.clear "pandas.io.formats.style.Styler.clear")<br>() | Reset the `Styler`, removing any previously applied styles. |
| [`concat`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.concat.html#pandas.io.formats.style.Styler.concat "pandas.io.formats.style.Styler.concat")<br>(other) | Append another Styler to combine the output into a single table. |
| [`export`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas.io.formats.style.Styler.export "pandas.io.formats.style.Styler.export")<br>() | Export the styles applied to the current Styler. |
| [`format`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html#pandas.io.formats.style.Styler.format "pandas.io.formats.style.Styler.format")<br>(\[formatter, subset, na\_rep, ...\]) | Format the text display value of cells. |
| [`format_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "pandas.io.formats.style.Styler.format_index")<br>(\[formatter, axis, level, ...\]) | Format the text display value of index labels or column headers. |
| [`format_index_names`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index_names.html#pandas.io.formats.style.Styler.format_index_names "pandas.io.formats.style.Styler.format_index_names")<br>(\[formatter, axis, level, ...\]) | Format the text display value of index names or column names. |
| [`from_custom_template`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.from_custom_template.html#pandas.io.formats.style.Styler.from_custom_template "pandas.io.formats.style.Styler.from_custom_template")<br>(searchpath\[, ...\]) | Factory function for creating a subclass of `Styler`. |
| [`hide`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html#pandas.io.formats.style.Styler.hide "pandas.io.formats.style.Styler.hide")<br>(\[subset, axis, level, names\]) | Hide the entire index / column headers, or specific rows / columns from display. |
| [`highlight_between`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas.io.formats.style.Styler.highlight_between "pandas.io.formats.style.Styler.highlight_between")<br>(\[subset, color, axis, ...\]) | Highlight a defined range with a style. |
| [`highlight_max`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_max.html#pandas.io.formats.style.Styler.highlight_max "pandas.io.formats.style.Styler.highlight_max")<br>(\[subset, color, axis, props\]) | Highlight the maximum with a style. |
| [`highlight_min`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#pandas.io.formats.style.Styler.highlight_min "pandas.io.formats.style.Styler.highlight_min")<br>(\[subset, color, axis, props\]) | Highlight the minimum with a style. |
| [`highlight_null`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#pandas.io.formats.style.Styler.highlight_null "pandas.io.formats.style.Styler.highlight_null")<br>(\[color, subset, props\]) | Highlight missing values with a style. |
| [`highlight_quantile`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#pandas.io.formats.style.Styler.highlight_quantile "pandas.io.formats.style.Styler.highlight_quantile")<br>(\[subset, color, axis, ...\]) | Highlight values defined by a quantile with a style. |
| [`map`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")<br>(func\[, subset\]) | Apply a CSS-styling function elementwise. |
| [`map_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map_index.html#pandas.io.formats.style.Styler.map_index "pandas.io.formats.style.Styler.map_index")<br>(func\[, axis, level\]) | Apply a CSS-styling function to the index or column headers, elementwise. |
| [`pipe`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.pipe.html#pandas.io.formats.style.Styler.pipe "pandas.io.formats.style.Styler.pipe")<br>(func, \*args, \*\*kwargs) | Apply `func(self, *args, **kwargs)`, and return the result. |
| [`relabel_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.relabel_index.html#pandas.io.formats.style.Styler.relabel_index "pandas.io.formats.style.Styler.relabel_index")<br>(labels\[, axis, level\]) | Relabel the index, or column header, keys to display a set of specified values. |
| [`set_caption`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html#pandas.io.formats.style.Styler.set_caption "pandas.io.formats.style.Styler.set_caption")<br>(caption) | Set the text added to a `<caption>` HTML element. |
| [`set_properties`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html#pandas.io.formats.style.Styler.set_properties "pandas.io.formats.style.Styler.set_properties")<br>(\[subset\]) | Set defined CSS-properties to each `<td>` HTML element for the given subset. |
| [`set_sticky`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html#pandas.io.formats.style.Styler.set_sticky "pandas.io.formats.style.Styler.set_sticky")<br>(\[axis, pixel\_size, levels\]) | Add CSS to permanently display the index or column headers in a scrolling frame. |
| [`set_table_attributes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#pandas.io.formats.style.Styler.set_table_attributes "pandas.io.formats.style.Styler.set_table_attributes")<br>(attributes) | Set the table attributes added to the `<table>` HTML element. |
| [`set_table_styles`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#pandas.io.formats.style.Styler.set_table_styles "pandas.io.formats.style.Styler.set_table_styles")<br>(\[table\_styles, axis, ...\]) | Set the table styles included within the `<style>` HTML element. |
| [`set_td_classes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas.io.formats.style.Styler.set_td_classes "pandas.io.formats.style.Styler.set_td_classes")<br>(classes) | Set the `class` attribute of `<td>` HTML elements. |
| [`set_tooltips`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html#pandas.io.formats.style.Styler.set_tooltips "pandas.io.formats.style.Styler.set_tooltips")<br>(ttips\[, props, css\_class, ...\]) | Set the DataFrame of strings on `Styler` generating `:hover` tooltips. |
| [`set_uuid`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_uuid.html#pandas.io.formats.style.Styler.set_uuid "pandas.io.formats.style.Styler.set_uuid")<br>(uuid) | Set the uuid applied to `id` attributes of HTML elements. |
| [`text_gradient`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html#pandas.io.formats.style.Styler.text_gradient "pandas.io.formats.style.Styler.text_gradient")<br>(\[cmap, low, high, axis, ...\]) | Color the text in a gradient style. |
| [`to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_excel.html#pandas.io.formats.style.Styler.to_excel "pandas.io.formats.style.Styler.to_excel")<br>(excel\_writer\[, sheet\_name, na\_rep, ...\]) | Write Styler to an Excel sheet. |
| [`to_html`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html#pandas.io.formats.style.Styler.to_html "pandas.io.formats.style.Styler.to_html")<br>(\[buf, table\_uuid, table\_attributes, ...\]) | Write Styler to a file, buffer or string in HTML-CSS format. |
| [`to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_latex.html#pandas.io.formats.style.Styler.to_latex "pandas.io.formats.style.Styler.to_latex")<br>(\[buf, column\_format, position, ...\]) | Write Styler to a file, buffer or string in LaTeX format. |
| [`to_string`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_string.html#pandas.io.formats.style.Styler.to_string "pandas.io.formats.style.Styler.to_string")<br>(\[buf, encoding, sparse\_index, ...\]) | Write Styler to a file, buffer or string in text format. |
| [`to_typst`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_typst.html#pandas.io.formats.style.Styler.to_typst "pandas.io.formats.style.Styler.to_typst")<br>(\[buf, encoding, sparse\_index, ...\]) | Write Styler to a file, buffer or string in Typst format. |
| [`use`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#pandas.io.formats.style.Styler.use "pandas.io.formats.style.Styler.use")<br>(styles) | Set the styles on the current Styler. |

On this page