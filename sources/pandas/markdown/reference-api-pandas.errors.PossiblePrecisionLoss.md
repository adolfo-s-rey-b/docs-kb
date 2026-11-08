[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossiblePrecisionLoss.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.PossiblePrecisionLoss.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.PossiblePrecisionLoss.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.PossiblePrecisionLoss[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossiblePrecisionLoss.html#pandas-errors-possibleprecisionloss "Link to this heading")

=========================================================================================================================================================================================

exception pandas.errors.PossiblePrecisionLoss[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L954-L969)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.PossiblePrecisionLoss.html#pandas.errors.PossiblePrecisionLoss "Link to this definition")

Warning raised by to\_stata on a column with a value outside or equal to int64.

When the column value is outside or equal to the int64 value the column is converted to a float64 dtype.

See also

`DataFrame.to_stata`

Export DataFrame object to Stata dta format.

Examples

\>>> df \= pd.DataFrame({"s": pd.Series(\[1, 2\*\*53\], dtype\=np.int64)})
\>>> df.to\_stata("test")

Copy to clipboard

On this page