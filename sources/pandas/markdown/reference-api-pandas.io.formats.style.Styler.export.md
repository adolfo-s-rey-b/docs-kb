[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.export[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas-io-formats-style-styler-export "Link to this heading")

===============================================================================================================================================================================================

Styler.export()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L2378-L2435)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.export.html#pandas.io.formats.style.Styler.export "Link to this definition")

Export the styles applied to the current Styler.

Can be applied to a second Styler with `Styler.use`.

Returns:

dict

Contains data-independent (exportable) styles applied to current Styler.

See also

[`Styler.use`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.use.html#pandas.io.formats.style.Styler.use "pandas.io.formats.style.Styler.use")

Set the styles on the current Styler.

`Styler.copy`

Create a copy of the current Styler.

Notes

This method is designed to copy non-data dependent attributes of one Styler to another. It differs from `Styler.copy` where data and data dependent attributes are also copied.

The following items are exported since they are not generally data dependent:

> *   Styling functions added by the `apply` and `map`
>     
> *   Whether axes and names are hidden from the display, if unambiguous.
>     
> *   Table attributes
>     
> *   Table styles
>     

The following attributes are considered data dependent and therefore not exported:

> *   Caption
>     
> *   UUID
>     
> *   Tooltips
>     
> *   Any hidden rows or columns identified by Index labels
>     
> *   Any formatting applied using `Styler.format`
>     
> *   Any CSS classes added using `Styler.set_td_classes`
>     

Examples

\>>> styler \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\]).style
\>>> styler2 \= pd.DataFrame(\[\[9, 9, 9\]\]).style
\>>> styler.hide(axis\=0).highlight\_max(axis\=1)
\>>> export \= styler.export()
\>>> styler2.use(export)

Copy to clipboard

On this page