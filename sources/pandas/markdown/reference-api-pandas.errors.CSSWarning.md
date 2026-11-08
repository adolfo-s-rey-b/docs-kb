[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.CSSWarning.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.CSSWarning[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.CSSWarning.html#pandas-errors-csswarning "Link to this heading")

========================================================================================================================================================

exception pandas.errors.CSSWarning[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L831-L857)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.CSSWarning.html#pandas.errors.CSSWarning "Link to this definition")

Warning is raised when converting css styling fails.

This can be due to the styling not having an equivalent value or because the styling isn’t properly formatted.

See also

`DataFrame.style`

Returns a Styler object for applying CSS-like styles.

`io.formats.style.Styler`

Helps style a DataFrame or Series according to the data with HTML and CSS.

`io.formats.style.Styler.to_excel`

Export styled DataFrame to Excel.

`io.formats.style.Styler.to_html`

Export styled DataFrame to HTML.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 1, 1\]})
\>>> df.style.map(lambda x: "background-color: blueGreenRed;").to\_excel(
...     "styled.xlsx"
... )
CSSWarning: Unhandled color format: 'blueGreenRed'
\>>> df.style.map(lambda x: "border: 1px solid red red;").to\_excel(
...     "styled.xlsx"
... )
CSSWarning: Unhandled color format: 'blueGreenRed'

Copy to clipboard

On this page