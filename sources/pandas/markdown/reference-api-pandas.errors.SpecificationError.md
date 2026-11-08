[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.SpecificationError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.SpecificationError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.SpecificationError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.SpecificationError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.SpecificationError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.SpecificationError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.SpecificationError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.SpecificationError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.SpecificationError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.SpecificationError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.SpecificationError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.SpecificationError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.SpecificationError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.SpecificationError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.SpecificationError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.SpecificationError.html#pandas-errors-specificationerror "Link to this heading")

================================================================================================================================================================================

exception pandas.errors.SpecificationError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L656-L684)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.SpecificationError.html#pandas.errors.SpecificationError "Link to this definition")

Exception raised by `agg` when the functions are ill-specified.

The exception raised in two scenarios.

The first way is calling `agg` on a Dataframe or Series using a nested renamer (dict-of-dict).

The second way is calling `agg` on a Dataframe with duplicated functions names without assigning column name.

See also

`DataFrame.agg`

Aggregate using one or more operations over the specified axis.

`Series.agg`

Aggregate using one or more operations over the specified axis.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 1, 1, 2, 2\], "B": range(5), "C": range(5)})
\>>> df.groupby("A").B.agg({"foo": "count"})
... \# SpecificationError: nested renamer is not supported

Copy to clipboard

\>>> df.groupby("A").agg({"B": {"foo": \["sum", "max"\]}})
... \# SpecificationError: nested renamer is not supported

Copy to clipboard

\>>> df.groupby("A").agg(\["min", "min"\])
... \# SpecificationError: nested renamer is not supported

Copy to clipboard

On this page