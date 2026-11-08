[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.set\_table\_attributes[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#pandas-io-formats-style-styler-set-table-attributes "Link to this heading")

===========================================================================================================================================================================================================================================

Styler.set\_table\_attributes(_attributes_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2346-L2376)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html#pandas.io.formats.style.Styler.set_table_attributes "Link to this definition")

Set the table attributes added to the `<table>` HTML element.

These are items in addition to automatic (by default) `id` attribute.

Parameters:

**attributes**str

Table attributes to be added to the `<table>` HTML element.

Returns:

Styler

Instance of class with specified table attributes set.

See also

[`Styler.set_table_styles`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html#pandas.io.formats.style.Styler.set_table_styles "pandas.io.formats.style.Styler.set_table_styles")

Set the table styles included within the `<style>` HTML element.

[`Styler.set_td_classes`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html#pandas.io.formats.style.Styler.set_td_classes "pandas.io.formats.style.Styler.set_td_classes")

Set the DataFrame of strings added to the `class` attribute of `<td>` HTML elements.

Examples

\>>> df \= pd.DataFrame(np.random.randn(10, 4))
\>>> df.style.set\_table\_attributes('class="pure-table"')
\# ... <table class="pure-table"> ...

Copy to clipboard

On this page