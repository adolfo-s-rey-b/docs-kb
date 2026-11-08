[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_sql\_table[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#pandas-read-sql-table "Link to this heading")

=================================================================================================================================================

pandas.read\_sql\_table(_table\_name_, _con_, _schema\=None_, _index\_col\=None_, _coerce\_float\=True_, _parse\_dates\=None_, _columns\=None_, _chunksize\=None_, _dtype\_backend\=<no\_default>_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/sql.py#L302-L406)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#pandas.read_sql_table "Link to this definition")

Read SQL database table into a DataFrame.

Given a table name and a SQLAlchemy connectable, returns a DataFrame. This function does not support DBAPI connections.

Parameters:

**table\_name**str

Name of SQL table in database.

**con**SQLAlchemy connectable or str

A database URI could be provided as str. SQLite DBAPI connection mode not supported.

**schema**str, default None

Name of SQL schema in database to query (if database flavor supports this). Uses default schema if None (default).

**index\_col**str or list of str, optional, default: None

Column(s) to set as index(MultiIndex).

**coerce\_float**bool, default True

Attempts to convert values of non-string, non-numeric objects (like decimal.Decimal) to floating point. Can result in loss of Precision.

**parse\_dates**list or dict, default None

*   List of column names to parse as dates.
    
*   Dict of `{column_name: format string}` where format string is strftime compatible in case of parsing string times or is one of (D, s, ns, ms, us) in case of parsing integer timestamps.
    
*   Dict of `{column_name: arg dict}`, where the arg dict corresponds to the keyword arguments of [`pandas.to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
     Especially useful with databases without native Datetime support, such as SQLite.
    

**columns**list, default None

List of column names to select from SQL table.

**chunksize**int, default None

If specified, returns an iterator where chunksize is the number of rows to include in each chunk. By itself this typically does not reduce peak memory usage, as most drivers buffer the full result set unless a server-side cursor is used; see the [user guide](https://pandas.pydata.org/docs/user_guide/io.html#io-sql-chunksize)
 on streaming results.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

Returns:

DataFrame or Iterator\[DataFrame\]

A SQL table is returned as two-dimensional data structure with labeled axes.

See also

[`read_sql_query`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html#pandas.read_sql_query "pandas.read_sql_query")

Read SQL query into a DataFrame.

[`read_sql`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas.read_sql "pandas.read_sql")

Read SQL query or database table into a DataFrame.

Notes

Any datetime values with time zone information will be converted to UTC.

Examples

\>>> pd.read\_sql\_table("table\_name", "postgres:///db\_name")

Copy to clipboard

On this page