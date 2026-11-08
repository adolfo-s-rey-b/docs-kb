[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.ValueLabelTypeMismatch.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.ValueLabelTypeMismatch.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.ValueLabelTypeMismatch.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.ValueLabelTypeMismatch[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ValueLabelTypeMismatch.html#pandas-errors-valuelabeltypemismatch "Link to this heading")

============================================================================================================================================================================================

exception pandas.errors.ValueLabelTypeMismatch[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L972-L990)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ValueLabelTypeMismatch.html#pandas.errors.ValueLabelTypeMismatch "Link to this definition")

Warning raised by to\_stata on a category column that contains non-string values.

When exporting data to Stata format using the to\_stata method, category columns must have string values as labels. If a category column contains non-string values (e.g., integers, floats, or other types), this warning is raised to indicate that the Stata file may not correctly represent the data.

See also

`DataFrame.to_stata`

Export DataFrame object to Stata dta format.

`Series.cat`

Accessor for categorical properties of the Series values.

Examples

\>>> df \= pd.DataFrame({"categories": pd.Series(\["a", 2\], dtype\="category")})
\>>> df.to\_stata("test")

Copy to clipboard

On this page