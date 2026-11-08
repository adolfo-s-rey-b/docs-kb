[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_iceberg.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_iceberg.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_iceberg.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_iceberg.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_iceberg.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_iceberg.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_iceberg.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_iceberg.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_iceberg.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_iceberg.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_iceberg.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_iceberg.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_iceberg.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_iceberg.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_iceberg[#](https://pandas.pydata.org/docs/reference/api/pandas.read_iceberg.html#pandas-read-iceberg "Link to this heading")

==========================================================================================================================================

pandas.read\_iceberg(_table\_identifier_, _catalog\_name\=None_, _\*_, _catalog\_properties\=None_, _columns\=None_, _row\_filter\=None_, _case\_sensitive\=True_, _snapshot\_id\=None_, _limit\=None_, _scan\_properties\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/iceberg.py#L16-L104)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_iceberg.html#pandas.read_iceberg "Link to this definition")

Read an Apache Iceberg table into a pandas DataFrame.

Added in version 3.0.0.

Warning

read\_iceberg is experimental and may change without warning.

Parameters:

**table\_identifier**str

Table identifier.

**catalog\_name**str, optional

The name of the catalog.

**catalog\_properties**dict of {str: str}, optional

The properties that are used next to the catalog configuration.

**columns**list of str, optional

A list of strings representing the column names to return in the output dataframe.

**row\_filter**str, optional

A string that describes the desired rows.

**case\_sensitive**bool, default True

If True column matching is case sensitive.

**snapshot\_id**int, optional

Snapshot ID to time travel to. By default the table will be scanned as of the current snapshot ID.

**limit**int, optional

An integer representing the number of rows to return in the scan result. By default all matching rows will be fetched.

**scan\_properties**dict of {str: obj}, optional

Additional Table properties as a dictionary of string key value pairs to use for this scan.

Returns:

DataFrame

DataFrame based on the Iceberg table.

See also

[`read_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas.read_parquet "pandas.read_parquet")

Read a Parquet file.

Examples

\>>> df \= pd.read\_iceberg(
...     table\_identifier\="my\_table",
...     catalog\_name\="my\_catalog",
...     catalog\_properties\={"s3.secret-access-key": "my-secret"},
...     row\_filter\="trip\_distance >= 10.0",
...     columns\=\["VendorID", "tpep\_pickup\_datetime"\],
... )

Copy to clipboard

On this page