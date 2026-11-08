[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.read_sql.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.read_sql.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.read_sql.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.read_sql.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.read_sql.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.read_sql.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.read_sql.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.read_sql.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.read_sql.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.read_sql.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.read_sql.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.read_sql.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.read\_sql[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas-read-sql "Link to this heading")

==============================================================================================================================

pandas.read\_sql(_sql_, _con_, _index\_col\=None_, _coerce\_float\=True_, _params\=None_, _parse\_dates\=None_, _columns\=None_, _chunksize\=None_, _dtype\_backend\=<no\_default>_, _dtype\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/sql.py#L581-L789)
[#](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html#pandas.read_sql "Link to this definition")

Read SQL query or database table into a DataFrame.

This function is a convenience wrapper around `read_sql_table` and `read_sql_query` (for backward compatibility). It will delegate to the specific function depending on the provided input. A SQL query will be routed to `read_sql_query`, while a database table name will be routed to `read_sql_table`. Note that the delegated function might have more specific notes about their functionality not listed here.

Parameters:

**sql**str or SQLAlchemy Selectable (select or text object)

SQL query to be executed or a table name.

**con**ADBC Connection, SQLAlchemy connectable, str, or sqlite3 connection

ADBC provides high performance I/O with native type support, where available. Using SQLAlchemy makes it possible to use any DB supported by that library. If a DBAPI2 object, only sqlite3 is supported. The user is responsible for engine disposal and connection closure for the ADBC connection and SQLAlchemy connectable; str connections are closed automatically. See [here](https://docs.sqlalchemy.org/en/20/core/connections.html)
.

Added in version 2.2.0: Support for ADBC drivers.

**index\_col**str or list of str, optional, default: None

Column(s) to set as index(MultiIndex).

**coerce\_float**bool, default True

Attempts to convert values of non-string, non-numeric objects (like decimal.Decimal) to floating point, useful for SQL result sets. This can lose precision: an integral `decimal.Decimal` larger than `2**53` has no exact `float64` representation, so a long identifier can be silently rounded. Pass `False` to leave such values as Python objects in an `object`\-dtype column.

**params**list, tuple or dict, optional, default: None

List of parameters to pass to execute method. The syntax used to pass parameters is database driver dependent. Check your database driver documentation for which of the five syntax styles, described in PEP 249’s paramstyle, is supported. Eg. for psycopg2, uses %(name)s so use params={‘name’ : ‘value’}.

**parse\_dates**list or dict, default: None

*   List of column names to parse as dates.
    
*   Dict of `{column_name: format string}` where format string is strftime compatible in case of parsing string times, or is one of (D, s, ns, ms, us) in case of parsing integer timestamps.
    
*   Dict of `{column_name: arg dict}`, where the arg dict corresponds to the keyword arguments of [`pandas.to_datetime()`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")
     Especially useful with databases without native Datetime support, such as SQLite.
    

**columns**list, default: None

List of column names to select from SQL table (only used when reading a table).

**chunksize**int, default None

If specified, return an iterator where chunksize is the number of rows to include in each chunk. By itself this typically does not reduce peak memory usage, as most drivers buffer the full result set unless a server-side cursor is used; see the [user guide](https://pandas.pydata.org/docs/user_guide/io.html#io-sql-chunksize)
 on streaming results.

**dtype\_backend**{‘numpy\_nullable’, ‘pyarrow’}

Back-end data type applied to the resultant [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (still experimental). If not specified, the default behavior is to not use nullable data types. If specified, the behavior is as follows:

*   `"numpy_nullable"`: returns nullable-dtype-backed [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    
*   `"pyarrow"`: returns pyarrow-backed nullable [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
     [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    

Added in version 2.0.

**dtype**Type name or dict of columns

Data type for data or columns. E.g. np.float64 or {‘a’: np.float64, ‘b’: np.int32, ‘c’: ‘Int64’}. The argument is ignored if a table is passed instead of a query.

Added in version 2.0.0.

Returns:

DataFrame or Iterator\[DataFrame\]

Returns a DataFrame object that contains the result set of the executed SQL query or an SQL Table based on the provided input, in relation to the specified database connection.

See also

[`read_sql_table`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_table.html#pandas.read_sql_table "pandas.read_sql_table")

Read SQL database table into a DataFrame.

[`read_sql_query`](https://pandas.pydata.org/docs/reference/api/pandas.read_sql_query.html#pandas.read_sql_query "pandas.read_sql_query")

Read SQL query into a DataFrame.

Notes

`pandas` does not attempt to sanitize SQL statements; instead it simply forwards the statement you are executing to the underlying driver, which may or may not sanitize from there. Please refer to the underlying driver documentation for any details. Generally, be wary when accepting statements from arbitrary sources.

Examples

Read data from SQL via either a SQL query or a SQL tablename. When using a SQLite database only SQL queries are accepted, providing only the SQL tablename will result in an error.

\>>> from sqlite3 import connect
\>>> conn \= connect(":memory:")
\>>> df \= pd.DataFrame(
...     data\=\[\[0, "10/11/12"\], \[1, "12/11/10"\]\],
...     columns\=\["int\_column", "date\_column"\],
... )
\>>> df.to\_sql(name\="test\_data", con\=conn)
2

Copy to clipboard

\>>> pd.read\_sql("SELECT int\_column, date\_column FROM test\_data", conn)
   int\_column date\_column
0           0    10/11/12
1           1    12/11/10

Copy to clipboard

\>>> pd.read\_sql("test\_data", "postgres:///db\_name")

Copy to clipboard

For parameterized query, using `params` is recommended over string interpolation.

\>>> from sqlalchemy import text
\>>> sql \= text(
...     "SELECT int\_column, date\_column FROM test\_data WHERE int\_column=:int\_val"
... )
\>>> pd.read\_sql(sql, conn, params\={"int\_val": 1})
   int\_column date\_column
0           1    12/11/10

Copy to clipboard

Apply date parsing to columns through the `parse_dates` argument The `parse_dates` argument calls `pd.to_datetime` on the provided columns. Custom argument values for applying `pd.to_datetime` on a column are specified via a dictionary format:

\>>> pd.read\_sql(
...     "SELECT int\_column, date\_column FROM test\_data",
...     conn,
...     parse\_dates\={"date\_column": {"format": "%d/%m/%y"}},
... )
   int\_column date\_column
0           0  2012-11-10
1           1  2010-11-12

Copy to clipboard

pandas supports reading via ADBC drivers:

\>>> from adbc\_driver\_postgresql import dbapi
\>>> with dbapi.connect("postgres:///db\_name") as conn:
...     pd.read\_sql("SELECT int\_column FROM test\_data", conn)
   int\_column
0           0
1           1

Copy to clipboard

On this page