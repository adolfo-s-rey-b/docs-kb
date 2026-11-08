[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_iceberg.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_iceberg[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_iceberg.html#pandas-dataframe-to-iceberg "Link to this heading")

==================================================================================================================================================================

DataFrame.to\_iceberg(_table\_identifier_, _catalog\_name\=None_, _\*_, _catalog\_properties\=None_, _location\=None_, _append\=False_, _snapshot\_properties\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L3699-L3753)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_iceberg.html#pandas.DataFrame.to_iceberg "Link to this definition")

Write a DataFrame to an Apache Iceberg table.

Added in version 3.0.0.

Warning

to\_iceberg is experimental and may change without warning.

Parameters:

**table\_identifier**str

Table identifier.

**catalog\_name**str, optional

The name of the catalog.

**catalog\_properties**dict of {str: str}, optional

The properties that are used next to the catalog configuration.

**location**str, optional

Location for the table.

**append**bool, default False

If `True`, append data to the table, instead of replacing the content.

**snapshot\_properties**dict of {str: str}, optional

Custom properties to be added to the snapshot summary

See also

[`read_iceberg`](https://pandas.pydata.org/docs/reference/api/pandas.read_iceberg.html#pandas.read_iceberg "pandas.read_iceberg")

Read an Apache Iceberg table.

[`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")

Write a DataFrame in Parquet format.

Examples

\>>> df \= pd.DataFrame(data\={"col1": \[1, 2\], "col2": \[4, 3\]})
\>>> df.to\_iceberg("my\_table", catalog\_name\="my\_catalog")

Copy to clipboard

On this page