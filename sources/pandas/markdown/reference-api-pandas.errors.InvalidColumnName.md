[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidColumnName.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.InvalidColumnName.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidColumnName.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.InvalidColumnName.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.InvalidColumnName.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.InvalidColumnName.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.InvalidColumnName.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.InvalidColumnName.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.InvalidColumnName.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.InvalidColumnName.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.InvalidColumnName.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.InvalidColumnName.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.InvalidColumnName.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.InvalidColumnName.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.InvalidColumnName[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidColumnName.html#pandas-errors-invalidcolumnname "Link to this heading")

=============================================================================================================================================================================

exception pandas.errors.InvalidColumnName[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L993-L1008)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.InvalidColumnName.html#pandas.errors.InvalidColumnName "Link to this definition")

Warning raised by to\_stata the column contains a non-valid stata name.

Because the column name is an invalid Stata variable, the name needs to be converted.

See also

`DataFrame.to_stata`

Export DataFrame object to Stata dta format.

Examples

\>>> df \= pd.DataFrame({"0categories": pd.Series(\[2, 2\])})
\>>> df.to\_stata("test")

Copy to clipboard

On this page