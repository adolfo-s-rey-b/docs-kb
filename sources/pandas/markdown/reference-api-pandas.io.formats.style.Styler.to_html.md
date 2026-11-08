[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.to_html.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.to_html.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.to_html.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.to_html.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.to_html.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.to_html.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.to_html.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.to_html.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.to_html.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.to_html.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.to_html.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.to_html.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.to\_html[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html#pandas-io-formats-style-styler-to-html "Link to this heading")

===================================================================================================================================================================================================

Styler.to\_html(_buf\=None_, _\*_, _table\_uuid\=None_, _table\_attributes\=None_, _sparse\_index\=None_, _sparse\_columns\=None_, _bold\_headers\=False_, _caption\=None_, _max\_rows\=None_, _max\_columns\=None_, _encoding\=None_, _doctype\_html\=False_, _exclude\_styles\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L1443-L1581)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html#pandas.io.formats.style.Styler.to_html "Link to this definition")

Write Styler to a file, buffer or string in HTML-CSS format.

The output includes `<style>` and `<table>` HTML elements with inline CSS, suitable for embedding in web pages or Jupyter notebooks. Use `doctype_html=True` to produce a fully structured HTML document.

Parameters:

**buf**str, path object, file-like object, optional

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a string `write()` function. If `None`, the result is returned as a string.

**table\_uuid**str, optional

Id attribute assigned to the <table> HTML element in the format:

`<table id="T_<table_uuid>" ..>`

If not given uses Styler’s initially assigned value.

**table\_attributes**str, optional

Attributes to assign within the <table> HTML element in the format:

`<table .. <table_attributes> >`

If not given defaults to Styler’s preexisting value.

**sparse\_index**bool, optional

Whether to sparsify the display of a hierarchical index. Setting to False will display each explicit level element in a hierarchical key for each row. Defaults to `pandas.options.styler.sparse.index` value.

**sparse\_columns**bool, optional

Whether to sparsify the display of a hierarchical index. Setting to False will display each explicit level element in a hierarchical key for each column. Defaults to `pandas.options.styler.sparse.columns` value.

**bold\_headers**bool, optional

Adds “font-weight: bold;” as a CSS property to table style header cells.

**caption**str, optional

Set, or overwrite, the caption on Styler before rendering.

**max\_rows**int, optional

The maximum number of rows that will be rendered. Defaults to `pandas.options.styler.render.max_rows/max_columns`.

**max\_columns**int, optional

The maximum number of columns that will be rendered. Defaults to `pandas.options.styler.render.max_columns`, which is None.

Rows and columns may be reduced if the number of total elements is large. This value is set to `pandas.options.styler.render.max_elements`, which is 262144 (18 bit browser rendering).

**encoding**str, optional

Character encoding setting for file output (and meta tags if available). Defaults to `pandas.options.styler.render.encoding` value of “utf-8”.

**doctype\_html**bool, default False

Whether to output a fully structured HTML file including all HTML elements, or just the core `<style>` and `<table>` elements.

**exclude\_styles**bool, default False

Whether to include the `<style>` element and all associated element `class` and `id` identifiers, or solely the `<table>` element without styling identifiers.

**\*\*kwargs**

Any additional keyword arguments are passed through to the jinja2 `self.template.render` process. This is useful when you need to provide additional variables for a custom template.

Returns:

str or None

If buf is None, returns the result as a string. Otherwise returns None.

See also

`DataFrame.to_html`

Write a DataFrame to a file, buffer or string in HTML format.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, 4\]})
\>>> print(df.style.to\_html())
<style type="text/css">
</style>
<table id="T\_1e78e">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T\_1e78e\_level0\_col0" class="col\_heading level0 col0" >A</th>
      <th id="T\_1e78e\_level0\_col1" class="col\_heading level0 col1" >B</th>
    </tr>
...

Copy to clipboard

On this page