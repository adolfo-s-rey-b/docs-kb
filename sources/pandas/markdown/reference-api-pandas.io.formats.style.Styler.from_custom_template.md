[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.from_custom_template.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.from_custom_template.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.from\_custom\_template[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.from_custom_template.html#pandas-io-formats-style-styler-from-custom-template "Link to this heading")

===========================================================================================================================================================================================================================================

classmethod Styler.from\_custom\_template(_searchpath_, _html\_table\=None_, _html\_style\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L4010-L4067)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.from_custom_template.html#pandas.io.formats.style.Styler.from_custom_template "Link to this definition")

Factory function for creating a subclass of `Styler`.

Uses custom templates and Jinja environment.

Parameters:

**searchpath**str or list

Path or paths of directories containing the templates.

**html\_table**str

Name of your custom template to replace the html\_table template.

**html\_style**str

Name of your custom template to replace the html\_style template.

Returns:

**MyStyler**subclass of Styler

Has the correct `env`, `template_html`, `template_html_table` and `template_html_style` class attributes set.

See also

[`Styler.export`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas.io.formats.style.Styler.export "pandas.io.formats.style.Styler.export")

Export the styles applied to the current Styler.

[`Styler.use`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#pandas.io.formats.style.Styler.use "pandas.io.formats.style.Styler.use")

Set the styles on the current Styler.

Examples

\>>> from pandas.io.formats.style import Styler
\>>> EasyStyler \= Styler.from\_custom\_template(
...     "path/to/template",
...     "template.tpl",
... )
\>>> df \= pd.DataFrame({"A": \[1, 2\]})
\>>> EasyStyler(df)

Copy to clipboard

Please see: [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page