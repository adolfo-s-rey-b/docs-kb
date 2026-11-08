[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_uuid.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_uuid.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_uuid.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_uuid[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_uuid.html#pandas-io-formats-style-styler-set-uuid "Link to this heading")

======================================================================================================================================================================================================

Styler.set\_uuid(_uuid_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2505-L2553)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_uuid.html#pandas.io.formats.style.Styler.set_uuid "Link to this definition")

Set the uuid applied to `id` attributes of HTML elements.

Useful for controlling the HTML `id` attributes when embedding multiple styled DataFrames in the same HTML page, ensuring there are no CSS conflicts between them.

Parameters:

**uuid**str

The uuid to be applied to `id` attributes of HTML elements.

Returns:

Styler

Instance of class with specified uuid for id attributes set.

See also

[`Styler.set_caption`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html#pandas.io.formats.style.Styler.set_caption "pandas.io.formats.style.Styler.set_caption")

Set the text added to a `<caption>` HTML element.

[`Styler.set_td_classes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas.io.formats.style.Styler.set_td_classes "pandas.io.formats.style.Styler.set_td_classes")

Set the `class` attribute of `<td>` HTML elements.

[`Styler.set_tooltips`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html#pandas.io.formats.style.Styler.set_tooltips "pandas.io.formats.style.Styler.set_tooltips")

Set the DataFrame of strings on `Styler` generating `:hover` tooltips.

Notes

Almost all HTML elements within the table, and including the `<table>` element are assigned `id` attributes. The format is `T_uuid_<extra>` where `<extra>` is typically a more specific identifier, such as `row1_col2`.

Examples

\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], index\=\["A", "B"\], columns\=\["c1", "c2"\])

Copy to clipboard

You can get the id attributes with the following:

\>>> print((df).style.to\_html())

Copy to clipboard

To add a title to column c1, its id is T\_20a7d\_level0\_col0:

\>>> df.style.set\_uuid("T\_20a7d\_level0\_col0").set\_caption("Test")
...

Copy to clipboard

Please see: [Table visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page