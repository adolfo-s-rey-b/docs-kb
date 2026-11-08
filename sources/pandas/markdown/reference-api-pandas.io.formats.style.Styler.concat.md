[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.concat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.concat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.concat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.concat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.concat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.concat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.concat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.concat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.concat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.concat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.concat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.concat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.concat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.concat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.concat[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.concat.html#pandas-io-formats-style-styler-concat "Link to this heading")

===============================================================================================================================================================================================

Styler.concat(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L258-L372)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.concat.html#pandas.io.formats.style.Styler.concat "Link to this definition")

Append another Styler to combine the output into a single table.

This method enables combining multiple styled DataFrames into a single HTML, LaTeX, or string output by appending additional summary rows or related data beneath the original table. Styles, formatting, and CSS classes applied to each Styler are preserved in the concatenated result.

Parameters:

**other**Styler

The other Styler object which has already been styled and formatted. The data for this Styler must have the same columns as the original, and the number of index levels must also be the same to render correctly.

Returns:

Styler

Instance of class with specified Styler appended.

See also

[`Styler.clear`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.clear.html#pandas.io.formats.style.Styler.clear "pandas.io.formats.style.Styler.clear")

Reset the `Styler`, removing any previously applied styles.

[`Styler.export`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas.io.formats.style.Styler.export "pandas.io.formats.style.Styler.export")

Export the styles applied to the current Styler.

Notes

The purpose of this method is to extend existing styled dataframes with other metrics that may be useful but may not conform to the original’s structure. For example adding a sub total row, or displaying metrics such as means, variance or counts.

Styles that are applied using the `apply`, `map`, `apply_index` and `map_index`, and formatting applied with `format` and `format_index` will be preserved.

Warning

Only the output methods `to_html`, `to_string` and `to_latex` currently work with concatenated Stylers.

Other output methods, including `to_excel`, **do not** work with concatenated Stylers.

The following should be noted:

> *   `table_styles`, `table_attributes`, `caption` and `uuid` are all inherited from the original Styler and not `other`.
>     
> *   hidden columns and hidden index levels will be inherited from the original Styler
>     
> *   `css` will be inherited from the original Styler, and the value of keys `data`, `row_heading` and `row` will be prepended with `foot0_`. If more concats are chained, their styles will be prepended with `foot1_`, ‘’foot\_2’’, etc., and if a concatenated style have another concatenated style, the second style will be prepended with `foot{parent}_foot{child}_`.
>     

A common use case is to concatenate user defined functions with `DataFrame.agg` or with described statistics via `DataFrame.describe`. See examples.

Examples

A common use case is adding totals rows, or otherwise, via methods calculated in `DataFrame.agg`.

\>>> df \= pd.DataFrame(
...     \[\[4, 6\], \[1, 9\], \[3, 4\], \[5, 5\], \[9, 6\]\],
...     columns\=\["Mike", "Jim"\],
...     index\=\["Mon", "Tue", "Wed", "Thurs", "Fri"\],
... )
\>>> styler \= df.style.concat(df.agg(\["sum"\]).style)

Copy to clipboard

![../../_images/footer_simple.png](https://pandas.pydata.org/docs/_images/footer_simple.png)

Since the concatenated object is a Styler the existing functionality can be used to conditionally format it as well as the original.

\>>> descriptors \= df.agg(\["sum", "mean", lambda s: s.dtype\])
\>>> descriptors.index \= \["Total", "Average", "dtype"\]
\>>> other \= (
...     descriptors.style.highlight\_max(
...         axis\=1, subset\=(\["Total", "Average"\], slice(None))
...     )
...     .format(subset\=("Average", slice(None)), precision\=2, decimal\=",")
...     .map(lambda v: "font-weight: bold;")
... )
\>>> styler \= df.style.highlight\_max(color\="salmon").set\_table\_styles(
...     \[{"selector": ".foot\_row0", "props": "border-top: 1px solid black;"}\]
... )
\>>> styler.concat(other)

Copy to clipboard

![../../_images/footer_extended.png](https://pandas.pydata.org/docs/_images/footer_extended.png)

When `other` has fewer index levels than the original Styler it is possible to extend the index in `other`, with placeholder levels.

\>>> df \= pd.DataFrame(
...     \[\[1\], \[2\]\], index\=pd.MultiIndex.from\_product(\[\[0\], \[1, 2\]\])
... )
\>>> descriptors \= df.agg(\["sum"\])
\>>> descriptors.index \= pd.MultiIndex.from\_product(\[\[""\], descriptors.index\])
\>>> df.style.concat(descriptors.style)

Copy to clipboard

On this page