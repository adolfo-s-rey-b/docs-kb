[Skip to main content](https://pandas.pydata.org/docs/reference/style.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/style.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/style.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/style.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/style.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/style.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/style.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/style.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/style.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/style.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/style.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/style.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/style.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/style.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Style[#](https://pandas.pydata.org/docs/reference/style.html#style "Link to this heading")

===========================================================================================

Note

For an overview, see [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
.

`Styler` objects are returned by [`pandas.DataFrame.style`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.style.html#pandas.DataFrame.style "pandas.DataFrame.style")
.

Styler constructor[#](https://pandas.pydata.org/docs/reference/style.html#styler-constructor "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Styler`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html#pandas.io.formats.style.Styler "pandas.io.formats.style.Styler")<br>(data\[, precision, table\_styles, ...\]) | Helps style a DataFrame or Series according to the data with HTML and CSS. |
| [`Styler.from_custom_template`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.from_custom_template.html#pandas.io.formats.style.Styler.from_custom_template "pandas.io.formats.style.Styler.from_custom_template")<br>(searchpath\[, ...\]) | Factory function for creating a subclass of `Styler`. |

Styler properties[#](https://pandas.pydata.org/docs/reference/style.html#styler-properties "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Styler.env`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.env.html#pandas.io.formats.style.Styler.env "pandas.io.formats.style.Styler.env") |     |
| [`Styler.template_html`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_html.html#pandas.io.formats.style.Styler.template_html "pandas.io.formats.style.Styler.template_html") |     |
| [`Styler.template_html_style`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_html_style.html#pandas.io.formats.style.Styler.template_html_style "pandas.io.formats.style.Styler.template_html_style") |     |
| [`Styler.template_html_table`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_html_table.html#pandas.io.formats.style.Styler.template_html_table "pandas.io.formats.style.Styler.template_html_table") |     |
| [`Styler.template_latex`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_latex.html#pandas.io.formats.style.Styler.template_latex "pandas.io.formats.style.Styler.template_latex") |     |
| [`Styler.template_typst`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_typst.html#pandas.io.formats.style.Styler.template_typst "pandas.io.formats.style.Styler.template_typst") |     |
| [`Styler.template_string`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.template_string.html#pandas.io.formats.style.Styler.template_string "pandas.io.formats.style.Styler.template_string") |     |
| [`Styler.loader`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.loader.html#pandas.io.formats.style.Styler.loader "pandas.io.formats.style.Styler.loader") |     |

Style application[#](https://pandas.pydata.org/docs/reference/style.html#style-application "Link to this heading")

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Styler.apply`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")<br>(func\[, axis, subset\]) | Apply a CSS-styling function column-wise, row-wise, or table-wise. |
| [`Styler.map`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")<br>(func\[, subset\]) | Apply a CSS-styling function elementwise. |
| [`Styler.apply_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html#pandas.io.formats.style.Styler.apply_index "pandas.io.formats.style.Styler.apply_index")<br>(func\[, axis, level\]) | Apply a CSS-styling function to the index or column headers, level-wise. |
| [`Styler.map_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map_index.html#pandas.io.formats.style.Styler.map_index "pandas.io.formats.style.Styler.map_index")<br>(func\[, axis, level\]) | Apply a CSS-styling function to the index or column headers, elementwise. |
| [`Styler.format`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html#pandas.io.formats.style.Styler.format "pandas.io.formats.style.Styler.format")<br>(\[formatter, subset, na\_rep, ...\]) | Format the text display value of cells. |
| [`Styler.format_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "pandas.io.formats.style.Styler.format_index")<br>(\[formatter, axis, ...\]) | Format the text display value of index labels or column headers. |
| [`Styler.format_index_names`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index_names.html#pandas.io.formats.style.Styler.format_index_names "pandas.io.formats.style.Styler.format_index_names")<br>(\[formatter, axis, ...\]) | Format the text display value of index names or column names. |
| [`Styler.relabel_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.relabel_index.html#pandas.io.formats.style.Styler.relabel_index "pandas.io.formats.style.Styler.relabel_index")<br>(labels\[, axis, level\]) | Relabel the index, or column header, keys to display a set of specified values. |
| [`Styler.hide`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html#pandas.io.formats.style.Styler.hide "pandas.io.formats.style.Styler.hide")<br>(\[subset, axis, level, names\]) | Hide the entire index / column headers, or specific rows / columns from display. |
| [`Styler.concat`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.concat.html#pandas.io.formats.style.Styler.concat "pandas.io.formats.style.Styler.concat")<br>(other) | Append another Styler to combine the output into a single table. |
| [`Styler.set_td_classes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas.io.formats.style.Styler.set_td_classes "pandas.io.formats.style.Styler.set_td_classes")<br>(classes) | Set the `class` attribute of `<td>` HTML elements. |
| [`Styler.set_table_styles`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#pandas.io.formats.style.Styler.set_table_styles "pandas.io.formats.style.Styler.set_table_styles")<br>(\[table\_styles, ...\]) | Set the table styles included within the `<style>` HTML element. |
| [`Styler.set_table_attributes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#pandas.io.formats.style.Styler.set_table_attributes "pandas.io.formats.style.Styler.set_table_attributes")<br>(attributes) | Set the table attributes added to the `<table>` HTML element. |
| [`Styler.set_tooltips`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html#pandas.io.formats.style.Styler.set_tooltips "pandas.io.formats.style.Styler.set_tooltips")<br>(ttips\[, props, ...\]) | Set the DataFrame of strings on `Styler` generating `:hover` tooltips. |
| [`Styler.set_caption`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html#pandas.io.formats.style.Styler.set_caption "pandas.io.formats.style.Styler.set_caption")<br>(caption) | Set the text added to a `<caption>` HTML element. |
| [`Styler.set_sticky`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html#pandas.io.formats.style.Styler.set_sticky "pandas.io.formats.style.Styler.set_sticky")<br>(\[axis, pixel\_size, levels\]) | Add CSS to permanently display the index or column headers in a scrolling frame. |
| [`Styler.set_properties`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html#pandas.io.formats.style.Styler.set_properties "pandas.io.formats.style.Styler.set_properties")<br>(\[subset\]) | Set defined CSS-properties to each `<td>` HTML element for the given subset. |
| [`Styler.set_uuid`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_uuid.html#pandas.io.formats.style.Styler.set_uuid "pandas.io.formats.style.Styler.set_uuid")<br>(uuid) | Set the uuid applied to `id` attributes of HTML elements. |
| [`Styler.clear`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.clear.html#pandas.io.formats.style.Styler.clear "pandas.io.formats.style.Styler.clear")<br>() | Reset the `Styler`, removing any previously applied styles. |
| [`Styler.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.pipe.html#pandas.io.formats.style.Styler.pipe "pandas.io.formats.style.Styler.pipe")<br>(func, \*args, \*\*kwargs) | Apply `func(self, *args, **kwargs)`, and return the result. |

Builtin styles[#](https://pandas.pydata.org/docs/reference/style.html#builtin-styles "Link to this heading")

-------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Styler.highlight_null`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html#pandas.io.formats.style.Styler.highlight_null "pandas.io.formats.style.Styler.highlight_null")<br>(\[color, subset, props\]) | Highlight missing values with a style. |
| [`Styler.highlight_max`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_max.html#pandas.io.formats.style.Styler.highlight_max "pandas.io.formats.style.Styler.highlight_max")<br>(\[subset, color, axis, ...\]) | Highlight the maximum with a style. |
| [`Styler.highlight_min`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html#pandas.io.formats.style.Styler.highlight_min "pandas.io.formats.style.Styler.highlight_min")<br>(\[subset, color, axis, ...\]) | Highlight the minimum with a style. |
| [`Styler.highlight_between`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html#pandas.io.formats.style.Styler.highlight_between "pandas.io.formats.style.Styler.highlight_between")<br>(\[subset, color, ...\]) | Highlight a defined range with a style. |
| [`Styler.highlight_quantile`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html#pandas.io.formats.style.Styler.highlight_quantile "pandas.io.formats.style.Styler.highlight_quantile")<br>(\[subset, color, ...\]) | Highlight values defined by a quantile with a style. |
| [`Styler.background_gradient`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.background_gradient.html#pandas.io.formats.style.Styler.background_gradient "pandas.io.formats.style.Styler.background_gradient")<br>(\[cmap, low, ...\]) | Color the background in a gradient style. |
| [`Styler.text_gradient`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html#pandas.io.formats.style.Styler.text_gradient "pandas.io.formats.style.Styler.text_gradient")<br>(\[cmap, low, high, ...\]) | Color the text in a gradient style. |
| [`Styler.bar`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.bar.html#pandas.io.formats.style.Styler.bar "pandas.io.formats.style.Styler.bar")<br>(\[subset, axis, color, cmap, ...\]) | Draw bar chart in the cell backgrounds. |

Style export and import[#](https://pandas.pydata.org/docs/reference/style.html#style-export-and-import "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Styler.to_html`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html#pandas.io.formats.style.Styler.to_html "pandas.io.formats.style.Styler.to_html")<br>(\[buf, table\_uuid, ...\]) | Write Styler to a file, buffer or string in HTML-CSS format. |
| [`Styler.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_latex.html#pandas.io.formats.style.Styler.to_latex "pandas.io.formats.style.Styler.to_latex")<br>(\[buf, column\_format, ...\]) | Write Styler to a file, buffer or string in LaTeX format. |
| [`Styler.to_typst`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_typst.html#pandas.io.formats.style.Styler.to_typst "pandas.io.formats.style.Styler.to_typst")<br>(\[buf, encoding, ...\]) | Write Styler to a file, buffer or string in Typst format. |
| [`Styler.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_excel.html#pandas.io.formats.style.Styler.to_excel "pandas.io.formats.style.Styler.to_excel")<br>(excel\_writer\[, sheet\_name, ...\]) | Write Styler to an Excel sheet. |
| [`Styler.to_string`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_string.html#pandas.io.formats.style.Styler.to_string "pandas.io.formats.style.Styler.to_string")<br>(\[buf, encoding, ...\]) | Write Styler to a file, buffer or string in text format. |
| [`Styler.export`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas.io.formats.style.Styler.export "pandas.io.formats.style.Styler.export")<br>() | Export the styles applied to the current Styler. |
| [`Styler.use`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#pandas.io.formats.style.Styler.use "pandas.io.formats.style.Styler.use")<br>(styles) | Set the styles on the current Styler. |

On this page