[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.use[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#pandas-io-formats-style-styler-use "Link to this heading")

======================================================================================================================================================================================

Styler.use(_styles_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2437-L2503)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#pandas.io.formats.style.Styler.use "Link to this definition")

Set the styles on the current Styler.

Possibly uses styles from `Styler.export`.

Parameters:

**styles**dict(str, Any)

List of attributes to add to Styler. Dict keys should contain only:

*   “apply”: list of styler functions, typically added with `apply` or `map`.
    
*   “table\_attributes”: HTML attributes, typically added with `set_table_attributes`.
    
*   “table\_styles”: CSS selectors and properties, typically added with `set_table_styles`.
    
*   “hide\_index”: whether the index is hidden, typically added with `hide_index`, or a boolean list for hidden levels.
    
*   “hide\_columns”: whether column headers are hidden, typically added with `hide_columns`, or a boolean list for hidden levels.
    
*   “hide\_index\_names”: whether index names are hidden.
    
*   “hide\_column\_names”: whether column header names are hidden.
    
*   “css”: the css class names used.
    

Returns:

Styler

Instance of class with defined styler attributes added.

See also

[`Styler.export`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas.io.formats.style.Styler.export "pandas.io.formats.style.Styler.export")

Export the non data dependent attributes to the current Styler.

Examples

\>>> styler \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\]).style
\>>> styler2 \= pd.DataFrame(\[\[9, 9, 9\]\]).style
\>>> styler.hide(axis\=0).highlight\_max(axis\=1)
\>>> export \= styler.export()
\>>> styler2.use(export)

Copy to clipboard

On this page