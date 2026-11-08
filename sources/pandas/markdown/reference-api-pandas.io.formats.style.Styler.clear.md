[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.clear.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.clear.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.clear.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.clear.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.clear.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.clear.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.clear.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.clear.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.clear.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.clear.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.clear.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.clear.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.clear.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.clear.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.clear[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.clear.html#pandas-io-formats-style-styler-clear "Link to this heading")

============================================================================================================================================================================================

Styler.clear()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L1912-L1948)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.clear.html#pandas.io.formats.style.Styler.clear "Link to this definition")

Reset the `Styler`, removing any previously applied styles.

Returns None.

See also

[`Styler.apply`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")

Apply a CSS-styling function column-wise, row-wise, or table-wise.

[`Styler.export`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas.io.formats.style.Styler.export "pandas.io.formats.style.Styler.export")

Export the styles applied to the current Styler.

[`Styler.map`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html#pandas.io.formats.style.Styler.map "pandas.io.formats.style.Styler.map")

Apply a CSS-styling function elementwise.

[`Styler.use`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#pandas.io.formats.style.Styler.use "pandas.io.formats.style.Styler.use")

Set the styles on the current Styler.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 2\], "B": \[3, np.nan\]})

Copy to clipboard

After any added style:

\>>> df.style.highlight\_null(color\="yellow")

Copy to clipboard

Remove it with:

\>>> df.style.clear()

Copy to clipboard

Please see: [Table Visualization](https://pandas.pydata.org/docs/user_guide/style.html)
 for more examples.

On this page